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
- [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k — [[fix] keep falsy tool results (0, False, []) on the sync tool execution path](https://github.com/agno-agi/agno/pull/9948) `2026-09-16`
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

自己审代码发现、带无网络最小复现报出的缺陷，能直接修的当天同步提 PR（合并后会自动进上一栏）：

| 仓库 | 问题 | 状态 |
|:--|:--|:--|
| [camel-ai/camel](https://github.com/camel-ai/camel) ⭐18k | [同步流式 ChatAgent 在流式工具调用超过 `tool_execution_timeout` 时抛未捕获的 `TimeoutError` 中止整个 step，而不是按契约降级](https://github.com/camel-ai/camel/issues/4336) `2026-09-15` | 🟢 修复 [#4337](https://github.com/camel-ai/camel/pull/4337) 已提交 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [`CrewStructuredTool.ainvoke()` 在 func 是异步工具的同步包装时返回未 await 的协程，异步 agent 把 `<coroutine object ...>` 当成工具结果喂给 LLM](https://github.com/crewAIInc/crewAI/issues/7474) `2026-09-15` | 🟡 社区 PR [#7475](https://github.com/crewAIInc/crewAI/pull/7475) / [#7481](https://github.com/crewAIInc/crewAI/pull/7481) 修复中 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) ⭐59k | [Azure 流式补全把并行 tool call 的增量按数组位置归并，首个 chunk 的 id 会配到最后一个 chunk 的 name 上、参数拼错](https://github.com/crewAIInc/crewAI/issues/7486) `2026-09-15` | 🟢 修复 [#7487](https://github.com/crewAIInc/crewAI/pull/7487) 已合并 |
| [mcp-use/mcp-use](https://github.com/mcp-use/mcp-use) ⭐11k | [OpenAI Responses 流式按 `call_id` 索引工具调用缓冲，但事件携带 `item_id`，导致工具调用事件永不发出、`stream()` 零 step](https://github.com/mcp-use/mcp-use/issues/2550) `2026-09-15` | 🟢 修复 [#2551](https://github.com/mcp-use/mcp-use/pull/2551) 已提交 |
| [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents) ⭐29k | [`compact_conversation` 跳过 `_offload_inline_media`，摘要时内联图片从存档中丢失，而自动摘要路径会保留](https://github.com/langchain-ai/deepagents/issues/6312) `2026-09-15` | ⚪ 该仓库禁止程序化提交，issue 被自动关闭（未重开） |
| [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) ⭐28k | [`LocalProvider.get_tasks()` 跳过 provider 自身的 transform，`add_transform(Namespace(...))` 会让后台任务注册失效](https://github.com/PrefectHQ/fastmcp/issues/5114) `2026-09-15` | 🟢 修复 [#5117](https://github.com/PrefectHQ/fastmcp/pull/5117) 已合并 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) ⭐42k | [ToolNode 拒绝合法的 `list[Command]` 返回：终止用的 ToolMessage 是 dict 形式或包在 list 形式的 `Command.update` 里时校验不通过](https://github.com/langchain-ai/langgraph/issues/8924) `2026-09-15` | 🟡 已提交，等待确认 |
| [mastra-ai/mastra](https://github.com/mastra-ai/mastra) ⭐28k | [顶层数组结构化输出对基元数组恒返回 `[]`，静默丢结果](https://github.com/mastra-ai/mastra/issues/23980) `2026-09-15` | 🟡 已提交，等待确认 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) ⭐18k | [`KimiModel.__init__` 在所选模型没有登记定价时抛 `TypeError: float(None)`，模型根本无法实例化](https://github.com/confident-ai/deepeval/issues/3287) `2026-09-15` | 🟢 修复 [#3288](https://github.com/confident-ai/deepeval/pull/3288) 已提交 |
| [mem0ai/mem0](https://github.com/mem0ai/mem0) ⭐65k | [AWS Bedrock 旧版 Titan 响应恒解析为空字符串：`_parse_response` 读 Titan 从不返回的 `completion` 字段](https://github.com/mem0ai/mem0/issues/7336) `2026-09-15` | 🟡 已提交，等待确认 |
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) ⭐29k | [Chat Completions 流式中迟到的 reasoning item 复用 `output_index 0`，与 `response.completed.output` 的索引脱节](https://github.com/openai/openai-agents-python/issues/5041) `2026-09-15` | 🟡 社区 PR [#5042](https://github.com/openai/openai-agents-python/pull/5042) 修复中 |
| [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) ⭐16k | [AG-UI 的 MessagesSnapshot 转换丢掉每个 tool call 的 name 与 arguments，回读成 `ToolCall(name='unknown_tool', args={})`](https://github.com/vibrantlabsai/ragas/issues/3010) `2026-09-15` | 🟢 修复 [#3011](https://github.com/vibrantlabsai/ragas/pull/3011) 已提交 |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) ⭐29k | [`Model.to_dict()` 丢 `custom_role_conversions`（属性名少个 s，`hasattr` 恒假）与 `client_kwargs` 里的端点配置，保存的 agent 重新加载后连回默认端点](https://github.com/huggingface/smolagents/issues/2799) `2026-09-15` | 🟡 已提交，等待确认 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) ⭐146k | [`Runnable.as_tool()` 重建 TypedDict schema 时把所有键标成必填，工具因此拒收 runnable 本身接受的输入](https://github.com/langchain-ai/langchain/issues/40455) `2026-09-15` | ⚪ 该仓库禁止程序化提交，issue 被自动关闭（未重开） |
| [openai/openai-agents-js](https://github.com/openai/openai-agents-js) ⭐3.8k | [`getAllMcpTools` 只拦截跨 server 的重名工具，同一 server 内归一化后同名的两个工具会一起返回](https://github.com/openai/openai-agents-js/issues/1934) `2026-09-15` | 🟢 修复 [#1935](https://github.com/openai/openai-agents-js/pull/1935) 已提交 |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) ⭐90k | [两个会话使用同名文件时，后注册的资源会把前一个会话的资源驱逐](https://github.com/modelcontextprotocol/servers/issues/4808) `2026-09-15` | 🟡 社区 PR [#4809](https://github.com/modelcontextprotocol/servers/pull/4809) 修复中 |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐82k | [Human Input Card 的回执被 MCP 路由自动提升忽略：`is_real_user_message` 对这类隐藏消息没有 carve-out，路由关键词只出现在用户澄清回答里时延迟 MCP 工具永不提升](https://github.com/bytedance/deer-flow/issues/5425) `2026-09-14` | 🟢 修复 [#5426](https://github.com/bytedance/deer-flow/pull/5426) 已合并 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k | [OpenAIModel（Responses，TypeScript）在 function call 被 max_output_tokens 截断时报 toolUse 而非 maxTokens，Python 侧同款缺陷的 TS 版](https://github.com/strands-agents/harness-sdk/issues/4158) `2026-09-04` | 🟡 修复 [#4159](https://github.com/strands-agents/harness-sdk/pull/4159) 已获维护者 approve，仍卡首次贡献者 CI 审批门禁 |
| [agno-agi/agno](https://github.com/agno-agi/agno) ⭐42k | [同步工具执行路径把 `0` / `False` / `[]` 这类有意义的假值结果当成空结果发给模型，异步路径却会发 `"0"`](https://github.com/agno-agi/agno/issues/9947) `2026-09-04` | 🟡 修复 [#9948](https://github.com/agno-agi/agno/pull/9948) 已提交，等待 review |
| [bytedance/deer-flow](https://github.com/bytedance/deer-flow) ⭐82k | [MindIE 工具模式下的异步流式丢 token usage](https://github.com/bytedance/deer-flow/issues/5192) `2026-09-04` | 🟢 社区 PR [#5195](https://github.com/bytedance/deer-flow/pull/5195) 已修复 |
| [agentscope-ai/agentscope](https://github.com/agentscope-ai/agentscope) ⭐31k | [AnthropicChatModel 流式解析把一次响应里的多个 thinking block 合并成一个，只保留最后一个 signature](https://github.com/agentscope-ai/agentscope/issues/2494) `2026-09-03` | 🟡 社区 PR [#2495](https://github.com/agentscope-ai/agentscope/pull/2495) 修复中，已用我的复现脚本验证 |
| [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) ⭐20k | [MistralModel 流式模式下注册了 output tool 时，模型回复纯文本会抛裸 ValueError 或丢文本](https://github.com/pydantic/pydantic-ai/issues/8039) `2026-09-03` | 🟡 维护者已认领修复 |
| [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk) ⭐7k | [OpenAIResponsesModel 在 function call 被 max_output_tokens 截断时报 tool_use 而非 max_tokens，截断的工具调用被直接执行](https://github.com/strands-agents/harness-sdk/issues/4135) `2026-09-03` | 🟢 修复 [#4139](https://github.com/strands-agents/harness-sdk/pull/4139) 已合并 |
| [OpenBMB/StaffDeck](https://github.com/OpenBMB/StaffDeck)（实习团队项目） | [报销额度查询对不存在的员工返回"成功"结果](https://github.com/OpenBMB/StaffDeck/issues/257) `2026-09-02` | 🟢 修复 [#258](https://github.com/OpenBMB/StaffDeck/pull/258) 已提交 |

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
