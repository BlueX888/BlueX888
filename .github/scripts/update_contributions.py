#!/usr/bin/env python3
"""把已合并到他人仓库的 PR 写进 README 的 contributions 区块。

用法: GITHUB_TOKEN=xxx python3 update_contributions.py README.md
"""
import json
import os
import re
import sys
import urllib.request

USER = "BlueX888"
START, END = "<!--START_SECTION:contributions-->", "<!--END_SECTION:contributions-->"

# 每个已合并 PR 的一句话说明（问题 → 影响 → 修法），键为 owner/repo#number。
# 新 PR 合并后在这里补一行即可；没有说明的 PR 只渲染标题行。
NOTES = {
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


def fetch_once():
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY}).encode(),
        headers={
            "Authorization": "bearer " + os.environ["GITHUB_TOKEN"],
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = json.loads(resp.read())
    if "errors" in data:
        raise RuntimeError("GraphQL errors: %s" % data["errors"])
    return [n for n in data["data"]["search"]["nodes"] if n]


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


def render(prs):
    if not prs:
        return "_暂无_"
    prs.sort(key=lambda p: p["mergedAt"], reverse=True)
    lines = []
    for p in prs:
        repo = p["repository"]
        lines.append(
            f"- [{repo['nameWithOwner']}]({repo['url']}) ⭐{fmt_stars(repo['stargazerCount'])} — "
            f"[{p['title']}]({p['url']}) `{p['mergedAt'][:10]}`"
        )
        note = NOTES.get(f"{repo['nameWithOwner']}#{p['number']}")
        if note:
            lines.append(f"  - {note}")
    return "\n".join(lines)


def count_entries(section):
    return sum(1 for line in section.splitlines() if line.startswith("- ["))


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
    # 用 callable 替换：body 里有反斜杠（说明文字里引用的文件名）时，
    # 字符串模板会被 re 当成转义序列解析，`\q` 这种直接抛 re.error。
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        lambda _m: f"{START}\n{body}\n{END}",
        text,
        flags=re.S,
    )
    if new != text:
        open(path, "w", encoding="utf-8").write(new)
        print("updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
