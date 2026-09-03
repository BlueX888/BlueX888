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

</div>

## 🎯 About Me

我做多智能体系统。从 174 行就能读完的 deep-research 团队，到跑在 Temporal 上、有租户隔离和审计的企业级执行内核，我想搞清楚同一件事：**让一群模型可靠地协作，到底需要什么样的工程。**

**我信什么？** 模型负责判断，代码负责搬运。安全边界、状态机、可审计性这些东西应该由确定性代码兜底，而不是寄希望于 prompt。

- 🎓 **研究生：** 北京工业大学（211）· 计算机科学与技术 · 2025.09 – 2028.06
- 🎓 **本科：** 河南大学（双一流）· 计算机科学与技术 · 2021.09 – 2025.06
- 🧪 **方向：** LLM Agent 编排、持久化执行、多智能体安全治理
- 💼 **实习：** 面壁智能（ModelBest / OpenBMB）· Agent 方向 · 2026.08 至今
- 📍 **状态：** 研二在读

---

## 🔬 Current Work

- ⚙️ **SwarmCore** 正在冲 M5 里程碑（v1 候选基线）：Temporal 持久化编排 + PostgreSQL 单一事实源 + OPA/Vault 治理
- 💼 在面壁智能实习，参与 OpenBMB 的 Agent 产品（ChatDev / StaffDeck / PilotDeck）开发
- 🔧 给上游 Agent 框架修 bug、提特性：Hugging Face smolagents、Agno、OpenHands、Strands Agents
- 🔍 审 Agent 框架的核心模块（provider 适配层、streaming 聚合、tool 调用）主动找缺陷，带最小复现报 issue，再自己修
- 📖 维护 **nanoteam**，把多智能体的最小可用形态写成一本能跑的教科书

---

## 📘 Projects

| 项目 | 简介 |
|---|---|
| 🐜 [**nanoteam**](https://github.com/BlueX888/nanoteam) | 1000 行以内的 deep-research 多智能体团队，Leader–Worker 架构，CI 强制行数上限 |
| 🔨 [**forge-code**](https://github.com/BlueX888/forge-code) | 本地 AI 编程助手：跨会话项目记忆、Skill 自进化、权限沙箱 |
| 🏥 [**Medical-Agent-Swarm**](https://github.com/BlueX888/Medical-Agent-Swarm) | LangGraph 医疗问答多智能体原型，Orchestrator–Worker + 确定性安全层 |
| ⚙️ [**SwarmCore**](https://github.com/BlueX888/SwarmCore) | 企业级多租户智能体执行内核：Temporal 持久化编排、PostgreSQL 单一事实源、OPA/Vault 治理 |

---

## 🤝 Merged Upstream PRs

<!--START_SECTION:contributions-->
- [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k — [[fix] Resolve Gemini image MIME type instead of hard-coding image/jpeg](https://github.com/agno-agi/agno/pull/9887) `2026-09-02`
<!--END_SECTION:contributions-->

## 🔍 Upstream Bugs Found

自己审代码发现、带无网络最小复现报出的缺陷（PR 合并后会自动进上一栏）：

- [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k — [OpenAIResponsesModel 在 function call 被 max_output_tokens 截断时报 tool_use 而非 max_tokens，截断的工具调用被直接执行](https://github.com/strands-agents/harness-sdk/issues/4135) `2026-09-03` · 已被打上 `bug`，修复待认领
- [OpenBMB/StaffDeck](https://github.com/OpenBMB/StaffDeck)（实习所在团队的项目）— [报销额度查询对不存在的员工返回"成功"结果](https://github.com/OpenBMB/StaffDeck/issues/257) `2026-09-02` · 修复 [#258](https://github.com/OpenBMB/StaffDeck/pull/258) 已提交

---

## 🛠️ Technical Arsenal

### 语言
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)

### Agent & AI
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Temporal](https://img.shields.io/badge/Temporal-000000?style=for-the-badge&logo=temporal&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-5A45FF?style=for-the-badge&logoColor=white)

### 后端与基础设施
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![NATS](https://img.shields.io/badge/NATS-27AAE1?style=for-the-badge&logo=natsdotio&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)

---

## 📊 GitHub Analytics

<div align="center">

<img height="195" src="https://raw.githubusercontent.com/BlueX888/BlueX888/metrics/stats.svg" alt="GitHub 统计"/>
<img height="195" src="https://raw.githubusercontent.com/BlueX888/BlueX888/metrics/langs.svg" alt="常用语言"/>

<img src="https://streak-stats.demolab.com?user=BlueX888&theme=tokyonight&hide_border=true&background=00000000&locale=zh_Hans" alt="连续贡献"/>

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

---

### 🌟 感谢来访！如果觉得这些项目有意思，给个 ⭐ 是最好的鼓励。

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A00E0,100:8E2DE2&height=120&section=footer" width="100%"/>

</div>
