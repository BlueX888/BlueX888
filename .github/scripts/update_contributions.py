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


def fetch():
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
        raise SystemExit("GraphQL errors: %s" % data["errors"])
    return [n for n in data["data"]["search"]["nodes"] if n]


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


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "README.md"
    text = open(path, encoding="utf-8").read()
    if START not in text or END not in text:
        raise SystemExit("README 缺少 contributions 标记")
    body = render(fetch())
    new = re.sub(
        re.escape(START) + r".*?" + re.escape(END),
        f"{START}\n{body}\n{END}",
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
