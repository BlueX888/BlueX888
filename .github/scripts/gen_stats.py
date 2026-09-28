#!/usr/bin/env python3
"""生成 profile 统计卡 SVG（透明底，深浅两套配色）。

深色沿用 tokyonight（与 README 其他卡片一致），浅色对齐 GitHub Primer 的前景色，
README 用 <picture> 按访客的 GitHub 主题二选一：stats.svg / langs.svg 是深色，*-light.svg 是浅色。
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

# 文件名后缀 -> 配色。卡片是透明底，bg 只用来判断语言色点在该主题下够不够显眼
PALETTES = {
    "": {"title": "#A78BFA", "text": "#C0CAF5", "muted": "#565F89", "icon": "#7AA2F7", "bg": "#0D1117"},
    "-light": {"title": "#8250DF", "text": "#1F2328", "muted": "#656D76", "icon": "#0969DA", "bg": "#FFFFFF"},
}
FALLBACK_LANG_COLOR = "#8E2DE2"

# Octicons 16px 路径（@primer/octicons，MIT）。SVG 以 <img> 嵌进主页时用不上 emoji 字体，图标得画成矢量
ICONS = {
    "calendar": "M4.75 0a.75.75 0 0 1 .75.75V2h5V.75a.75.75 0 0 1 1.5 0V2h1.25c.966 0 1.75.784 1.75 1.75v10.5A1.75 1.75 0 0 1 13.25 16H2.75A1.75 1.75 0 0 1 1 14.25V3.75C1 2.784 1.784 2 2.75 2H4V.75A.75.75 0 0 1 4.75 0ZM2.5 7.5v6.75c0 .138.112.25.25.25h10.5a.25.25 0 0 0 .25-.25V7.5Zm10.75-4H2.75a.25.25 0 0 0-.25.25V6h11V3.75a.25.25 0 0 0-.25-.25Z",
    "git-commit": "M11.93 8.5a4.002 4.002 0 0 1-7.86 0H.75a.75.75 0 0 1 0-1.5h3.32a4.002 4.002 0 0 1 7.86 0h3.32a.75.75 0 0 1 0 1.5Zm-1.43-.75a2.5 2.5 0 1 0-5 0 2.5 2.5 0 0 0 5 0Z",
    "star": "M8 .25a.75.75 0 0 1 .673.418l1.882 3.815 4.21.612a.75.75 0 0 1 .416 1.279l-3.046 2.97.719 4.192a.751.751 0 0 1-1.088.791L8 12.347l-3.766 1.98a.75.75 0 0 1-1.088-.79l.72-4.194L.818 6.374a.75.75 0 0 1 .416-1.28l4.21-.611L7.327.668A.75.75 0 0 1 8 .25Zm0 2.445L6.615 5.5a.75.75 0 0 1-.564.41l-3.097.45 2.24 2.184a.75.75 0 0 1 .216.664l-.528 3.084 2.769-1.456a.75.75 0 0 1 .698 0l2.77 1.456-.53-3.084a.75.75 0 0 1 .216-.664l2.24-2.183-3.096-.45a.75.75 0 0 1-.564-.41L8 2.694Z",
    "git-pull-request": "M1.5 3.25a2.25 2.25 0 1 1 3 2.122v5.256a2.251 2.251 0 1 1-1.5 0V5.372A2.25 2.25 0 0 1 1.5 3.25Zm5.677-.177L9.573.677A.25.25 0 0 1 10 .854V2.5h1A2.5 2.5 0 0 1 13.5 5v5.628a2.251 2.251 0 1 1-1.5 0V5a1 1 0 0 0-1-1h-1v1.646a.25.25 0 0 1-.427.177L7.177 3.427a.25.25 0 0 1 0-.354ZM3.75 2.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm0 9.5a.75.75 0 1 0 0 1.5.75.75 0 0 0 0-1.5Zm8.25.75a.75.75 0 1 0 1.5 0 .75.75 0 0 0-1.5 0Z",
    "issue-opened": "M8 9.5a1.5 1.5 0 1 0 0-3 1.5 1.5 0 0 0 0 3ZM8 0a8 8 0 1 1 0 16A8 8 0 0 1 8 0ZM1.5 8a6.5 6.5 0 1 0 13 0 6.5 6.5 0 0 0-13 0Z",
}

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


def luminance(color):
    h = color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    rgb = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    r, g, b = [c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4 for c in rgb]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    hi, lo = sorted((luminance(a), luminance(b)), reverse=True)
    return (hi + 0.05) / (lo + 0.05)


def svg_card(width, height, title, body, pal):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" fill="none" role="img">
  <style>
    text {{ font-family: 'Segoe UI', Ubuntu, 'Helvetica Neue', sans-serif; }}
    .title {{ font-size: 18px; font-weight: 600; fill: {pal["title"]}; }}
    .label {{ font-size: 14px; fill: {pal["text"]}; }}
    .value {{ font-size: 14px; font-weight: 600; fill: {pal["title"]}; }}
    .icon  {{ fill: {pal["icon"]}; }}
    .pct   {{ font-size: 12px; fill: {pal["muted"]}; }}
    /* 默认可见；支持 CSS 动画的环境才做淡入（backwards 让 delay 期间应用 from 状态） */
    .fade  {{ animation: fadein 0.5s ease-in-out backwards; }}
    @keyframes fadein {{ from {{ opacity: 0; }} }}
  </style>
  <text x="25" y="33" class="title fade">{title}</text>
{body}
</svg>"""


def build_stats_card(user, pal):
    cc = user["contributionsCollection"]
    stars = sum(r["stargazerCount"] for r in user["repositories"]["nodes"])
    rows = [
        ("calendar", "过去一年贡献", cc["contributionCalendar"]["totalContributions"]),
        ("git-commit", "提交 Commits（近一年）", cc["totalCommitContributions"]),
        ("star", "获得 Stars", stars),
        ("git-pull-request", "Pull Requests", cc["totalPullRequestContributions"]),
        ("issue-opened", "Issues", cc["totalIssueContributions"]),
    ]
    body = []
    for i, (icon, label, value) in enumerate(rows):
        y = 62 + i * 26
        body.append(
            f'  <g class="fade" style="animation-delay:{150 + i * 100}ms">\n'
            f'    <path transform="translate(25 {y - 13})" class="icon" d="{ICONS[icon]}"/>\n'
            f'    <text x="50" y="{y}" class="label">{label}:</text>\n'
            f'    <text x="240" y="{y}" class="value">{value}</text>\n'
            f"  </g>"
        )
    return svg_card(300, 195, f"{USER} 的 GitHub 统计", "\n".join(body), pal)


def build_langs_card(user, pal):
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
        f'  <rect x="{bar_x}" y="50" width="{bar_w}" height="10" rx="5" fill="{pal["muted"]}" opacity="0.25"/>'
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
        # 与底色太接近的语言色（深色下的 PowerShell、浅色下的 JavaScript）描一圈边，免得色点看不见
        ring = f' stroke="{pal["muted"]}"' if contrast(colors[name], pal["bg"]) < 2 else ""
        legend.append(
            f'  <g class="fade" style="animation-delay:{300 + i * 80}ms">\n'
            f'    <circle cx="{lx + 5}" cy="{ly - 4}" r="5" fill="{colors[name]}"{ring}/>\n'
            f'    <text x="{lx + 18}" y="{ly}" class="label">{name}</text>\n'
            f'    <text x="{lx + 100}" y="{ly}" class="pct">{pct:.1f}%</text>\n'
            f"  </g>"
        )
    return svg_card(width, 195, "常用语言", "\n".join(segs + legend), pal)


def main():
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "dist"
    os.makedirs(out_dir, exist_ok=True)
    user = fetch()
    for suffix, pal in PALETTES.items():
        for name, svg in (("stats", build_stats_card(user, pal)), ("langs", build_langs_card(user, pal))):
            path = os.path.join(out_dir, f"{name}{suffix}.svg")
            with open(path, "w", encoding="utf-8") as f:
                f.write(svg)
            print("wrote", path)


if __name__ == "__main__":
    main()
