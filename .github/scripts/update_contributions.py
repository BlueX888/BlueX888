#!/usr/bin/env python3
"""刷新 README 里两个自动生成的区块。

- contributions：代码合并（GraphQL search 抓取已合并到他人仓库的 PR）与问题获修（ISSUES_FIXED）——
  上游仓库头像墙 + 每个 PR、每个获修问题一条可折叠说明；
- bug-stats：缺陷表上方的数字条，逐行统计手工维护的 `## 🔍` 缺陷表，改完表跑一次本脚本即可跟上。

用法: GITHUB_TOKEN=xxx python3 update_contributions.py README.md
"""
import html
import json
import math
import os
import re
import sys
import urllib.request
from collections import Counter

USER = "BlueX888"
START, END = "<!--START_SECTION:contributions-->", "<!--END_SECTION:contributions-->"
BUG_START, BUG_END = "<!--START_SECTION:bug-stats-->", "<!--END_SECTION:bug-stats-->"
# 头像墙每行最多几个仓库，再多就均分成几行，免得在主页上被挤扁
WALL_PER_ROW = 5
# 与 pr-tracker 的 homepage_sync.py 同一口径：区块里每个 PR 至少要有一个 markdown 形式的 `(…/pull/N)` 链接
# （render_entry 把它写在 HTML 注释里，页面上不显示）
PR_LINK = re.compile(r"\((https://github\.com/[^)\s]+/pull/\d+)\)")

# 每个已合并 PR 的一句话说明（问题 → 影响 → 修法），键为 owner/repo#number。
# 目前主页只列标题、不展示这些说明；pr-tracker 仍按这里检查新合并的 PR 有没有补说明。
NOTES = {
    "PrefectHQ/fastmcp#5672": (
        "`Tool.from_tool` 的 `TransformedTool.run` 只认协程函数与普通同步 callable 两条派发路径，生成器结果"
        "被原样交给 `convert_result`——生成器体在迭代时才执行：同步生成器在文本序列化时被消费、构建 "
        "`structured_content` 时已耗尽，`content` 与 `structured_content` 全空；async 生成器函数不是协程"
        "函数、被当普通 callable 扔进线程池，生成器对象序列化成 repr，直接抛「has an output schema but did "
        "not return structured content」；带注入依赖的 transform 还可能把阻塞生成器跑在事件循环上。"
        "修复在依赖注入之前包裹函数体并复用普通工具的物化路径：同步迭代留在 worker、异步迭代留在本次调用内，"
        "`_current_tool` 与 `forward()` 照常可用，body 校验失败仍按工具执行错误返回。"
    ),
    "PrefectHQ/fastmcp#5843": (
        "函数 resource/template 声明组件级 `meta=` 且返回 `list[ResourceContent]` 时，组件 meta 在每一项上被丢掉"
        "（`list_resources` 却照常公告），只有 list 形状受影响，`str`/`bytes`/JSON 返回都正常。修复在 "
        "`convert_raw_to_resource_result` 为 list 增加显式分支：先按 `ResourceResult` 校验（非 "
        "`ResourceContent` 成员仍抛 `TypeError`），再逐项把组件 meta 合并进副本（项级键优先、不改调用方对象）；"
        "没有公开 meta 时原样返回，空列表与模板路径行为不变。"
    ),
    "PrefectHQ/fastmcp#5823": (
        "`SKILL.md` frontmatter 的 `description` 写成 YAML 序列或映射时，`parse_frontmatter` 返回 list/dict，"
        "`SkillProvider._load_skill` 原样存下，`SkillResource(description=...)` 的 pydantic 校验随即失败——"
        "`list_resources`/`get_resource` 抛错，技能从 provider 列表里静默消失（目录模式只剩一条 warning）。"
        "修复只接受 `str` 类型的 description，其余按缺失处理并回退到正文第一条有意义的行（再回退 "
        "`Skill: {name}`），资源列表恢复完整。"
    ),
    "mcp-use/mcp-use#2651": (
        "`RemoteAgent.run` 用 `result.status === \"error\" || result.error !== null` 判定失败，200 成功响应"
        "只要缺 `error` 键就被拒（`undefined !== null`），与注释和下方成功分支相悖；错误插值还把对象错误值"
        "渲染成 `[object Object]`。修复改为 `result.error != null`（缺失/`null` 都算成功，真实错误与 "
        "`status:\"error\"` 仍拒绝），对象错误用 `JSON.stringify` 展示，并删掉永远匹配不上的 "
        "`String(result).includes(...)` 死代码。"
    ),
    "mcp-use/mcp-use#2551": (
        "OpenAI Responses 驱动的流式工具调用缓冲按 `call_id` 索引，而 "
        "`response.function_call_arguments.delta/done` 携带的是 output item id（`fc_...`），查不到缓冲就永不"
        "发出 `tool-call-args-delta`/`tool-call-ready`——工具照常执行但 `agent.stream()`/`streamEvents()` 对"
        "工具调用产出零 AgentStep，缺陷是静默的。修复按 `item.id` 索引缓冲并在事件里继续使用 MCP 侧的 "
        "`call_id`，两种 id 都保存以保持 `toolCallId` 与 `tool-result` 对齐。"
    ),
    "strands-agents/harness-sdk#4981": (
        "`deepCopyWithValidation` 的 replacer 路径栈只压不弹：嵌套对象/数组序列化完后陈旧帧留在栈顶，后续"
        "兄弟节点的不可序列化值继承已完成子树的路径——`StateStore`/router 元数据校验把 "
        "`{ nested: {x:1}, bad: fn }` 报成 `value for key \"a\".nested.bad` 而非 `\"a\".bad`。修复让每个"
        "栈帧记录其对象并按当前序列化对象回弹，路径始终相对真实父级。"
    ),
    "livekit/agents#7929": (
        "legacy `connect` 命令解析 `--url`/`--api-key`/`--api-secret` 却只拿它们调房间 API，从未 "
        "`server.update_options(...)`（`start`/`dev` 都会），`simulate_job` 因此按构造时/环境变量生成 job "
        "连接：环境里没有或只有不同凭据时模拟 job 带着空/错凭据、agent 无法入会。修复在 server 启动前把"
        "真值参数传给 `update_options`，与 `_run_worker` 一致，未提供的 flag 仍回落环境变量。"
    ),
    "bytedance/deer-flow#6981": (
        "`HonchoMemoryManager.search` 无视调用方给的 `category`：查询始终发同一条未过滤语句，命中之后再把"
        "请求的 category 标签贴到每个结果上——`memory_search(category=\"preference\")` 变成「先按相关度取"
        "top-k，再统一标成 preference」，与 `MemoryManager.search` 契约「category 在 top_k 切片**之前**过滤」"
        "以及工具承诺「Only facts with this exact category are returned」相悖；mem0、OpenViking 两个后端都按"
        "服务端过滤。修复把 category 作为 Honcho 排序查询的服务端 filter"
        "（`filters={\"metadata\": {\"category\": ...}}`，v3 search 端点在其 limit 之前应用），"
        "并按每条记录自身元数据标注结果。"
    ),
    "bytedance/deer-flow#7039": (
        "`config.yaml` profile 同时声明 `reasoning:` 契约和真值但非 mapping 的 "
        "`when_thinking_enabled.extra_body`（例如把 payload 写成字符串 `extra_body: oops`、或写成 `true`）"
        "时配置能加载、模型却完全不可用：`ModelConfig.when_thinking_enabled` 是无逐键校验的 `dict | None`，"
        "契约校验器的 `_lookup_dotted` 对这种形状直接返回 `None`，随后**每次** `create_chat_model` 都抛 "
        "`AttributeError: 'str' object has no attribute 'get'`——lead agent、子代理、标题生成与摘要全走这个工厂，"
        "整个后端为该模型瘫掉；legacy（无 `reasoning:` 契约）的启用路径早已原样转发非 mapping 模板值。"
        "修复让契约路径把真值非 mapping 的 `extra_body` 与缺失/null 同等对待：`_infer_dialect` 与 "
        "`_apply_contract_thinking_settings` 共用 `isinstance(..., dict)` 守卫，启用方向仍原样转发模板值、"
        "禁用方向继续合成方言 payload——已能构建的 profile 行为逐字节不变。"
    ),
    "bytedance/deer-flow#7002": (
        "local-sandbox 模式的 forward（容器→宿主）路径翻译在 `write_file` 内容、bash 命令"
        "（skills/ACP/自定义挂载）与用户数据命令解析三处尾部模式里都不在 `:` 处结束，冒号连接列表"
        "只有第一项被翻成宿主路径、其余仍是容器内虚拟路径："
        "`export PATH=\"/mnt/user-data/workspace/bin:/mnt/user-data/outputs/bin\"` 落盘后第二项悬空，"
        "之后 source 该文件或 runner 脚本会继承只存在于容器路径契约里的条目；`read_file` 又把混合行"
        "掩回原始虚拟文本，模型看不到损坏。反向翻译的 `path_patterns._PATH_TAIL` 早已为此在 `:` 处"
        "结束尾部。修复在三处 forward 尾部停止集合里加入 `:`，替换在每个列表项处续接；"
        "单条目形式 `$PATH` 后缀与裸根路径行为不变。"
    ),
    "livekit/agents#7894": (
        "`livekit.agents.llm.__all__` 里留着 `RealtimeSessionRestoredEvent`——全仓仅此一处出现该名字，"
        "真正的类是 `RealtimeSessionReconnectedEvent`（`llm/realtime.py`），显然是一次改名/删除留下的"
        "幽灵条目：`from livekit.agents.llm import *` 在 3.12 抛 "
        "`AttributeError: module 'livekit.agents.llm' has no attribute 'RealtimeSessionRestoredEvent'`"
        "（旧版本是 `ImportError`），任何星号导入公共 API 的调用方在导入期就崩；79 个导出里恰好 1 个"
        "没有后备属性（修复后 78 个全部可解析）。仓内 "
        "`tests/test_inference_utils.py::test_public_inference_exports_resolve` "
        "已为 `inference.__all__` 立了同款守卫。修复删掉该条目，并补一份镜像测试逐个断言 "
        "`llm.__all__` 都能解析。"
    ),
    "bytedance/deer-flow#6839": (
        "MindIE 的 XML tool-call parser 对 `json.loads` 拒收的 `{` 开头参数值回退 `ast.literal_eval`，"
        "解析值按设计流入 tool-call args 以满足下游 Pydantic 校验——模型吐出 set 字面量 `{1, 2, 3}` 即产出"
        "带 Python `set` 的 AIMessage；该消息留在会话历史里，下一轮 `_fix_messages` 重序列化为 XML wire 格式时"
        "对非 str 值走无守卫的 `json.dumps(v, ensure_ascii=False)`，`TypeError: Object of type set is not JSON "
        "serializable`，且消息不离开历史，线程此后每个请求都失败而非仅那一次工具调用。同函数 ToolMessage "
        "json-block 分支早有「Circular 抛 ValueError、其余不可序列化抛 TypeError，一律降级 `str()`」的先例，"
        "AIMessage args join 是唯一没有该兜底的序列化点。改为新增 `_render_tool_arg` helper 路由 args join："
        "字符串原样、其余值 json.dumps 失败降级 `str(v)`，与既有分支同构，补 parser→AIMessage→下一轮 "
        "`_fix_messages` 的 round-trip 回归。"
    ),
    "bytedance/deer-flow#6838": (
        "`config.yaml` profile 的空 YAML 键（`extra_body:` → 显式 null）被 `ModelConfig.when_thinking_enabled`"
        "（无逐键校验的 `dict | None`）静默接受，legacy（无 `reasoning:` 契约）thinking 禁用路径却用 "
        "`effective_wte.get(\"extra_body\", {})` 读模板——`dict.get(key, {})` 只兜「键缺失」，显式 `None` "
        "原样返回，链式 `.get` 抛 `AttributeError: 'NoneType' object has no attribute 'get'`；"
        "`thinking_enabled=False` 是每个 `create_chat_model` 调用点（标题生成、摘要、子代理与 lead-agent 构建）"
        "的默认值，首个模型构建即崩而非罕见开关组合。同模块 `_infer_dialect` 与契约路径都已是 "
        "`get(...) or {}` 的守卫写法，同一 profile 挂上 `reasoning:` 契约反而能正常构建。"
        "改为 legacy 路径三处模板读取统一 `(effective_wte.get(key) or {})`，null 模板键与缺失键同样落进"
        "方言启发式，补双 thinking 方向、三种 null 模板形态的回归。"
    ),
    "livekit/agents#7733": (
        "`BM25SearchStrategy` 的查询归一化把 `_` 换成空格，工具名与参数键的分词也做同样拆分，"
        "唯独描述 token 与参数描述值只按空白切——描述里的 `snake_case` 术语被索引成单个 token，"
        "而每个查询都先替换掉 `_`、不可能含它，`checking_balance` 这类写在描述里的术语搜索永远 0 分，"
        "`tool_search` 对描述里明确写着该术语的工具抛 `No tools found`。"
        "改为对描述与参数描述 token 应用与名字/键相同的下划线拆分，补跨两种策略、两种查询拼法的回归测试。"
    ),
    "bytedance/deer-flow#6733": (
        "`memory_add` 文档明文允许自由 category 标签（示例给出 \"personal\"），`memory_search` 承诺"
        "「Only facts with this exact category are returned」，`storage._normalize_category` 却把核心类目之外的"
        "标签一律改写成 \"other\"、原文只存进全仓无代码读取的 `categoryExtension` 字段——"
        "`memory_add(category=\"personal\")` 落库即 \"other\"、按 \"personal\" 永远搜不到，"
        "记忆设置页的自由文本分类输入与 fact 抽取 prompt 自带的 `knowledge` 枚举（不在核心类目里）"
        "也被同一改写折进 \"other\"。改为保留调用方标签作为存储 `category`（空串仍回退 \"context\"），"
        "非核心标签在 create/update、get_memory 文档、FTS5 检索索引与分类过滤中全程 round-trip。"
    ),
    "bytedance/deer-flow#6732": (
        "检索适配器关闭时（`retrieval_adapter: \"\"` 是文档化的配置）substring 搜索走 "
        "`FileMemoryStorage._search_substring`，它遍历默认 `limit: 100` 的分页 `list_facts` 且从不翻页——"
        "一个 scope 有 150 条匹配、`top_k=150` 也只返回前 100 条，违反 `MemoryManager.search` "
        "「return up to `top_k`」的契约；索引结果非空时上层 `DeerMem.search` 不会再落到无上限的兜底路径，"
        "同文件 scoped `rebuild_index` 早已为「bulk replace 会丢掉没读到的行」读完整 scope。"
        "改为按同样方式读全量事实、原位套用 filters，补回归测试。"
    ),
    "agentscope-ai/agentscope#3242": (
        "流式语音的最终 `is_last` 音频 `DataBlock` 保留流式 WAV 头的 `0xFFFFFFFF` RIFF/data 占位大小——"
        "两个流式 parser 只给首个 delta 加流式头，累积器把后续 delta 原样拼进完成块，完成的音频不是合法 WAV、"
        "与同一调用非流式路径的产物不一致，信任头部的消费方（`wave.getnframes()`、时长、seek、严格播放器）"
        "看到 4294967295 而非实际音频长度。改为在最终块声明真实 RIFF/data 尺寸。"
    ),
    "livekit/agents#7734": (
        "`ToolProxyToolset` 的 `call_tool` 工具描述与 unknown-tool 报错都让模型「用 `search_tools` 发现工具」，"
        "而该工具集实际暴露的搜索工具由父类 `ToolSearchToolset` 以 `tool_search` 之名创建、测试也断言这个名字——"
        "两段字符串都是 LLM 可见的，照自己指令行事的模型会去调用一个不存在的工具。改为引用真实工具名 `tool_search`。"
    ),
    "bytedance/deer-flow#6478": (
        "MindIE 的无工具原生流式逐 chunk 调 `_decode_escaped_newlines_outside_fences`，而该助手靠输入里成对的围栏定界符判断围栏——"
        "token 大小的 chunk 几乎不可能同时含一对定界符，围栏判定永不生效，chunk 里每个字面 `\\n`（包括完整回复中位于围栏内的代码）"
        "都被解成真换行：`print(\"a\\nb\")` 的转义被拆成两行写进用户可见消息与持久化内容，而非流式路径（`_generate`/`_agenerate`）"
        "与开工具的模拟流都保留转义。改为用带围栏状态的解码器跨 chunk 维持围栏状态、复用同一实现，跨 chunk 的半个围栏定界符或 `\\` "
        "留到下一 chunk 决定，流末未决文本作为最后一个 chunk 吐出。"
    ),
    "Arize-ai/phoenix#16535": (
        "`_ToolKwargsConversion.to_anthropic` 在存档 prompt 的 `tool_choice` 为 `\"none\"` 时立即 `return {}`，"
        "把此前已装好的 `ans[\"tools\"]` 一并丢掉——带工具但禁用工具使用的捕获请求，回放时 tools 整个消失；"
        "服务端 playground 本就同时发 tools 与 `tool_choice: none`，同文件 `_ToolChoiceConversion` 的 to/from 两个方向"
        "都早已正确映射 `\"none\"`，只有这条早退绕开了既有处理。改为删掉早退，让 tool_choice 走既有映射、tools 保留，补回归用例。"
    ),
    "livekit/agents#7445": (
        "`Agent.chat_ctx` 返回的 `_ReadOnlyChatContext` 有两条变更路径没守卫、静默写进视图的 detached 副本后正常返回："
        "`_ImmutableList` 覆盖了 append/extend/pop/remove/clear/sort/reverse 独漏 `insert`，`chat_ctx.insert(item)` 与"
        "走 `list.insert()` 的 `add_message(created_at=...)` / `merge(...)` 都把消息写丢，消息从没进真实 chat context；"
        "`items` property setter 也未覆盖，`chat_ctx.items = [...]` 把不可变列表换成可变列表而 `readonly` 仍报 True。"
        "改为补上 `insert` 的抛错实现并覆盖 `items` setter，两条路径都按文档抛 `RuntimeError`，补回归测试。"
    ),
    "strands-agents/harness-sdk#4593": (
        "Anthropic Messages API 的 `RedactedThinkingBlock.data` 是 base64 字符串，`AnthropicModel.stream` 却经"
        "编译期 cast 把它直接塞进声明为 `Uint8Array`、带 base64 `toJSON()/fromJSON()` 契约的 "
        "`ReasoningBlock.redactedContent`——首轮侥幸原样通过，首次 `Message.clone()` 或 session 存取经 "
        "`toJSON()/fromJSON()` 把它再编码成 base64 文本的 ASCII 字节，下一请求的 `redacted_thinking` 块序列化成 "
        "`{\"0\":69,\"1\":109,...}` 被 Messages API 拒收，加密推理的多轮工具使用全断。"
        "改为入库时把 base64 解码成字节存进 `redactedContent`、发送时再编码回字符串，往返与类型契约都对齐。"
    ),
    "PrefectHQ/fastmcp#5271": (
        "`TransformedTool.run` 只拿字面顶层 `\"type\": \"object\"` 键判定 `output_schema` 是不是 object schema——"
        "不带该键的 object schema（properties-only 的 `{\"properties\": {...}}`、根级 `$ref` 指向 object）被误判为"
        "非 object，`transform_fn` 返回的 `ToolResult` 的 `structured_content` 被丢弃，重建的 `ToolResult` 还把 "
        "`is_error` 与 `meta` 一并丢掉。改为按解析后的 schema 判定（properties-only 与根级 `$ref` 都算 object），"
        "透传 `structured_content` 并保留 `is_error`/`meta`，补回归测试。"
    ),
    "PrefectHQ/fastmcp#5575": (
        "`set_up_component_manager` 文档写明支持 `POST /tools/{name}/disable?version=v1`，路由处理器却把原始查询串"
        "直接交给 `Provider.enable`/`disable` 的 `VersionSpec` 参数，存下 `str` 后 `Visibility._matches` 调 "
        "`self.version.matches(...)` 抛 `AttributeError`：一次带 `?version=` 的请求返回 200，之后所有客户端的 "
        "`tools/list` 全部报错直到重启。改为把 `version` 查询参数转成 `VersionSpec(eq=version)` 再传入，"
        "无 `?version=` 路径保持 `None` 不变，补回归测试。"
    ),
    "PrefectHQ/fastmcp#5269": (
        "`functools.partial` 造的工具全叫 `partial`、描述是 partial 类 docstring——`ParsedFunction.from_function` 经 "
        "`fn.__class__.__name__` 兜底取名，partial 既无 `__name__` 也无 `__doc__`，注册两个 partial 工具就在名字 "
        "`partial` 上相撞、后者顶掉前者（只给一条泛型 warning）。改为取名/取 docstring 时回退到被包裹的 callable"
        "（保留 partial 绑定的参数与默认值）；partial 上显式给的名字、文档与参数描述仍优先（含故意留空的文档），"
        "FastMCP 显式元数据照样覆盖，补回归测试。"
    ),
    "bytedance/deer-flow#5861": (
        "`bind_task_tool` / `_bind_batch_tool` 给副本重绑的只有 `coroutine`，`func` 仍是进程级单例的 sync 包装——"
        "包着**未绑定**的 coroutine，同步调用 bound 副本因此绕过显式 SDK submitter 与执行容量、落回进程全局回退"
        "（恰是 `bind_batch_tools` docstring 明令禁止的「never fall through to another application's process-global "
        "submitter」），在单例从未被 sync 包装过的新进程里则直接 `NotImplementedError`。"
        "改为把副本的 `func` 也重绑成 `make_sync_tool_wrapper(bound_coroutine, ...)`（与 `_ensure_sync_invocable_tool` "
        "同一 helper），两条调用路径都走 bound coroutine 及其 runtime 的 submitter 与容量；补三条回归测试，"
        "main 上红、本分支绿。"
    ),
    "bytedance/deer-flow#5857": (
        "默认（非 policy-scoped）skills 投影下 `ls /mnt/skills` 报 Directory not found：该布局只挂四个 category "
        "子目录、没有 `/mnt/skills` 根自身的 `PathMapping`，`LocalSandbox.list_dir` 把根解析成字面宿主路径，"
        "宿主扫描的 `FileNotFoundError` 抢在虚拟子目录 overlay——专为让 agent 用 `ls /mnt/skills` 发现 category "
        "而写的代码块——之前抛出。改为宿主扫描抛 `FileNotFoundError` 时，只要请求的容器路径内至少挂了一个映射，"
        "就按空宿主列表处理、让既有 overlay 浮出挂载的子目录，什么都没挂的路径照旧报错；"
        "补回归测试，main 上红、本分支绿。"
    ),
    "openai/openai-agents-js#1935": (
        "`getAllMcpTools` 只拦**跨** server 的重名：`toFunctionToolName` 把非字母数字全替成 `_`，同一 server 里 "
        "`search-a` 与 `search_a` 归一后都叫 `search_a`，两个工具一起返回，`resolveModelVisibleToolNameCollisions` "
        "丢掉其中一个、模型只剩一个可达——守卫只拿当前 server 的名字与之前 server 已占的比较，还先把当前批次收进 "
        "`Set`，批内重复根本到不了比较；prefixed 路径按前缀后的 base name 计数，`-` 与 `_` 都算安全字符、"
        "base 不同就不强制 hash 后缀，归一后才相撞。改为 `findDuplicateToolNames` 同时报批内重复与先前 server 的"
        "占用（非前缀路径抛既有 `UserError`），前缀路径按归一后的名字计数预留、相撞时给同一确定性 hash 后缀，"
        "两个工具都保可达；补/扩回归测试，修前 2 败、修后 69 全过。"
    ),
    "agno-agi/agno#10554": (
        "`GeminiTools.generate_video` 把返回的 `Video` artifact 用 base64 **文本**构造"
        "（`base64.b64encode(generated_video.video_bytes).decode(\"utf-8\")`），而 `agno.media.Video.content` "
        "声明为原始视频 `bytes`，Pydantic 把该字符串强转成 base64 文本的 UTF-8 字节——`Video.get_content_bytes()` "
        "的每个消费者（媒体卸载上传、artifact 落盘）拿到的都是 base64 文本而不是视频。改为直接传原始字节，"
        "对齐同工具箱的 `generate_image` 分支与其余六个视频工具箱（opencv/fal/minimax/replicate/wavespeed/lumalab），"
        "补回归测试。"
    ),
    "bytedance/deer-flow#5591": (
        "Claude 凭据加载：`_extract_claude_code_credential` 把 `claudeAiOauth.expiresAt` 原样拷进 "
        "`ClaudeCodeCredential.expires_at`，`is_expired` 随即拿它和 `0` 比大小——字符串、`null`、list、object "
        "一律抛 `TypeError` 且无人捕获，凭据查找循环停在坏文件上不再推进，`$CLAUDE_CODE_CREDENTIALS_PATH` 里"
        "一个坏 `expiresAt` 就足以让 `~/.claude/.credentials.json` 永远读不到，还顺着 `ClaudeChatModel.model_post_init` "
        "冒出去使该文件存在时所有模型构造失败而非降级。改为非数值 `expiresAt` 的候选源按 #5494 已立的契约跳过并记 "
        "debug 日志（缺失键仍回落默认 `0`、不视为过期），补齐各形态回归测试。"
    ),
    "bytedance/deer-flow#5601": (
        "Codex 凭据加载：`account_id` 以 `data.get(\"account_id\") or tokens.get(\"account_id\", \"\")` 读取，"
        "`\"\"` 兜底只覆盖「键缺失」——键存在但值为 JSON `null` 时 falsy 落穿到下一环，表达式求值为 `None` 灌进 "
        "`CodexCliCredential(account_id=None)`，在 `model_post_init` 的 `account_id[:8]` 处抛裸 `TypeError`，"
        "account 未知的凭据文件让所有 `CodexChatModel` 构造失败而非以未记账账号运行。改为任何非字符串值一律归一为"
        "字段文档的未知账号值 `\"\"`，补回归测试。"
    ),
    "bytedance/deer-flow#5584": (
        "Codex 凭据加载：`load_codex_cli_credential` 经 `_load_json_file` 读 `~/.codex/auth.json`，"
        "而 `json.loads` 的产物不限于对象，加载器却直接对它调 `data.get(\"tokens\", {})`——"
        "顶层是数组/字符串/数字的 auth 文件因此抛 `AttributeError: 'list' object has no attribute 'get'`。"
        "异常无人捕获，从 `CodexChatModel.model_post_init` 冒出去，在 provider 来得及抛它那句文档化的"
        "「Codex CLI credential not found」之前就中止了模型构造，与该模块「读不到就降级」的约定正好相反。"
        "嵌套的 `tokens` 早已有这道守卫，同文件的 Claude 加载器也在 #5494 补了等价的顶层守卫，"
        "Codex 的顶层是唯一漏掉的一处。"
    ),
    "bytedance/deer-flow#5522": (
        "MCP 工具结果重写：`_rewrite_unique_bare_filenames` 把相关好的虚拟路径当成 `Pattern.subn` 的**替换模板**传入，"
        "而替换串来自真实文件的相对路径、反斜杠在 POSIX 文件名里是普通字符（模型给 stdio server 传了 Windows 风格路径就会"
        "产生名为 `screenshots\\q3.png` 的文件）。模板在找匹配**之前**编译，于是 `\\q` 这种未知转义直接抛 `re.error` 逃出 "
        "`_convert_call_tool_result`、整个工具调用失败（文件其实已写好）；能被 `re` 接受的转义则把该字节替换进返回文本"
        "（`\\r` 变成路径中间的真实回车）。改为用 callable 替换逐字插入，并补两半回归测试。"
        "文件来自 workspace 快照 diff，所以触发文件不必是本次调用写的。"
    ),
    "bytedance/deer-flow#5509": (
        "Codex Responses 序列化：模型发出 `arguments` 不是合法 JSON 的 `function_call` 时，该调用被 `_parse_response` 收进 "
        "`invalid_tool_calls`，中间件会用带同一 `call_id` 的占位 `ToolMessage` 就地兜住，但序列化器只回放 `msg.tool_calls`，"
        "于是占位结果的 `call_id` 在请求里找不到对应的 `function_call` item，Responses 直接拒收——恰好是中间件要恢复的那种可恢复错误。"
        "改为把 `invalid_tool_calls` 一并回放；同时处理 `InvalidToolCall` 字段可空，缺 name/call_id 的调用直接跳过"
        "（中间件已为这类调用补了合成 id 与兜底名，跳过不会让占位结果变孤儿）。"
    ),
    "agno-agi/agno#9948": (
        "同步工具执行路径把 `0` / `False` / `[]` 这类有意义的假值结果当成空结果发给模型，异步路径 `arun_function_calls` 却照发 "
        "`str(result)`，同一个工具在 `run()` 与 `arun()` 下给模型的结果不一致，模型无法区分“零条”和“没有输出”，空串还会被持久化进会话。"
        "去掉真值判断让两条路径一致，并补无网络回归测试。"
    ),
    "PrefectHQ/fastmcp#5117": (
        "MCP 本地 Provider：`LocalProvider.get_tasks()` 直接返回原始组件键，绕过了 Provider 基类的 transform 管线，"
        "于是 `add_transform(Namespace(...))` 之后后台任务注册到的名字与工具/资源不一致，按命名空间调用会找不到任务。"
        "改为在 `get_tasks` 里同样应用 transforms，并补回归测试。"
    ),
    "crewAIInc/crewAI#7487": (
        "Azure 流式补全：tool call 的增量按数组位置归并，但后续 chunk 会重排顺序，"
        "导致首个 chunk 的 `id` 配上最后一个 chunk 的 `name`、参数被拼到错误的调用上。"
        "改为按 wire index 归并，并补回归测试。"
    ),
    "bytedance/deer-flow#5426": (
        "HITL 澄清与 MCP 路由：Human Input Card 的回执被 `is_real_user_message` 当成“非真实用户消息”跳过，"
        "用户只在澄清回答里提到的关键词不会触发延迟 MCP 工具提升。改用同包已有的 `is_genuine_user_message` 谓词"
        "（与 summarization / tool_receipt 中间件一致），并补回归测试。"
    ),
    "bytedance/deer-flow#5164": (
        "MCP 工具调用：同步包装的 MCP 工具在 PEP 563 延迟注解下丢失 `ToolRuntime` 注入，工具拿不到会话上下文。"
        "修复后注入在两种注解模式下都生效，按 maintainer review 补了契约说明和测试。"
    ),
    "strands-agents/harness-sdk#4139": (
        "OpenAI Responses 流式解析：function call 被 `max_output_tokens` 截断时 `stop_reason` 仍报 `tool_use`，"
        "Agent 会拿残缺参数直接执行工具。修正判定优先级，截断时如实报 `max_tokens`，并补回归测试。"
    ),
    "agno-agi/agno#9887": (
        "Gemini 多模态输入：图片 MIME 类型被硬编码为 `image/jpeg`，PNG/WebP 等格式会被贴错标签导致 API 拒收或误解析。"
        "改为从图片数据实际解析类型后再传给模型。"
    ),
}

# 问题获修：自己发现、报告或提供补丁的问题，由上游修好，但不是以「我们的 PR 被合并」的方式纳入。
# 按独立问题计数，与合并 PR 不重复计入；每条都有已合并的修复 PR 或修复 commit 作证。
# 数据与核实过程见 docs/github-contribution-stats.md 第三、五节；新问题获修后在这里补一行。
# fixed_at：修复 PR 合并（多个取最晚）或修复 commit 的日期，详情列表与合并 PR 一起按它倒序；
# patch：我们提交过、被上游采纳的补丁 PR；fixed_by：(修复 PR 编号, 作者)；fixed_by_commit：(commit, 作者)。
ISSUES_FIXED = [
    {"repo": "Arize-ai/phoenix", "issue": 17398, "fixed_at": "2026-10-31", "fixed_by": [(17433, "pcbeingused333")],
     "title": "[BUG]: Span annotation DataFrame logging skips required-column validation that the document path enforces"},
    {"repo": "agentscope-ai/agentscope", "issue": 3291, "fixed_at": "2026-10-30", "fixed_by": [(3297, "SSK988I")],
     "title": "[Bug]: Read tool accepts offset <= 0, negative-slicing the file and returning its tail labeled with line numbers 0 or negative"},
    {"repo": "PrefectHQ/fastmcp", "issue": 6155, "fixed_at": "2026-10-29", "fixed_by": [(6156, "HootRock")],
     "title": "[Bug] A kept-alive stdio transport keeps the first client's session and silently ignores a second client's timeout"},
    {"repo": "PrefectHQ/fastmcp", "issue": 6117, "fixed_at": "2026-10-28", "fixed_by": [(6119, "KashifManzer")],
     "title": "[Bug] FastMCPStdioTransport silently drops its args parameter"},
    {"repo": "PrefectHQ/fastmcp", "issue": 5866, "fixed_at": "2026-10-27", "patch": 5867, "fixed_by": [(6100, "jlowin")],
     "title": "[Bug] FastMCPApp treats hash-shaped tool names as pre-addressed, breaking Prefab callbacks after composition"},
    {"repo": "openai/openai-agents-python", "issue": 5348, "fixed_at": "2026-10-26", "fixed_by": [(5423, "jbeckwith-oai")],
     "title": "ShellTool: empty ShellResult(output=[]) fabricates stdout \"(no output)\" in the model-visible shell_call_output and persisted shell_output"},
    {"repo": "bytedance/deer-flow", "issue": 7086, "fixed_at": "2026-10-24", "fixed_by": [(7092, "Hugo-DDT")],
     "title": "[Bug] DeerFlowClient(config_path=...) silently uses the default config, and explicit reloads can be discarded"},
    {"repo": "bytedance/deer-flow", "issue": 7077, "fixed_at": "2026-10-23", "fixed_by": [(7115, "gmll-star")],
     "title": "[Bug] POST /threads/{id}/state silently ignores the checkpoint object and mutates the thread head"},
    {"repo": "bytedance/deer-flow", "issue": 7072, "fixed_at": "2026-10-20", "fixed_by": [(7076, "LuckVd")],
     "title": "[Bug] Unreadable memory.json is silently overwritten instead of quarantined (data loss)"},
    {"repo": "PrefectHQ/fastmcp", "issue": 5816, "fixed_at": "2026-10-19", "fixed_by": [(5817, "HootRock")],
     "title": "[Bug] Shared() dependencies become request-scoped without pydocket, and direct call_tool crashes with pydocket"},
    {"repo": "bytedance/deer-flow", "issue": 5846, "fixed_at": "2026-10-18", "fixed_by": [(7020, "Totoro-qaq")],
     "title": "[bug] skill_manage: parallel tool calls for the same (user, skill) deadlock forever on the sync client path (shared asyncio.Lock across per-call event loops)"},
    {"repo": "mastra-ai/mastra", "issue": 26481, "fixed_at": "2026-10-16", "fixed_by": [(26662, "mastra-platform")],
     "title": "[BUG] MCP image/audio tool results emitted as spec-v3 `image-data`/`file-data` in the v5 tool-result output — dropped by spec-v2 providers, rejected by spec-v4 (Bedrock throws)"},
    {"repo": "Arize-ai/phoenix", "issue": 16950, "fixed_at": "2026-10-15", "fixed_by": [(16951, "lx3133584")],
     "title": "[BUG]: [playground] AWS Bedrock run crashes with JSONDecodeError when a tool result message contains plain text"},
    {"repo": "Fei2411/DS-Bot", "issue": 58, "fixed_at": "2026-10-12", "fixed_by_commit": ("d9af38d", "Fei2411"),
     "title": "Node 22 下 web-search 慢端点超时永不触发（`AbortSignal.timeout` 的 unref 定时器）"},
    {"repo": "Fei2411/DS-Bot", "issue": 57, "fixed_at": "2026-10-12", "fixed_by_commit": ("2ceba39", "Fei2411"),
     "title": "删除 Bot / 群聊后其定时任务成为孤儿：仍在 DSH 中待命，设置页不可见也无法删除"},
    {"repo": "Fei2411/DS-Bot", "issue": 56, "fixed_at": "2026-10-12", "fixed_by_commit": ("7018a8b", "Fei2411"),
     "title": "`state.lock` 被另一台 host 接管后，写端点仍返回 ok:true 但 `save()` 静默失败"},
    {"repo": "Fei2411/DS-Bot", "issue": 55, "fixed_at": "2026-10-12", "fixed_by_commit": ("d9af38d", "Fei2411"),
     "title": "dev/mock-llm.mjs 的 `长任务 N` 省略 K 时每一步都不产出文本块（`.map(Number)` 把缺失的 K 变成 NaN）"},
    {"repo": "bytedance/deer-flow", "issue": 6471, "fixed_at": "2026-10-08", "fixed_by": [(6477, "yu1128-L")],
     "title": "[bug] DbRunEventStore: delete_by_run lowers the thread's max-seq watermark, so later puts reissue already-used seq values and become invisible to after_seq cursors"},
    {"repo": "PrefectHQ/fastmcp", "issue": 5265, "fixed_at": "2026-10-05", "fixed_by": [(5270, "lzyruc")],
     "title": "CallToolResult.data is None when output_schema has uniqueItems on an array of objects"},
    {"repo": "modelcontextprotocol/servers", "issue": 4827, "fixed_at": "2026-10-05", "patch": 4828, "fixed_by": [(5013, "cliffhall")],
     "title": "server-memory: saveGraph rewrites memory.jsonl via temp-file + rename, dropping an existing file's permission bits (0600 -> 0644) and silently overwriting read-only files"},
    {"repo": "modelcontextprotocol/servers", "issue": 4813, "fixed_at": "2026-10-05", "patch": 4814, "fixed_by": [(5036, "cliffhall")],
     "title": "sequentialthinking: a branchId that collides with an Object.prototype key throws instead of creating the branch, and the failed call still extends thoughtHistory"},
    {"repo": "modelcontextprotocol/servers", "issue": 4808, "fixed_at": "2026-10-05", "fixed_by": [(5032, "cliffhall")],
     "title": "everything: session resources evict another session's resource when two sessions use the same file name"},
    {"repo": "e2b-dev/E2B", "issue": 1895, "fixed_at": "2026-10-01", "fixed_by": [(1912, "harshitgavita-07"), (1923, "devin-ai-integration")],
     "title": "[Bug]: JS SDK: filesystem watch handle.stop() always fires onExit with a TimeoutError blaming 'requestTimeoutMs'"},
    {"repo": "mastra-ai/mastra", "issue": 25208, "fixed_at": "2026-09-28", "fixed_by": [(25278, "mastra-platform")],
     "title": "[BUG] Array structured output textStream/elementStream keep the stale partial element when a later chunk completes it in place"},
    {"repo": "mastra-ai/mastra", "issue": 24516, "fixed_at": "2026-09-25", "fixed_by": [(25086, "breken-ai")],
     "title": "[BUG] schema-compat/zodToJsonSchema: nullable zod v4 enum/literal widens to type:[X,\"null\"] but keeps enum/const, so exported schema rejects null"},
    {"repo": "Arize-ai/phoenix", "issue": 16228, "fixed_at": "2026-09-25", "fixed_by": [(16316, "Anurag-M1")],
     "title": "[BUG]: Anthropic prompt adapter ignores `{{ variables }}` in str system messages, sending the literal template as the `system` kwarg"},
    {"repo": "openai/openai-agents-js", "issue": 1976, "fixed_at": "2026-09-24", "fixed_by": [(1977, "jbeckwith-oai")],
     "title": "MCP tool cache: invalidating server 'X' deletes the cached tools of an unrelated server named 'X:suffix' via the unscoped prefix-scan fallback"},
    {"repo": "agentscope-ai/agentscope", "issue": 2709, "fixed_at": "2026-09-21", "fixed_by": [(2726, "DavdGao")],
     "title": "[Bug]: Grep: offset/head_limit pagination silently drops and duplicates matches because ripgrep output order is non-deterministic across invocations"},
    {"repo": "livekit/agents", "issue": 7324, "fixed_at": "2026-09-18", "fixed_by": [(7330, "longcw")],
     "title": "ChatContext.copy(tools=...) drops FunctionCallOutput with a default (empty) name, silently removing the whole function call + result pair from provider requests"},
    {"repo": "bytedance/deer-flow", "issue": 5473, "fixed_at": "2026-09-17", "fixed_by": [(5494, "cyberspace-cs")],
     "title": "[bug] Claude credential loader raises AttributeError when ~/.claude/.credentials.json has a non-object claudeAiOauth container"},
    {"repo": "mastra-ai/mastra", "issue": 23980, "fixed_at": "2026-09-15", "fixed_by": [(24055, "DanielSLew")],
     "title": "[BUG] Top-level array structured output silently returns [] for arrays of primitives"},
    {"repo": "agentscope-ai/agentscope", "issue": 2494, "fixed_at": "2026-09-15", "fixed_by": [(2495, "RICARDO51167")],
     "title": "[Bug]: AnthropicChatModel streaming merges all `thinking` blocks of one response into a single block, keeping only the last `signature`"},
    {"repo": "bytedance/deer-flow", "issue": 5192, "fixed_at": "2026-09-05", "fixed_by": [(5195, "Coder-xiaosuo")],
     "title": "[bug] MindIE tool-enabled async streaming drops token usage"},
]

QUERY = """
{
  search(query: "author:%s is:pr is:merged -user:%s", type: ISSUE, first: 50) {
    nodes {
      ... on PullRequest {
        repository { nameWithOwner url stargazerCount }
        number title url mergedAt
      }
    }
  }
}
""" % (USER, USER)


REPO_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    nameWithOwner url stargazerCount
  }
}
"""


def graphql(query, variables=None):
    payload = {"query": query}
    if variables:
        payload["variables"] = variables
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps(payload).encode(),
        headers={
            "Authorization": "bearer " + os.environ["GITHUB_TOKEN"],
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    if "errors" in data:
        raise RuntimeError("GraphQL errors: %s" % data["errors"])
    return data["data"]


def fetch_once():
    return [n for n in graphql(QUERY)["search"]["nodes"] if n]


def fetch_repo(full):
    """只有问题获修、没有已合并 PR 的仓库不在 search 结果里，单独取头像墙需要的信息。"""
    owner, name = full.split("/", 1)
    return graphql(REPO_QUERY, {"owner": owner, "name": name})["repository"]


def fetch(attempts=4):
    """GitHub 的 search 索引是最终一致的：同一条查询连着跑会返回不同的子集
    （实测 4 条 → 2 条 → 1 条）。多打几次、取条数最多的那次，别拿残缺结果去覆盖。"""
    best = []
    for i in range(attempts):
        try:
            got = fetch_once()
        except Exception as exc:
            print("fetch attempt %d/%d failed: %s" % (i + 1, attempts, exc), file=sys.stderr)
            continue
        if len(got) > len(best):
            best = got
        if len(got) == len(best) and len(best) >= 50:
            break
    if not best:
        raise SystemExit("search 连续 %d 次都没返回结果，拒绝覆盖" % attempts)
    return best


def fmt_stars(n):
    # 粗粒度，避免 star 数微小波动导致每次运行都产生提交
    return f"{n / 1000:.0f}k" if n >= 1000 else str(n)


def avatar(owner, size):
    # github.com/<owner>.png 会 302 到头像 CDN，GitHub 的 camo 图片代理能跟随
    return f"https://github.com/{owner}.png?size={size}"


def wall_order(repos):
    """repos: {owner/repo: [repository, 合并数, 问题获修数]}；按 star 数降序排。"""
    return sorted(repos.values(), key=lambda e: (-e[0]["stargazerCount"], e[0]["nameWithOwner"].lower()))


def render_wall(ordered):
    per_row = math.ceil(len(ordered) / math.ceil(len(ordered) / WALL_PER_ROW))
    rows = []
    for i in range(0, len(ordered), per_row):
        cells = []
        for repo, merged, fixed in ordered[i:i + per_row]:
            owner, name = repo["nameWithOwner"].split("/", 1)
            url, stars = repo["url"], fmt_stars(repo["stargazerCount"])
            bits = []
            if merged:
                bits.append(f"代码合并&nbsp;<b>{merged}</b>")
            if fixed:
                bits.append(f"问题获修&nbsp;<b>{fixed}</b>")
            # 头像单独一行：浏览器总能在行内图片后折行，和名字放一行时长名字会把头像挤上去。
            # 名字一行用 &nbsp; 与不换行连字符（U+2011），不会被挤折；单元格给百分比宽度表格才占满整行
            # （GitHub 会剥掉 style，table 自身的 width 也不生效），名字长的列会自动分得宽一些。
            cells.append(
                f'<td align="center" width="{100 // per_row}%"><a href="{url}"><img src="{avatar(owner, 48)}" '
                f'width="24" height="24" alt="{owner}"/><br/><b>{name.replace("-", "‑")}</b></a>&nbsp;·&nbsp;⭐{stars}'
                f'<br/><sub>{"&nbsp;·&nbsp;".join(bits)}</sub></td>'
            )
        rows.append("<tr>\n" + "\n".join(cells) + "\n</tr>")
    # 一张表、多行，各列上下对齐
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def summary_title(text):
    # <summary> 里不解析 markdown，标题只能写成 HTML；反引号照旧渲染成代码
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", html.escape(text, quote=False))


def entry_head(date, full, url, title):
    owner, name = full.split("/", 1)
    # 日期放行首：放行尾时长标题会把它从连字符处折断（GitHub 会剥掉 style，没法 nowrap）
    return (f'<code>{date}</code> <img src="{avatar(owner, 40)}" width="16" height="16" alt="{owner}"/> '
            f'<b>{name}</b> · <a href="{url}">{summary_title(title)}</a>')


def render_entry(p):
    full, url = p["repository"]["nameWithOwner"], p["url"]
    # 页面上只露标题链接；PR_LINK 要的 markdown 形式链接放进注释，pr-tracker 与条数检查照样认得
    return f"<p>{entry_head(p['mergedAt'][:10], full, url, p['title'])}</p>\n<!-- ({url}) -->"


def render_fixed_entry(item):
    # 标题直接链到 issue
    url = f"https://github.com/{item['repo']}/issues/{item['issue']}"
    return f"<p>{entry_head(item['fixed_at'], item['repo'], url, item['title'])}</p>"


def render(prs):
    if not prs:
        return "_暂无_"
    repos = {}
    for p in prs:
        repos.setdefault(p["repository"]["nameWithOwner"], [p["repository"], 0, 0])[1] += 1
    for item in ISSUES_FIXED:
        full = item["repo"]
        if full not in repos:
            repos[full] = [fetch_repo(full), 0, 0]
        repos[full][2] += 1
    summary = (
        f'<p align="center">代码合并 <b>{len(prs)}</b> · 问题获修 <b>{len(ISSUES_FIXED)}</b>'
        f" · 覆盖 <b>{len(repos)}</b> 个上游仓库</p>"
    )
    # 两类贡献合成一个列表，按合并／修复日期倒序；同一天里合并 PR 按时间戳排、排在获修问题前面
    entries = [((p["mergedAt"][:10], 1, p["mergedAt"]), render_entry(p)) for p in prs]
    entries += [((it["fixed_at"], 0, f'{it["repo"].lower()}#{it["issue"]:08d}'),
                 render_fixed_entry(it)) for it in ISSUES_FIXED]
    entries = [e for _, e in sorted(entries, key=lambda e: e[0], reverse=True)]
    detail = "\n\n".join(
        ["<details>", "<summary><b>全部贡献</b>：代码合并：本人 PR 获合并 · 问题获修：本人报告或补丁获修复，"
         "未合并本人 PR · 成果不重复计数</summary>", "<br/>"]
        + entries + ["</details>"]
    )
    return "\n\n".join([render_wall(wall_order(repos)), summary, detail])


def count_entries(section):
    return len(set(PR_LINK.findall(section)))


def bug_rows(text):
    """缺陷表的数据行（按 `|` 切好的单元格），解析口径与 pr-tracker 的 homepage_sync.py 一致：
    `## 🔍` 到下一个 `## ` 之间、以 `| [` 开头且含 github.com 的行。"""
    rows, zone = [], False
    for line in text.splitlines():
        if line.startswith("## 🔍"):
            zone = True
        elif zone and line.startswith("## "):
            break
        elif zone and line.startswith("| [") and "github.com" in line:
            cells = [c.strip() for c in re.split(r"(?<!\\)\|", line)]
            if len(cells) >= 5:
                rows.append(cells)
    return rows


def bug_kind(status):
    # 状态列开头的色点见 pr-tracker SKILL.md 的用词约定：🟢 有修复，🟡 在等，⚪ 已关闭
    if status.startswith("🟢"):
        return "fixed" if "已合并" in status or "已被上游修复" in status else "submitted"
    if status.startswith("⚪"):
        return "closed"
    return "waiting"


def render_bug_stats(rows):
    kinds = Counter(bug_kind(cells[3]) for cells in rows)
    repos = set()
    for cells in rows:
        m = re.search(r"\(https://github\.com/([^)]+)\)", cells[1])
        repos.add((m.group(1) if m else cells[1]).lower())
    stats = [
        ("🐛", "发现缺陷", len(rows)),
        ("📦", "涉及仓库", len(repos)),
        ("✅", "已修复", kinds["fixed"]),
        ("🔧", "修复已提交", kinds["submitted"]),
        ("⏳", "等待中", kinds["waiting"]),
        ("⚪", "已关闭", kinds["closed"]),
    ]
    # 一行数字条，比 6 列表格矮一半，手机上也不会横向滚动
    return '<p align="center">' + " &nbsp;·&nbsp; ".join(
        f"{icon} <b>{n}</b> {label}" for icon, label, n in stats
    ) + "</p>"


def replace_block(text, start, end, body):
    # 用 callable 替换：body 里有反斜杠（说明文字里引用的文件名）时，
    # 字符串模板会被 re 当成转义序列解析，`\q` 这种直接抛 re.error。
    return re.sub(
        re.escape(start) + r".*?" + re.escape(end),
        lambda _m: f"{start}\n{body}\n{end}",
        text,
        flags=re.S,
    )


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        raise SystemExit("README 缺少 contributions 标记")
    span = re.search(re.escape(START) + r"(.*?)" + re.escape(END), text, flags=re.S)
    old_count = count_entries(span.group(1))
    body = render(fetch())
    # 这个区块是整段替换的：抓到一半就等于把真实存在的已合并 PR 从主页删掉。
    # 宁可本次不更新、让 CI 失败得看得见，也不要静默缩水。
    new_count = count_entries(body)
    if new_count < old_count:
        raise SystemExit(
            "拒绝写入：本次抓到 %d 条，现有区块有 %d 条。"
            "多半是 GitHub search 返回了不完整结果，重跑即可。" % (new_count, old_count)
        )
    new = replace_block(text, START, END, body)
    if BUG_START in new and BUG_END in new:
        new = replace_block(new, BUG_START, BUG_END, render_bug_stats(bug_rows(new)))
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
