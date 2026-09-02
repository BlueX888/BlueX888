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


def render(prs):
    if not prs:
        return "_暂无_"
    prs.sort(key=lambda p: p["mergedAt"], reverse=True)
    lines = []
    for p in prs:
        repo = p["repository"]
        lines.append(
            f"- [{repo['nameWithOwner']}]({repo['url']}) ⭐{repo['stargazerCount']:,} — "
            f"[{p['title']}]({p['url']}) `{p['mergedAt'][:10]}`"
        )
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
