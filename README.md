<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:8E2DE2,100:4A00E0&height=200&section=header&text=BlueX888&fontSize=60&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=Multi-Agent%20Systems%20Builder&descSize=20&descAlignY=55" width="100%"/>

<h1>👨‍💻 Hey there! 👋 I'm 哈基米</h1>

<a href="https://github.com/BlueX888">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&duration=2500&pause=900&color=A78BFA&center=true&vCenter=true&width=650&lines=%F0%9F%A4%96+Building+Multi-Agent+Systems;%F0%9F%A7%AA+From+1000-line+demos+to+durable+kernels;%F0%9F%9A%80+Talk+is+cheap%2C+show+me+the+Agent!" alt="Typing SVG" />
</a>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="900">

<p>
  <a href="https://github.com/BlueX888?tab=repositories&sort=stargazers">
    <img alt="total stars" src="https://custom-icon-badges.demolab.com/github/stars/BlueX888?color=55960c&style=for-the-badge&labelColor=488207&logo=star"/></a>
  <a href="https://github.com/BlueX888?tab=followers">
    <img alt="followers" src="https://custom-icon-badges.demolab.com/github/followers/BlueX888?color=236ad3&labelColor=1155ba&style=for-the-badge&logo=person-add&label=Follow&logoColor=white"/></a>
  <img alt="profile views" src="https://komarev.com/ghpvc/?username=BlueX888&label=Profile%20Views&color=8E2DE2&style=for-the-badge"/>
</p>

<p>
  <img alt="Intern at ModelBest" src="https://img.shields.io/badge/💼_面壁智能_%2F_OpenBMB-Agent_方向实习中-4A00E0?style=flat-square"/>
  <img alt="BJUT" src="https://img.shields.io/badge/🎓_北京工业大学-研二在读-8E2DE2?style=flat-square"/>
  <img alt="Focus" src="https://img.shields.io/badge/🧪_方向-LLM_Agent_编排_%2F_持久化执行_%2F_多智能体安全-A78BFA?style=flat-square"/>
</p>

</div>

## 🎯 About Me

<table border="0">
<tr>
<td width="62%" valign="top">

我做多智能体系统。从 174 行就能读完的 deep-research 团队，到跑在 Temporal 上、有租户隔离和审计的企业级执行内核，我想搞清楚同一件事：**让一群模型可靠地协作，到底需要什么样的工程。**

**我信什么？** 模型负责判断，代码负责搬运。安全边界、状态机、可审计性这些东西应该由确定性代码兜底，而不是寄希望于 prompt。

<table>
  <tr><td>🎓 <b>研究生</b></td><td>北京工业大学（211）· 计算机科学与技术 · 2025.09 – 2028.06</td></tr>
  <tr><td>🎓 <b>本科</b></td><td>河南大学（双一流）· 计算机科学与技术 · 2021.09 – 2025.06</td></tr>
  <tr><td>💼 <b>实习</b></td><td>面壁智能（ModelBest / OpenBMB）· Agent 方向 · 2026.08 至今</td></tr>
  <tr><td>🧪 <b>方向</b></td><td>LLM Agent 编排 · 持久化执行 · 多智能体安全治理</td></tr>
</table>

</td>
<td width="38%" align="center" valign="middle">

<img src="https://user-images.githubusercontent.com/74038190/229223263-cf2e4b07-2615-4f87-9c38-e37600f8381a.gif" width="100%" alt="coding"/>

</td>
</tr>
</table>

---

## 🔬 Current Work

- ⚙️ **SwarmCore** 正在冲 M5 里程碑（v1 候选基线）：Temporal 持久化编排 + PostgreSQL 单一事实源 + OPA/Vault 治理
- 💼 在面壁智能实习，参与 OpenBMB 的 Agent 产品（ChatDev / StaffDeck / PilotDeck）开发
- 🔧 给上游 Agent 框架修 bug、提特性：Strands Agents、Agno、deer-flow、Hugging Face smolagents、OpenHands、crewAI、CAMEL、LangGraph / DeepAgents、mem0、RAGAS、DeepEval、FastMCP、mcp-use、MCP Servers、OpenAI Agents SDK（Python / TS）、Mastra
- 🔍 审 Agent 框架的核心模块（provider 适配层、streaming 聚合、tool 调用）主动找缺陷：写无网络最小复现 → 按仓库模板报 issue → 允许直接 PR 的仓库当天带回归测试提修复，issue-first 的仓库等维护者确认后再修
- 📖 维护 **nanoteam**，把多智能体的最小可用形态写成一本能跑的教科书

---

## 📘 Projects

> 一条完整的多智能体谱系：**看得懂 → 用得上 → 跑得稳**

<table>
<tr>
<td width="50%" valign="top">

### 🐜 [nanoteam](https://github.com/BlueX888/nanoteam)

1000 行以内的 deep-research 多智能体团队，一天就能读完的"可运行教科书"。Leader–Worker 架构，可预测的 N+2 次模型调用，CI 强制行数上限。

<img src="https://img.shields.io/badge/-Leader–Worker-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/-CI_行数上限-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/-单一依赖-1C3C3C?style=flat-square"/>

</td>
<td width="50%" valign="top">

### 🔨 [forge-code](https://github.com/BlueX888/forge-code)

面向本地工程的个人 AI 编程助手。跨会话项目记忆，Skill 自进化（人工审核后沉淀），长任务上下文压缩，本地权限沙箱。

<img src="https://img.shields.io/badge/-项目记忆-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/-Skill_自进化-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/-权限沙箱-1C3C3C?style=flat-square"/>

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🏥 [Medical-Agent-Swarm](https://github.com/BlueX888/Medical-Agent-Swarm)

基于 LangGraph 的医疗问答多智能体原型。Orchestrator–Worker 编排，确定性安全层由代码而非 LLM 兜底，技能白名单 + 隐私脱敏 API。

<img src="https://img.shields.io/badge/-LangGraph-1C3C3C?style=flat-square&logo=langchain&logoColor=white"/> <img src="https://img.shields.io/badge/-确定性安全层-1C3C3C?style=flat-square"/> <img src="https://img.shields.io/badge/-隐私脱敏-1C3C3C?style=flat-square"/>

</td>
<td width="50%" valign="top">

### ⚙️ [SwarmCore](https://github.com/BlueX888/SwarmCore)

企业级多租户、可持久化的智能体执行内核。Temporal 持久化编排，不可变执行计划，PostgreSQL 单一事实源，OPA/Vault 安全治理。

<img src="https://img.shields.io/badge/-Temporal-1C3C3C?style=flat-square&logo=temporal&logoColor=white"/> <img src="https://img.shields.io/badge/-PostgreSQL-1C3C3C?style=flat-square&logo=postgresql&logoColor=white"/> <img src="https://img.shields.io/badge/-OPA_%2F_Vault-1C3C3C?style=flat-square"/>

</td>
</tr>
</table>

---

## 🤝 Merged Upstream PRs

<!--START_SECTION:contributions-->
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k — [fix(models): degrade a non-object Codex auth file to no credential](https://github.com/bytedance/deer-flow/pull/5584) `2026-09-19`
  - Codex 凭据加载：`load_codex_cli_credential` 经 `_load_json_file` 读 `~/.codex/auth.json`，而 `json.loads` 的产物不限于对象，加载器却直接对它调 `data.get("tokens", {})`——顶层是数组/字符串/数字的 auth 文件因此抛 `AttributeError: 'list' object has no attribute 'get'`。异常无人捕获，从 `CodexChatModel.model_post_init` 冒出去，在 provider 来得及抛它那句文档化的「Codex CLI credential not found」之前就中止了模型构造，与该模块「读不到就降级」的约定正好相反。嵌套的 `tokens` 早已有这道守卫，同文件的 Claude 加载器也在 #5494 补了等价的顶层守卫，Codex 的顶层是唯一漏掉的一处。
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k — [fix(mcp): insert bare-filename rewrites literally](https://github.com/bytedance/deer-flow/pull/5522) `2026-09-18`
  - MCP 工具结果重写：`_rewrite_unique_bare_filenames` 把相关好的虚拟路径当成 `Pattern.subn` 的**替换模板**传入，而替换串来自真实文件的相对路径、反斜杠在 POSIX 文件名里是普通字符（模型给 stdio server 传了 Windows 风格路径就会产生名为 `screenshots\q3.png` 的文件）。模板在找匹配**之前**编译，于是 `\q` 这种未知转义直接抛 `re.error` 逃出 `_convert_call_tool_result`、整个工具调用失败（文件其实已写好）；能被 `re` 接受的转义则把该字节替换进返回文本（`\r` 变成路径中间的真实回车）。改为用 callable 替换逐字插入，并补两半回归测试。文件来自 workspace 快照 diff，所以触发文件不必是本次调用写的。
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k — [fix(models): pair Codex invalid tool calls with their tool results](https://github.com/bytedance/deer-flow/pull/5509) `2026-09-17`
  - Codex Responses 序列化：模型发出 `arguments` 不是合法 JSON 的 `function_call` 时，该调用被 `_parse_response` 收进 `invalid_tool_calls`，中间件会用带同一 `call_id` 的占位 `ToolMessage` 就地兜住，但序列化器只回放 `msg.tool_calls`，于是占位结果的 `call_id` 在请求里找不到对应的 `function_call` item，Responses 直接拒收——恰好是中间件要恢复的那种可恢复错误。改为把 `invalid_tool_calls` 一并回放；同时处理 `InvalidToolCall` 字段可空，缺 name/call_id 的调用直接跳过（中间件已为这类调用补了合成 id 与兜底名，跳过不会让占位结果变孤儿）。
- [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k — [[fix] keep falsy tool results (0, False, []) on the sync tool execution path](https://github.com/agno-agi/agno/pull/9948) `2026-09-16`
  - 同步工具执行路径把 `0` / `False` / `[]` 这类有意义的假值结果当成空结果发给模型，异步路径 `arun_function_calls` 却照发 `str(result)`，同一个工具在 `run()` 与 `arun()` 下给模型的结果不一致，模型无法区分“零条”和“没有输出”，空串还会被持久化进会话。去掉真值判断让两条路径一致，并补无网络回归测试。
- [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) ⭐28k — [fix(local-provider): apply transforms in get_tasks](https://github.com/PrefectHQ/fastmcp/pull/5117) `2026-09-15`
  - MCP 本地 Provider：`LocalProvider.get_tasks()` 直接返回原始组件键，绕过了 Provider 基类的 transform 管线，于是 `add_transform(Namespace(...))` 之后后台任务注册到的名字与工具/资源不一致，按命名空间调用会找不到任务。改为在 `get_tasks` 里同样应用 transforms，并补回归测试。
- [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k — [fix(azure): key streamed tool calls by wire index](https://github.com/crewAIInc/crewAI/pull/7487) `2026-09-15`
  - Azure 流式补全：tool call 的增量按数组位置归并，但后续 chunk 会重排顺序，导致首个 chunk 的 `id` 配上最后一个 chunk 的 `name`、参数被拼到错误的调用上。改为按 wire index 归并，并补回归测试。
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k — [fix(mcp): treat a Human Input Card reply as the current user request](https://github.com/bytedance/deer-flow/pull/5426) `2026-09-14`
  - HITL 澄清与 MCP 路由：Human Input Card 的回执被 `is_real_user_message` 当成“非真实用户消息”跳过，用户只在澄清回答里提到的关键词不会触发延迟 MCP 工具提升。改用同包已有的 `is_genuine_user_message` 谓词（与 summarization / tool_receipt 中间件一致），并补回归测试。
- [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k — [fix(mcp): keep ToolRuntime injection for sync-wrapped MCP tools](https://github.com/bytedance/deer-flow/pull/5164) `2026-09-04`
  - MCP 工具调用：同步包装的 MCP 工具在 PEP 563 延迟注解下丢失 `ToolRuntime` 注入，工具拿不到会话上下文。修复后注入在两种注解模式下都生效，按 maintainer review 补了契约说明和测试。
- [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k — [fix(openai): report max_tokens when a Responses function call is cut off](https://github.com/strands-agents/harness-sdk/pull/4139) `2026-09-03`
  - OpenAI Responses 流式解析：function call 被 `max_output_tokens` 截断时 `stop_reason` 仍报 `tool_use`，Agent 会拿残缺参数直接执行工具。修正判定优先级，截断时如实报 `max_tokens`，并补回归测试。
- [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k — [[fix] Resolve Gemini image MIME type instead of hard-coding image/jpeg](https://github.com/agno-agi/agno/pull/9887) `2026-09-02`
  - Gemini 多模态输入：图片 MIME 类型被硬编码为 `image/jpeg`，PNG/WebP 等格式会被贴错标签导致 API 拒收或误解析。改为从图片数据实际解析类型后再传给模型。
<!--END_SECTION:contributions-->

## 🔍 Upstream Bugs Found

自己审代码发现、带无网络最小复现报出的缺陷。维护者那边已有讨论的按 issue 报，能直接修的当天带回归测试提 PR；有些仓库不必先开 issue，缺陷的复现与根因就写在 PR 描述里，这类条目的「问题」列直接指向 PR。下表按发现时间倒序，合并后会自动进上一栏：

| 仓库 | 问题 | 状态 |
|:--|:--|:--|
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k | [`load_codex_cli_credential` 读 `account_id` 用 `data.get("account_id") or tokens.get("account_id", "")`，`""` 兜底只覆盖「键缺失」——键存在但值为 JSON `null` 时 falsy 落穿到下一环，表达式求值为 `None` 灌进 `CodexCliCredential(account_id=None)`，而同文件对缺失键早已断言 `== ""`。`None` 穿过加载器，在 `model_post_init` 的 `account_id[:8]` 处抛裸 `TypeError: 'NoneType' object is not subscriptable`，account 未知的凭据文件让所有 `CodexChatModel` 构造失败而非以未记账账号运行](https://github.com/bytedance/deer-flow/pull/5601) `2026-09-20` | 🟢 直接提 PR（未建 issue），已合并 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`DeepEvalAgent.__post_init__` 只调 `patch_default_agent_runner_get_model()`、从不调 `super().__post_init__()`——dataclass 的 `__post_init__` 完全顶掉基类，基类的归一化整段不跑：非 GPT-5 模型也沿用 GPT-5 默认的 `reasoning`/verbosity 模型设置，dict 型 `model_settings` 永不被 `_coerce_model_settings` 归一](https://github.com/confident-ai/deepeval/pull/3323) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`@observe` 异步生成器分支的 `__anext__` 把 yield 值直接还给调用方、从不落存，`Observer.result` 恒为 `None`；耗尽时 `_finish()` 触发的 `__exit__` 只在 result 已设时才填 `current_span.output`——每个被完整消费的 `async for` 落库的 span/trace output 都是 `None`，而同步生成器分支（`last_yielded_value` 赋给 `observer.result`）早已正确，同一装饰器的两条分支相悖](https://github.com/confident-ai/deepeval/pull/3324) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`update_trace_properties_from_span_data` 对 `ResponseSpanData` 无条件解引用 `span_data.response`（读 `.instructions` / `.output`），而 Agents SDK 只在 `trace_include_sensitive_data=True` 时才填充该属性——`RunConfig(trace_include_sensitive_data=False)` 下每个 `ResponseSpanData` 都带着 `response=None` 进 trace processor，直接 `AttributeError`](https://github.com/confident-ai/deepeval/pull/3326) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [外部 HTTPS URL 路径的 `MCPToolWrapper._execute_tool` 无条件返回响应文本、从不检查 MCP server 在成功 `tools/call` 响应上设置的 `isError` 标志——错误文本以裸 `str` 进框架，调用被记成成功：不触发 `ToolFailureDetectedEvent`、`ToolOutput.has_tool_failures` 恒 false；`MCPNativeTool` 对同一 server 回答早已返回 `ToolFailure(reason=MCP_ERROR)`](https://github.com/crewAIInc/crewAI/pull/7643) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) ⭐52k | [`ReActAgent.finalize` 无条件剥掉最终响应里首个 `'Answer:'` 及之前的全部内容，默认该文本来自 `ReActOutputParser` 解析的 LLM 回合；但 `return_direct` 路径的最终响应由 `aggregate_tool_results` 直接取自工具输出——`return_direct` 工具的输出里含 `'Answer:'`（如 `Sources:\n  doc-1: pricing faq\nAnswer: 42 dollars per seat`）就被静默截成残句才交给调用方](https://github.com/run-llama/llama_index/pull/23147) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [`TextMessageChunkEvent` 是 AG-UI「代替 start+content+end 三连」的续写简写：`role` 只在开 chunk 上有值、`message_id` 缺省表示续上已打开的消息，而 `_handle_text_message_chunk` 把每个 chunk 当完整自足的消息——`getattr(event, "role", "assistant")` 的默认值永不上场（字段存在、续写 chunk 上是 `None`），首个 chunk 之后的全部落进 unexpected-role 分支被丢弃，流式回答被截断成第一段](https://github.com/vibrantlabsai/ragas/pull/3023) `2026-09-20` | 🟢 直接提 PR（未建 issue） |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k | [`_extract_claude_code_credential` 把 `claudeAiOauth.expiresAt` 原样拷进 `ClaudeCodeCredential.expires_at` 不做类型检查，`is_expired` 随即拿它和 `0` 比大小：字符串形式的 `"1773430695128"`、`null`、list、object 一律抛 `TypeError: '<=' not supported between instances of 'str' and 'int'`。异常无人捕获，凭据查找循环不会推进到下一个候选源——`$CLAUDE_CODE_CREDENTIALS_PATH` 里一个坏文件就足以让 `~/.claude/.credentials.json` 永远读不到；它还顺着 `ClaudeChatModel.model_post_init` 冒出去，使该文件存在时所有模型构造都失败而非降级。而「缺 `expiresAt`」本会回落到默认 `0` 并被 `is_expired` 明确容忍，显式 `null` 同属「过期时间未知」却中止加载](https://github.com/bytedance/deer-flow/issues/5589) `2026-09-19` | 🟢 修复 [#5591](https://github.com/bytedance/deer-flow/pull/5591) 已合并 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [工具参数 schema 用 `inspect.Parameter.annotation` 的原始值喂 `pydantic.create_model`，而 `from __future__ import annotations`（PEP 563）下它是纯字符串，pydantic 会拿**调用方**的命名空间去解析这个 `ForwardRef`（`base_tool.py`），调用方的名字在那里并不存在。这类模块里定义的工具能构造成功却永远调不动：首次调用抛 `ValueError: Tool 'wallet' arguments validation failed: `Wallet` is not fully defined`，把工具渲染进 prompt 也抛同义的 `PydanticUserError`。不限于用户自定义模型，`Optional[str]`、`Literal["a","b"]`、`pathlib.Path` 一样中招，`main` 上有六处 schema 构建点都读原始注解](https://github.com/crewAIInc/crewAI/issues/7623) `2026-09-19` | 🟢 修复 [#7626](https://github.com/crewAIInc/crewAI/pull/7626) 已提交 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [memory server 的 `KnowledgeGraphManager.saveGraph()` 先写临时文件再 `rename` 覆盖 `memory.jsonl`，而 `rename(2)` 用临时文件的 inode 顶掉目标 inode，临时文件按进程 umask 建立，运维给记忆文件设的权限位就此丢失、下次变更后回到 `0644`。`saveGraph` 是所有变更（`create_entities`、`add_observations`、`delete_*`）的落盘路径，每一次写都会放松权限。这是 #4642 引入的回归（此前直接 `writeFile` 会保留已有文件的 mode）；仓库里 `src/filesystem/lib.ts` 对同一套「临时文件 + rename」早已在 rename 后还原 `origStats.mode & 0o777`（#4115 已合并）](https://github.com/modelcontextprotocol/servers/issues/4827) `2026-09-19` | 🟢 修复 [#4828](https://github.com/modelcontextprotocol/servers/pull/4828) 已提交 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`update_span_properties_from_generation_span_data` 只在 `if usage:` 里绑定 `input_tokens` / `output_tokens`，却在守卫外无条件读它们。而 `GenerationSpanData.usage` 的契约类型是 `dict \| None = None`，agents SDK 在模型调用失败（坏 API key、429、连接错误、超时）时正是以 `usage=None` 收尾，于是抛 `UnboundLocalError`；异常逃出 `DeepEvalTracingProcessor.on_span_end` 后被 SDK 吞掉，observer 永不退出：该 `LlmSpan` 一直留在 `current_span_context` 与 `trace_manager.active_spans` 里，进程后续所有 span 都挂到这个再也不会结束的陈旧 span 上。同文件的 `update_span_properties_from_response_span_data` 在同类守卫前已把可选局部量初始化为 `None`](https://github.com/confident-ai/deepeval/pull/3315) `2026-09-19` | 🟢 直接提 PR（未建 issue） |
| [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines) ⭐16k | [`_ensure_json_quoted` 用 `String(f'"{term.value}"')` 手工加引号，从不转义值本身，生成的正则只匹配**未转义**的文本。`list[Literal['say "hi"']]` 于是编出 `\[("say\ "hi"")(,\ ("say\ "hi""))*\]`，而 `json.dumps` 产出的合法编码 `["say \"hi\""]` 反而 `re.fullmatch` 不中——含 `"`、`\` 或控制字符的字面量全部失效](https://github.com/dottxt-ai/outlines/pull/2045) `2026-09-19` | 🟢 直接提 PR（未建 issue） |
| [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) ⭐16k | [`PerplexityLLMAdapter` 合并相邻同角色消息以满足 Perplexity 的严格交替要求，但合并时只把 `content` 搬过去就丢掉被吸收的消息，携带 `tool_calls` 的消息因此丢调用：`[assistant(text), assistant(tool_calls: c1), tool(c1)]` 变成 `[assistant(text), tool(c1)]`，工具结果回答的是一个已经不在请求里的调用；`[assistant(tool_calls: c1, c2), tool(c1), tool(c2)]` 则把两个结果都落到 `c1` 上、`c2` 无人回答。而连续 `tool` 消息合并后，两个结果也只能挂到第一个调用的 id 上](https://github.com/pipecat-ai/pipecat/pull/5855) `2026-09-19` | 🟢 直接提 PR（未建 issue） |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) ⭐52k | [`CodeActAgent.__init__` 就地修改调用方传进来的 `tools` 列表：`tools = tools or []` 在列表非空时求值就是调用方那个对象（`[]` 兜底只在 `None`/空列表时新建），紧接着的 `tools.append(内部 execute 工具)` 便写进了调用方的列表。两个 agent 共用一份工具列表时，每次构造都多出一个重复的 `execute` 工具，而调用方自己从没动过这个列表](https://github.com/run-llama/llama_index/pull/23136) `2026-09-19` | 🟢 直接提 PR（未建 issue） |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [`AGUIEventCollector._handle_messages_snapshot` 用 `str(getattr(msg, "content", ""))` 构造内容，把 `ag_ui.core` 文档化的两种内容形态都毁掉：`AssistantMessage.content` 是 `Optional[str]`、默认 `None`（工具调用轮的常见形态），`str(None)` 得到四个字符的 `"None"`，这个值会经 `build_sample` → `extract_response` 进到 `SingleTurnSample.response`，指标拿字面量 `None` 当回答打分；`UserMessage.content` 是 `Union[str, List[InputContentPart]]`，多模态时 `str([TextInputContent(...)])` 得到的是 pydantic repr 而不是用户实际文本](https://github.com/vibrantlabsai/ragas/pull/3020) `2026-09-19` | 🟢 直接提 PR（未建 issue） |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [`llm_factory(..., mode=...)` 文档把 `mode` 写成结构化输出的 instructor 模式（默认 `Mode.JSON`），`_get_instructor_client()` 也会把 `None` 归一成 `Mode.JSON`，但归一后的值只传给了部分分支：`from_openai` / `from_litellm` / `_patch_client_for_provider` 都带 `mode=`，而 anthropic 与 google 分支调 `instructor.from_anthropic(client)`、`from_genai(client)`、`from_gemini(client)` 时**完全没有 `mode` 参数**，perplexity 分支同样丢。两个 provider 都会走默认路径（`auto_detect_adapter()` 把 `anthropic` 与新 `google.genai.Client` 路由到 instructor 适配器），于是客户端停在 instructor 各自工厂的默认模式（`from_anthropic`/`from_genai` 是 `Mode.TOOLS`、`from_gemini` 是 `Mode.MD_JSON`）而非请求的、也是文档默认的 `Mode.JSON`](https://github.com/vibrantlabsai/ragas/issues/3021) `2026-09-19` | 🟢 修复 [#3022](https://github.com/vibrantlabsai/ragas/pull/3022) 已提交 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [Anthropic 扩展思考：开启 thinking 后，紧跟在 `tool_result` 前的 assistant 消息必须带上产生该 `tool_use` 的 thinking block，而 provider 只在纯文本返回路径上保存这些块——工具调用响应会提前 `return`，于是后续请求只回放裸 `tool_use`，缺了 API 要求的前置思考块（流式路径早在 `get_final_message()` 之后就捕获，同步路径是唯一的例外）](https://github.com/crewAIInc/crewAI/pull/7577) `2026-09-18` | 🟢 直接提 PR（未建 issue） |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) ⭐20k | [`DefaultAgent.forward_with_handling` 把 requery 计数器同时当作循环卫兵，而循环体里包含**首次**模型查询：`max_requeries=N` 时最多只跑 N 次 `forward()`，即只给到 N-1 次重试；`max_requeries=0` 时循环体一次都不执行，`self.forward()` 从不被调用，`run()` 直接返回空轨迹的 `exit_format`。字段文档写的是“出错后重新查询的最大次数”，卫兵应无条件放行首次尝试](https://github.com/SWE-agent/SWE-agent/pull/1558) `2026-09-18` | 🟢 直接提 PR（未建 issue） |
| [e2b-dev/E2B](https://github.com/e2b-dev/E2B) ⭐14k | [`run_code(timeout=N)` 实际在约 `2*N` 秒才超时：pyqwest 传输层把读写两个 deadline 相加当成一个整体 deadline](https://github.com/e2b-dev/E2B/issues/1881) `2026-09-17` | 🟢 修复 [#1886](https://github.com/e2b-dev/E2B/pull/1886) 已提交 |
| [SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent) ⭐20k | [`BinaryTrajectoryComparisonConfig.comparison_temperature` 文档说是覆盖项，实际从不生效，成对比较查询仍跑模型自己的 temperature](https://github.com/SWE-agent/SWE-agent/issues/1556) `2026-09-17` | 🟢 修复 [#1557](https://github.com/SWE-agent/SWE-agent/pull/1557) 已提交 |
| [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines) ⭐16k | [LlamaCppTokenizer 丢掉所有 piece 超过 32 字节的 token：缓冲区不足时 llama.cpp 返回**负**的所需长度，而非大于缓冲区的值，`n > size` 的重试分支恒不可达](https://github.com/dottxt-ai/outlines/issues/2041) `2026-09-17` | 🟢 修复 [#2042](https://github.com/dottxt-ai/outlines/pull/2042) 已提交 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐66k | [AWS Bedrock：非工具调用的 Amazon Nova 走 Converse API 发送，却用旧版 `invoke_model` 解析器解析，`generate_response` 恒返回 "Error parsing response"](https://github.com/mem0ai/mem0/issues/7360) `2026-09-17` | 🟡 已提交，等待确认 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k | [结构化输出：嵌套模型的最后一个字段是可选项时，该嵌套模型自身的 `required` 字段被整个丢掉](https://github.com/strands-agents/harness-sdk/issues/4379) `2026-09-17` | 🟢 修复 [#4391](https://github.com/strands-agents/harness-sdk/pull/4391) 已提交 |
| [livekit/agents](https://github.com/livekit/agents) ⭐14k | [`ChatContext.copy(tools=...)` 只按 name 过滤 function item，而 `FunctionCallOutput.name` 可省略且默认为空串，成对的 function call + result 会从 provider 请求里静默消失](https://github.com/livekit/agents/issues/7324) `2026-09-17` | 🟢 已被上游修复（maintainer [PR #7330](https://github.com/livekit/agents/pull/7330) 已合并，改为按 `call_id` 配对） |
| [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k | [`BaseRunOutputEvent.from_dict` 不重建 `citations`，往返后的 event 携带的是 dict，`event.citations.urls` 抛 `AttributeError`；它是 `_HAND_SERIALIZED_FIELDS` 里唯一被写却不被重建的字段](https://github.com/agno-agi/agno/issues/10272) `2026-09-17` | 🟢 修复 [#10273](https://github.com/agno-agi/agno/pull/10273) 已提交 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [everything server 的 `MCP_TINY_IMAGE` 硬编码 PNG 里 `iCCP` 块带两个错校验和：块 CRC-32 写作 `0x5321b951`（实际 `0x9004394b`），块内 zlib 流的 Adler-32 尾写作 `0x5d040ba2`（实际 `0x6f050bad`），解压直接报 `incorrect data check`，按 PNG 规范校验的解码器会拒收整个文件。只改这 8 个字节，deflate 载荷与其余字节逐一不变](https://github.com/modelcontextprotocol/servers/pull/4816) `2026-09-17` | 🟢 直接提 PR（未建 issue） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`LLamaIndexHandler.prepare_to_drop_span` 忽略 `err` 参数，抛异常结束的 span 被当作成功收尾：状态盖成 `SUCCESS`、没有错误信息、根 trace 也报 `SUCCESS`，而且从不调 `remove_span`，失败的 span 在进程生命周期内一直留在 `active_spans` 里。`llama_index_instrumentation` 只在 `except BaseException` 里调 `span_drop(..., err=e)`，这条路径上的 span 全部是失败 span；同文件的 `prepare_to_exit_span` 与 LangChain 侧同名逻辑都已正确处理](https://github.com/confident-ai/deepeval/pull/3305) `2026-09-17` | 🟢 直接提 PR（未建 issue） |
| [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k | [`_derive_entrypoint_schema` 不看 `param.kind`，把 `*args` / `**kwargs` 当成普通属性、还因为没有默认值而标进 `required`，而调用路径本来就拒绝按名绑定这两个可变参数。已发布的 `ClickUpTools.update_task(..., **kwargs)` 因此对外声明 `required: ["task_id", "kwargs"]`，模型照 schema 传 `kwargs={"name": ...}` 会让 PUT body 变成 `{"kwargs": {...}}`，想改的字段根本没发出去；`*args` 则直接以 pydantic `ValidationError` 失败](https://github.com/agno-agi/agno/pull/10271) `2026-09-17` | 🟢 直接提 PR（未建 issue） |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [`ToolUsage._format_result()` 每 3 次（`function_calling_llm` 是大模型时 4 次）工具调用就往返回串里追加一次工具目录与格式提醒，而这个返回值同时是 executor 收到的结果和 `agent.tools_results` 里存的最终答案。工具标了 `result_as_answer` 时，agent 的答案变成「工具输出 + 一段写给模型看的提醒」，而提醒在此时已经没有收件人——工具结束了这一轮，之后没有任何东西会读它](https://github.com/crewAIInc/crewAI/pull/7555) `2026-09-17` | 🟢 直接提 PR（未建 issue） |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) ⭐52k | [`_generate_early_stopping_response` 从 `memory.aget()` 取消息却没有先调 `finalize`。FunctionAgent / AgentWorkflow 的产出在 `finalize` 之前都留在 scratchpad 里，于是早停路径上的最后一次 LLM 调用只拿到原始用户消息加早停提示，模型被要求总结它从没见过的观测结果。这是唯一一处不 finalize 就读 memory 的地方（`parse_agent_output` 还专门写了注释说明必须反过来）。顺带丢掉最后一步携带 `tool_calls` 的 assistant 消息——早停触发时那些调用不会被执行，留着会让请求以「assistant tool_calls 之后没有对应 tool 消息」被 provider 拒收](https://github.com/run-llama/llama_index/pull/23113) `2026-09-17` | 🟢 直接提 PR（未建 issue） |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [sequentialthinking：`branchId` 撞上 `Object.prototype` 的键名（`constructor`、`toString` 等）时不去建分支，而是直接抛错](https://github.com/modelcontextprotocol/servers/issues/4813) `2026-09-16` | 🟢 修复 [#4814](https://github.com/modelcontextprotocol/servers/pull/4814) 已提交 |
| [camel-ai/camel](https://github.com/camel-ai/camel) ⭐18k | [非流式 ChatAgent：tool call 的 arguments 为空或被截断时抛原生 `JSONDecodeError`，整轮对话直接崩，而不是按解析失败降级](https://github.com/camel-ai/camel/issues/4338) `2026-09-16` | ⚪ 修复 [#4339](https://github.com/camel-ai/camel/pull/4339) 被关闭（维护者认为暴露解析错误是预期行为，issue 同步标记 not planned） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [LangChain 回调类实现了 `on_llm_error` / `on_tool_error` / `on_retriever_error`，独漏 `on_chain_error`，chain 失败时 span 永不收尾](https://github.com/confident-ai/deepeval/issues/3303) `2026-09-16` | 🟢 修复 [#3304](https://github.com/confident-ai/deepeval/pull/3304) 已提交 |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [`AgentGoalAccuracyWithoutReference` 从不设置 `output_type`，`metric.train()` 的指令优化拿到空 schema](https://github.com/vibrantlabsai/ragas/issues/3014) `2026-09-16` | 🟢 修复 [#3015](https://github.com/vibrantlabsai/ragas/pull/3015) 已提交 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) ⭐11k | [Python 客户端 OAuth：`initialize()` 遇到过期 access token 直接丢弃，已落盘的 refresh token 从不使用](https://github.com/mcp-use/mcp-use/issues/2560) `2026-09-16` | ⚪ 修复 [#2561](https://github.com/mcp-use/mcp-use/pull/2561) 被关闭（维护者当前只收 TypeScript 侧与亲身踩到的问题） |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) ⭐30k | [`function_schema` 把首个 keyword-only 的 `RunContextWrapper` 参数当成 context，导致每次调用都按参数位置错位被拒](https://github.com/openai/openai-agents-python/issues/5053) `2026-09-16` | ⚪ 修复 [#5056](https://github.com/openai/openai-agents-python/pull/5056) 已关闭（未合并） |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [Responses API 流式在 `available_functions` 为 `None` 时丢掉 tool call，只返回空字符串](https://github.com/crewAIInc/crewAI/issues/7497) `2026-09-16` | 🟡 社区 PR [#7502](https://github.com/crewAIInc/crewAI/pull/7502) 修复中 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k | [`~/.claude/.credentials.json` 的容器非空时，Claude 凭据加载器抛 `AttributeError`](https://github.com/bytedance/deer-flow/issues/5473) `2026-09-16` | 🟢 修复 [#5494](https://github.com/bytedance/deer-flow/pull/5494) 已合并 |
| [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k | [`BaseRunOutputEvent.from_dict` 用 `model_validate` 重建 images/videos/audio，base64 媒体不会被解码](https://github.com/agno-agi/agno/issues/10205) `2026-09-16` | 🟡 已提交，等待确认 |
| [run-llama/llama_index](https://github.com/run-llama/llama_index) ⭐52k | [CodeActAgent 在 `codeact_agent.py:110` 抛 `UnboundLocalError`，模板缺 `code_act_system_prompt` 时整个 agent 不可用](https://github.com/run-llama/llama_index/issues/23080) `2026-09-16` | 🟡 社区 PR [#23084](https://github.com/run-llama/llama_index/pull/23084) 修复中 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) ⭐12k | [Anthropic prompt adapter 忽略 str 型 system message 里的 `{{ variables }}`，发给模型的是未渲染的模板](https://github.com/Arize-ai/phoenix/issues/16228) `2026-09-16` | 🟡 已提交，等待确认 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [`git_diff` 拒收修订范围：`git_diff(repo, "main..feature")` 抛 `BadName`，而 `git diff main..feature` 本身是合法命令、工具也把 `target` 原样透传。根因是 CWE-88 防注入加固新加的 `repo.rev_parse(target)` 只解析单个对象名，`main..feature` / `main...feature` / `HEAD~1..HEAD` 被当成一个 ref 名直接否掉。改为按 `..` / `...` 拆开分别校验两端，范围可用，`-` 前缀检查与不可解析的端点仍被拒](https://github.com/modelcontextprotocol/servers/pull/4815) `2026-09-16` | 🟢 直接提 PR（未建 issue） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`AmazonBedrockModel(region_name=...)` 被静默丢弃：别名表里 `region` 声明了 `["region_name"]`，`normalize_kwargs_and_extract_aliases` 会把 `region_name` 从 `kwargs` 里 pop 进 `alias_values["region"]`，但 `__init__` 只把 `model` 与 `*_token_cost` 拷回去，`region` 没有对应的拷回。于是要么回落到 `AWS_BEDROCK_REGION`、调用方传的值无声消失，要么该环境变量未设时抛「缺少必需参数」——后者正是 #2395 报的回归，当时的修复补了别名表却漏了这一步](https://github.com/confident-ai/deepeval/pull/3297) `2026-09-16` | 🟢 直接提 PR（未建 issue） |
| [camel-ai/camel](https://github.com/camel-ai/camel) ⭐18k | [同步流式 ChatAgent 在流式工具调用超过 `tool_execution_timeout` 时抛未捕获的 `TimeoutError` 中止整个 step，而不是按契约降级](https://github.com/camel-ai/camel/issues/4336) `2026-09-15` | 🟢 修复 [#4337](https://github.com/camel-ai/camel/pull/4337) 已提交 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [`CrewStructuredTool.ainvoke()` 在 func 是异步工具的同步包装时返回未 await 的协程，异步 agent 把 `<coroutine object ...>` 当成工具结果喂给 LLM](https://github.com/crewAIInc/crewAI/issues/7474) `2026-09-15` | 🟡 社区 PR [#7475](https://github.com/crewAIInc/crewAI/pull/7475) / [#7481](https://github.com/crewAIInc/crewAI/pull/7481) 修复中 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [Azure 流式补全把并行 tool call 的增量按数组位置归并，首个 chunk 的 id 会配到最后一个 chunk 的 name 上、参数拼错](https://github.com/crewAIInc/crewAI/issues/7486) `2026-09-15` | 🟢 修复 [#7487](https://github.com/crewAIInc/crewAI/pull/7487) 已合并 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) ⭐11k | [OpenAI Responses 流式按 `call_id` 索引工具调用缓冲，但事件携带 `item_id`，导致工具调用事件永不发出、`stream()` 零 step](https://github.com/mcp-use/mcp-use/issues/2550) `2026-09-15` | 🟢 修复 [#2551](https://github.com/mcp-use/mcp-use/pull/2551) 已提交（同 issue 另有社区 PR [#2556](https://github.com/mcp-use/mcp-use/pull/2556)，已关闭） |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) ⭐30k | [`compact_conversation` 跳过 `_offload_inline_media`，摘要时内联图片从存档中丢失，而自动摘要路径会保留](https://github.com/langchain-ai/deepagents/issues/6312) `2026-09-15` | ⚪ 该仓库禁止程序化提交，issue 被自动关闭（未重开） |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) ⭐28k | [`LocalProvider.get_tasks()` 跳过 provider 自身的 transform，`add_transform(Namespace(...))` 会让后台任务注册失效](https://github.com/PrefectHQ/fastmcp/issues/5114) `2026-09-15` | 🟢 修复 [#5117](https://github.com/PrefectHQ/fastmcp/pull/5117) 已合并 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) ⭐42k | [ToolNode 拒绝合法的 `list[Command]` 返回：终止用的 ToolMessage 是 dict 形式或包在 list 形式的 `Command.update` 里时校验不通过](https://github.com/langchain-ai/langgraph/issues/8924) `2026-09-15` | 🟡 已提交，等待确认（社区 PR [#8946](https://github.com/langchain-ai/langgraph/pull/8946) 已关闭未合并） |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) ⭐28k | [顶层数组结构化输出对基元数组恒返回 `[]`，静默丢结果](https://github.com/mastra-ai/mastra/issues/23980) `2026-09-15` | 🟢 已被上游修复（[PR #24055](https://github.com/mastra-ai/mastra/pull/24055)） |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`KimiModel.__init__` 在所选模型没有登记定价时抛 `TypeError: float(None)`，模型根本无法实例化](https://github.com/confident-ai/deepeval/issues/3287) `2026-09-15` | 🟢 修复 [#3288](https://github.com/confident-ai/deepeval/pull/3288) 已提交 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐66k | [AWS Bedrock 旧版 Titan 响应恒解析为空字符串：`_parse_response` 读 Titan 从不返回的 `completion` 字段](https://github.com/mem0ai/mem0/issues/7336) `2026-09-15` | 🟡 已提交，等待确认（社区 PR [#7341](https://github.com/mem0ai/mem0/pull/7341) / [#7343](https://github.com/mem0ai/mem0/pull/7343) 均已关闭未合并，缺陷仍在） |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) ⭐30k | [Chat Completions 流式中迟到的 reasoning item 复用 `output_index 0`，与 `response.completed.output` 的索引脱节](https://github.com/openai/openai-agents-python/issues/5041) `2026-09-15` | ⚪ 维护者未接受并关闭（合成流未证明受支持的 provider 会发出该顺序，需要真实 provider 的 wire 证据） |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [AG-UI 的 MessagesSnapshot 转换丢掉每个 tool call 的 name 与 arguments，回读成 `ToolCall(name='unknown_tool', args={})`](https://github.com/vibrantlabsai/ragas/issues/3010) `2026-09-15` | 🟢 修复 [#3011](https://github.com/vibrantlabsai/ragas/pull/3011) 已提交 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) ⭐29k | [`Model.to_dict()` 丢 `custom_role_conversions`（属性名少个 s，`hasattr` 恒假）与 `client_kwargs` 里的端点配置，保存的 agent 重新加载后连回默认端点](https://github.com/huggingface/smolagents/issues/2799) `2026-09-15` | 🟡 已提交，等待确认 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) ⭐147k | [`Runnable.as_tool()` 重建 TypedDict schema 时把所有键标成必填，工具因此拒收 runnable 本身接受的输入](https://github.com/langchain-ai/langchain/issues/40455) `2026-09-15` | ⚪ 该仓库禁止程序化提交，issue 被自动关闭（未重开） |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) ⭐3.8k | [`getAllMcpTools` 只拦截跨 server 的重名工具，同一 server 内归一化后同名的两个工具会一起返回](https://github.com/openai/openai-agents-js/issues/1934) `2026-09-15` | 🟢 修复 [#1935](https://github.com/openai/openai-agents-js/pull/1935) 已获维护者 approve，等待合并 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [两个会话使用同名文件时，后注册的资源会把前一个会话的资源驱逐](https://github.com/modelcontextprotocol/servers/issues/4808) `2026-09-15` | 🟡 社区 PR [#4809](https://github.com/modelcontextprotocol/servers/pull/4809) 修复中 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [everything server 的异步 sampling / elicitation 演示工具，对在最后一次允许的轮询里已达终态的任务报超时：轮询循环最多执行 `MAX_POLL_ATTEMPTS` 次，所以它被允许发出的最后一次轮询完全可能观察到终态，而紧随其后的超时分支只看尝试计数，存在 off-by-one](https://github.com/modelcontextprotocol/servers/pull/4811) `2026-09-15` | 🟢 直接提 PR（未建 issue） |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) ⭐30k | [非流式 run 正常跑完后 `RunResult.to_state()` 不带 trace 信息，用该 state 恢复会新开一条 trace，一次逻辑运行被拆成两条：`AgentRunner._run_impl` 的多个 `RunResult` 构造点里，完成路径是唯一没有赋值 `result._trace_state` 的（其余三处都已拷贝），是 #2540 的剩余分支](https://github.com/openai/openai-agents-python/pull/5045) `2026-09-15` | ⚪ 维护者未接受并关闭（认为完成的 run 可以用 group_id 或显式 trace 关联，没有具体工作流需要复用该 trace 身份） |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k | [Human Input Card 的回执被 MCP 路由自动提升忽略：`is_real_user_message` 对这类隐藏消息没有 carve-out，路由关键词只出现在用户澄清回答里时延迟 MCP 工具永不提升](https://github.com/bytedance/deer-flow/issues/5425) `2026-09-14` | 🟢 修复 [#5426](https://github.com/bytedance/deer-flow/pull/5426) 已合并 |
| [UKGovernmentBEIS/inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) ⭐2.8k | [工具参数里的嵌套 `@dataclass`/`TypedDict` 字段带默认值时被从 `None` 强转：`tool_param` 按声明字段重建对象而非用收到的数据，模型省略 schema 已标为非必填的字段后，`int` 默认值抛 `ToolParsingError`、`str` 默认值被静默换成字面量 `"None"`、`list` 默认值抛 `TypeError` 终止样本](https://github.com/UKGovernmentBEIS/inspect_ai/issues/5243) `2026-09-04` | 🟡 已提交，等待确认（已有贡献者复核确认可复现） |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k | [OpenAIModel（Responses，TypeScript）在 function call 被 max_output_tokens 截断时报 toolUse 而非 maxTokens，Python 侧同款缺陷的 TS 版](https://github.com/strands-agents/harness-sdk/issues/4158) `2026-09-04` | 🟡 修复 [#4159](https://github.com/strands-agents/harness-sdk/pull/4159) 已获维护者 approve，仍卡首次贡献者 CI 审批门禁 |
| [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k | [同步工具执行路径把 `0` / `False` / `[]` 这类有意义的假值结果当成空结果发给模型，异步路径却会发 `"0"`](https://github.com/agno-agi/agno/issues/9947) `2026-09-04` | 🟢 修复 [#9948](https://github.com/agno-agi/agno/pull/9948) 已合并 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐83k | [MindIE 工具模式下的异步流式丢 token usage](https://github.com/bytedance/deer-flow/issues/5192) `2026-09-04` | 🟢 修复 [#5195](https://github.com/bytedance/deer-flow/pull/5195) 已合并 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) ⭐32k | [AnthropicChatModel 流式解析把一次响应里的多个 thinking block 合并成一个，只保留最后一个 signature](https://github.com/agentscope-ai/agentscope/issues/2494) `2026-09-03` | 🟢 社区 PR [#2495](https://github.com/agentscope-ai/agentscope/pull/2495) 已合并，已用我的复现脚本验证 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) ⭐20k | [MistralModel 流式模式下注册了 output tool 时，模型回复纯文本会抛裸 ValueError 或丢文本](https://github.com/pydantic/pydantic-ai/issues/8039) `2026-09-03` | 🟡 维护者已认领修复 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k | [OpenAIResponsesModel 在 function call 被 max_output_tokens 截断时报 tool_use 而非 max_tokens，截断的工具调用被直接执行](https://github.com/strands-agents/harness-sdk/issues/4135) `2026-09-03` | 🟢 修复 [#4139](https://github.com/strands-agents/harness-sdk/pull/4139) 已合并 |
| [OpenBMB/StaffDeck](https://github.com/OpenBMB/StaffDeck)（实习团队项目） | [报销额度查询对不存在的员工返回"成功"结果](https://github.com/OpenBMB/StaffDeck/issues/257) `2026-09-02` | 🟢 修复 [#258](https://github.com/OpenBMB/StaffDeck/pull/258) 已提交 |
| [OpenBMB/StaffDeck](https://github.com/OpenBMB/StaffDeck)（实习团队项目） | [`parse_bid_award` 把 TL 判定分数直接写进 `bid.score`，没有 `parse_bid_scores` 那道 0–10 夹取。越界的判定分（如 `12.0`、`-3.0`）因此进入持久化的 bid 记录，并流入 `candidate_hp`——HP 损失按 `10 - score` 计算，超过 10 的分数能把已被淘汰候选人的 HP 拉回零以上。同一个 `bid.score` 字段由两条解析路径写入，只有其中一条夹取](https://github.com/OpenBMB/StaffDeck/pull/256) `2026-09-02` | 🟢 直接提 PR（未建 issue） |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) ⭐29k | [provider 为 `<end_plan>` 返回结构化内容（内容块列表）时，`_generate_planning_step` 把整个 list 直接塞进 plan 的 f-string，而 `plan` 是字符串字段，于是计划文本变成 list 的 Python repr 而不是可读文本；生成计划与更新计划两条分支都受影响，而这段文本正是会被记日志、被下一次模型调用读回的内容](https://github.com/huggingface/smolagents/pull/2730) `2026-09-02` | 🟢 直接提 PR（未建 issue） |

---

## 🛠️ Technical Arsenal

<div align="center">

<table border="0">
<tr>
<td align="right"><b>语言</b></td>
<td>
<a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=python,ts,cpp,bash&theme=dark" alt="languages"/></a>
</td>
</tr>
<tr>
<td align="right"><b>Agent & AI</b></td>
<td>
<img src="https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph"/>
<img src="https://img.shields.io/badge/Temporal-000000?style=for-the-badge&logo=temporal&logoColor=white" alt="Temporal"/>
<img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch"/>
<img src="https://img.shields.io/badge/MCP-5A45FF?style=for-the-badge&logoColor=white" alt="MCP"/>
</td>
</tr>
<tr>
<td align="right"><b>后端 & 基础设施</b></td>
<td>
<a href="https://skillicons.dev"><img src="https://skillicons.dev/icons?i=fastapi,postgres,redis,docker,react,linux,git,githubactions&theme=dark" alt="infra"/></a>
</td>
</tr>
</table>

</div>

---

## 📊 GitHub Analytics

<div align="center">

<img height="195" src="https://raw.githubusercontent.com/BlueX888/BlueX888/metrics/stats.svg" alt="GitHub 统计"/>
<img height="195" src="https://raw.githubusercontent.com/BlueX888/BlueX888/metrics/langs.svg" alt="常用语言"/>

<br/>

<img src="https://streak-stats.demolab.com?user=BlueX888&theme=tokyonight&hide_border=true&background=00000000&locale=zh_Hans" alt="连续贡献"/>

<br/><br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/BlueX888/BlueX888/output/github-contribution-grid-snake-dark.svg"/>
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/BlueX888/BlueX888/output/github-contribution-grid-snake.svg"/>
  <img src="https://raw.githubusercontent.com/BlueX888/BlueX888/output/github-contribution-grid-snake.svg" alt="贪吃蛇贡献图"/>
</picture>

</div>

---

## 🤝 Let's Connect!

<div align="center">

[![Email](https://img.shields.io/badge/Email-li__chaoran8888%40163.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:li_chaoran8888@163.com)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/BlueX888)
[![ModelBest](https://img.shields.io/badge/Intern%20%40-ModelBest%20%2F%20OpenBMB-4A00E0?style=for-the-badge&logo=briefcase&logoColor=white)](https://github.com/OpenBMB)

</div>

---

<div align="center">

### 💭 "Talk is cheap. Show me the code."
*— Linus Torvalds*

<br/>

### 🌟 感谢来访！如果觉得这些项目有意思，给个 ⭐ 是最好的鼓励。

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A00E0,100:8E2DE2&height=120&section=footer" width="100%"/>

</div>
