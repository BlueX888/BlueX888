#!/usr/bin/env python3
"""生成 profile 统计卡 SVG（tokyonight 透明风格，与 README 其他卡片一致）。

数据来自 GitHub GraphQL API，只读公开数据，GITHUB_TOKEN 即可。
用法: GITHUB_TOKEN=xxx python3 gen_stats.py <输出目录>
"""
import json
import os
import sys
import urllib.request

USER = "BlueX888"

# TrainQwenCodder 含 20MB 生成的 JS 训练数据，会淹没语言统计；HTML 多为构建产物
EXCLUDE_REPOS = {"TrainQwenCodder"}
HIDE_LANGS = {"HTML"}

# tokyonight 配色
TITLE = "#A78BFA"
TEXT = "#C0CAF5"
MUTED = "#565F89"
ICON = "#7AA2F7"
FALLBACK_LANG_COLOR = "#8E2DE2"

QUERY = """
{
  user(login: "%s") {
    followers { totalCount }
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false, privacy: PUBLIC) {
      totalCount
      nodes {
        name
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      contributionCalendar { totalContributions }
    }
  }
}
""" % USER


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
    return data["data"]["user"]


def svg_card(width, height, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img">
  <style>
    text {{ font-family: 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; }}
    .title {{ font-size: 18px; font-weight: 600; fill: {TITLE}; }}
    .label {{ font-size: 14px; fill: {TEXT}; }}
    .value {{ font-size: 14px; font-weight: 600; fill: {TITLE}; }}
    .icon  {{ font-size: 14px; }}
    .pct   {{ font-size: 12px; fill: {MUTED}; }}
    /* 默认可见；支持 CSS 动画的环境才做淡入（backwards 让 delay 期间应用 from 状态） */
    .fade  {{ animation: fadein 0.5s ease-in-out backwards; }}
    @keyframes fadein {{ from {{ opacity: 0; }} }}
  </style>
  <text x="25" y="33" class="title fade">{title}</text>
{body}
</svg>"""


def build_stats_card(user):
    cc = user["contributionsCollection"]
    stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])
    rows = [
        ("🗓", "过去一年贡献", cc["contributionCalendar"]["totalContributions"]),
        ("⚡", "提交 Commits（近一年）", cc["totalCommitContributions"]),
        ("⭐", "获得 Stars", stars),
        ("🔀", "Pull Requests", cc["totalPullRequestContributions"]),
        ("🐛", "Issues", cc["totalIssueContributions"]),
    ]
    body = []
    for i, (icon, label, value) in enumerate(rows):
        y = 62 + i * 26
        body.append(
            f'  <g class="fade" style="animation-delay:{150 + i * 100}ms">\n'
            f'    <text x="25" y="{y}" class="icon">{icon}</text>\n'
            f'    <text x="50" y="{y}" class="label">{label}:</text>\n'
            f'    <text x="240" y="{y}" class="value">{value}</text>\n'
            f"  </g>"
        )
    return svg_card(300, 195, f"{USER} 的 GitHub 统计", "\n".join(body))


def build_langs_card(user):
    sizes, colors = {}, {}
    for repo in user["repositories"]["nodes"]:
        if repo["name"] in EXCLUDE_REPOS:
            continue
        for edge in repo["languages"]["edges"]:
            name = edge["node"]["name"]
            if name in HIDE_LANGS:
                continue
            sizes[name] = sizes.get(name, 0) + edge["size"]
            colors[name] = edge["node"]["color"] or FALLBACK_LANG_COLOR
    top = sorted(sizes.items(), key=lambda kv: -kv[1])[:6]
    total = sum(v for _, v in top) or 1

    width, bar_x, bar_w = 340, 25, 290
    # 单条堆叠进度条
    segs, x = [], float(bar_x)
    segs.append(
        f'  <rect x="{bar_x}" y="50" width="{bar_w}" height="10" rx="5" fill="{MUTED}" opacity="0.25"/>'
    )
    segs.append(f'  <clipPath id="bar"><rect x="{bar_x}" y="50" width="{bar_w}" height="10" rx="5"/></clipPath>')
    segs.append('  <g clip-path="url(#bar)" class="fade" style="animation-delay:150ms">')
    for name, size in top:
        w = bar_w * size / total
        segs.append(f'    <rect x="{x:.1f}" y="50" width="{w:.1f}" height="10" fill="{colors[name]}"/>')
        x += w
    segs.append("  </g>")

    # 两列图例
    legend = []
    for i, (name, size) in enumerate(top):
        col, row = i % 2, i // 2
        lx = bar_x + col * 150
        ly = 84 + row * 24
        pct = 100.0 * size / total
        legend.append(
            f'  <g class="fade" style="animation-delay:{300 + i * 80}ms">\n'
            f'    <circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{colors[name]}"/>\n'
            f'    <text x="{lx + 18}" y="{ly}" class="label">{name}</text>\n'
            f'    <text x="{lx + 100}" y="{ly}" class="pct">{pct:.1f}%</text>\n'
            f"  </g>"
        )
    return svg_card(width, 195, "常用语言", "\n".join(segs + legend))


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "dist"
    os.makedirs(out_dir, exist_ok=True)
    user = fetch()
    for name, svg in (("stats.svg", build_stats_card(user)), ("langs.svg", build_langs_card(user))):
        path = os.path.join(out_dir, name)
        with open(path, "w", encoding="utf-8") as f:
            f.write(svg)
        print("wrote", path)


if __name__ == "__main__":
    main()
