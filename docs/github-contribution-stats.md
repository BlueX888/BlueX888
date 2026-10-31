# GitHub 贡献数据统计 · BlueX888

> 统计时间：**2026-10-31**
> 统计对象：GitHub 公开数据，账号 [`BlueX888`](https://github.com/BlueX888)
> “上游”指非本人拥有的仓库；“本人作为作者”指 PR / Issue / commit 的 author 为 BlueX888。

## 一、结论

| 指标 | 数量 | 判定口径 |
|---|---:|---|
| **合并 N** | **44** | 本人为 PR 作者，PR 已被非本人仓库正式合并（含 squash / rebase / merge commit） |
| **修补 N** | **3** | 本人补丁被上游采纳，但并非通过合并本人 PR 纳入；有 commit 作者、Co-authored-by 或维护者明文致谢作证 |
| **问题获修 N** | **30** | 本人报告 Issue，由其他贡献者完成修复，且 Issue 与实际修复之间有明确关联；已剔除与“修补 3 项”重叠的 issue |
| 问题获修（不去重） | 33 | 含 3 个“修复本身也是本人补丁被采纳”的 issue |

三个指标按互斥口径使用：**44 / 3 / 30**。
若只按各自定义直接计数、允许重叠，则是 **44 / 3 / 33**。

另有 2 项上游在 PR 中明文致谢“原型来自本人 PR”，但最终实现不同、未采用本人补丁，单独列在第四节，是否算“修补”建议自行决定。

---

## 二、合并 N = 44

口径：`is:pr author:BlueX888 is:merged` 共 193 个；其中 149 个合并进本人仓库（`BlueX888/RunWeave` 144、`SwarmCore` 2 等），不计入上游贡献。剩余 **44 个**分布在 11 个上游仓库。

| 上游仓库 | 合并 PR 数 |
|---|---:|
| bytedance/deer-flow | 18 |
| PrefectHQ/fastmcp | 8 |
| livekit/agents | 5 |
| strands-agents/harness-sdk | 3 |
| agno-agi/agno | 3 |
| mcp-use/mcp-use | 2 |
| langgenius/dify | 1 |
| agentscope-ai/agentscope | 1 |
| Arize-ai/phoenix | 1 |
| openai/openai-agents-js | 1 |
| crewAIInc/crewAI | 1 |
| **合计** | **44** |

### 完整清单（按合并时间倒序）

| 合并日期 | PR | 标题 |
|---|---|---|
| 2026-10-30 | [PrefectHQ/fastmcp#5847](https://github.com/PrefectHQ/fastmcp/pull/5847) | fix(openapi): preserve timeouts so the server maps them to the actionable message |
| 2026-10-30 | [langgenius/dify#45088](https://github.com/langgenius/dify/pull/45088) | fix(api): fall back to the raw reference for non-object file reference payloads |
| 2026-10-22 | [bytedance/deer-flow#7088](https://github.com/bytedance/deer-flow/pull/7088) | fix(skills): treat only top-level scripts/ paths as executable in skill_manage |
| 2026-10-20 | [PrefectHQ/fastmcp#5672](https://github.com/PrefectHQ/fastmcp/pull/5672) | fix(tools): materialize generator transform_fn results in TransformedTool.run |
| 2026-10-19 | [PrefectHQ/fastmcp#5843](https://github.com/PrefectHQ/fastmcp/pull/5843) | fix(resources): preserve component meta for list[ResourceContent] returns |
| 2026-10-19 | [PrefectHQ/fastmcp#5823](https://github.com/PrefectHQ/fastmcp/pull/5823) | fix: treat non-string skill frontmatter descriptions as absent |
| 2026-10-19 | [mcp-use/mcp-use#2651](https://github.com/mcp-use/mcp-use/pull/2651) | fix(agent): treat missing error field as success in RemoteAgent.run |
| 2026-10-19 | [mcp-use/mcp-use#2551](https://github.com/mcp-use/mcp-use/pull/2551) | fix(agent): emit OpenAI Responses tool-call args events keyed by item_id |
| 2026-10-19 | [strands-agents/harness-sdk#4981](https://github.com/strands-agents/harness-sdk/pull/4981) | fix(ts): report correct paths for values after nested objects in deepCopyWithValidation |
| 2026-10-19 | [livekit/agents#7929](https://github.com/livekit/agents/pull/7929) | fix(cli): apply connect credentials to the agent server |
| 2026-10-18 | [bytedance/deer-flow#6981](https://github.com/bytedance/deer-flow/pull/6981) | fix(memory): filter honcho search by category instead of stamping it on unfiltered results |
| 2026-10-18 | [bytedance/deer-flow#7039](https://github.com/bytedance/deer-flow/pull/7039) | fix(models): tolerate non-mapping when_thinking_enabled.extra_body on the reasoning-contract path |
| 2026-10-17 | [bytedance/deer-flow#7002](https://github.com/bytedance/deer-flow/pull/7002) | fix(sandbox): resolve every entry of colon-joined path lists in forward path translation |
| 2026-10-17 | [livekit/agents#7894](https://github.com/livekit/agents/pull/7894) | fix(llm): drop nonexistent name from __all__ |
| 2026-10-14 | [bytedance/deer-flow#6839](https://github.com/bytedance/deer-flow/pull/6839) | fix(mindie): degrade unserializable tool args to str() in XML replay |
| 2026-10-14 | [bytedance/deer-flow#6838](https://github.com/bytedance/deer-flow/pull/6838) | fix(models): tolerate null template keys in the legacy thinking disable path |
| 2026-10-13 | [livekit/agents#7733](https://github.com/livekit/agents/pull/7733) | fix: split underscore terms in BM25 description and param tokens |
| 2026-10-12 | [bytedance/deer-flow#6732](https://github.com/bytedance/deer-flow/pull/6732) | fix(memory): read the complete scope in the substring search fallback |
| 2026-10-12 | [bytedance/deer-flow#6733](https://github.com/bytedance/deer-flow/pull/6733) | fix(memory): keep non-core fact categories instead of rewriting to other |
| 2026-10-12 | [agentscope-ai/agentscope#3242](https://github.com/agentscope-ai/agentscope/pull/3242) | fix(model): declare real WAV sizes in the final streamed audio block |
| 2026-10-12 | [livekit/agents#7734](https://github.com/livekit/agents/pull/7734) | fix: reference real tool name in ToolProxyToolset description and errors |
| 2026-10-09 | [PrefectHQ/fastmcp#5575](https://github.com/PrefectHQ/fastmcp/pull/5575) | fix: convert version query param to VersionSpec in component manager routes |
| 2026-10-08 | [bytedance/deer-flow#6478](https://github.com/bytedance/deer-flow/pull/6478) | fix(models): keep escaped newlines inside fences in MindIE native stream |
| 2026-10-06 | [Arize-ai/phoenix#16535](https://github.com/Arize-ai/phoenix/pull/16535) | fix(client): keep tools when anthropic tool_choice is none |
| 2026-10-05 | [PrefectHQ/fastmcp#5271](https://github.com/PrefectHQ/fastmcp/pull/5271) | fix(tools): keep structured content for object schemas without explicit type |
| 2026-10-05 | [PrefectHQ/fastmcp#5269](https://github.com/PrefectHQ/fastmcp/pull/5269) | fix(tools): take partial tool names and docstrings from the wrapped function |
| 2026-10-01 | [strands-agents/harness-sdk#4593](https://github.com/strands-agents/harness-sdk/pull/4593) | fix(anthropic): store redacted thinking as bytes and re-encode on send |
| 2026-09-30 | [livekit/agents#7445](https://github.com/livekit/agents/pull/7445) | fix(llm): block unguarded mutations on read-only chat contexts |
| 2026-09-25 | [openai/openai-agents-js#1935](https://github.com/openai/openai-agents-js/pull/1935) | fix(agents-core): handle same-server MCP tool name collisions |
| 2026-09-25 | [bytedance/deer-flow#5861](https://github.com/bytedance/deer-flow/pull/5861) | fix(tools): route bound task and batch tools' sync path through the bound runtime |
| 2026-09-25 | [bytedance/deer-flow#5857](https://github.com/bytedance/deer-flow/pull/5857) | fix(sandbox): list the skills root when only category mounts exist |
| 2026-09-25 | [agno-agi/agno#10554](https://github.com/agno-agi/agno/pull/10554) | fix: store raw video bytes in GeminiTools.generate_video artifact |
| 2026-09-20 | [bytedance/deer-flow#5601](https://github.com/bytedance/deer-flow/pull/5601) | fix(models): tolerate a null Codex account_id before it reaches the request header |
| 2026-09-20 | [bytedance/deer-flow#5591](https://github.com/bytedance/deer-flow/pull/5591) | fix(models): skip Claude credentials sources with a non-numeric expiresAt |
| 2026-09-19 | [bytedance/deer-flow#5584](https://github.com/bytedance/deer-flow/pull/5584) | fix(models): degrade a non-object Codex auth file to no credential |
| 2026-09-18 | [bytedance/deer-flow#5522](https://github.com/bytedance/deer-flow/pull/5522) | fix(mcp): insert bare-filename rewrites literally |
| 2026-09-17 | [bytedance/deer-flow#5509](https://github.com/bytedance/deer-flow/pull/5509) | fix(models): pair Codex invalid tool calls with their tool results |
| 2026-09-16 | [agno-agi/agno#9948](https://github.com/agno-agi/agno/pull/9948) | [fix] keep falsy tool results (0, False, []) on the sync tool execution path |
| 2026-09-15 | [PrefectHQ/fastmcp#5117](https://github.com/PrefectHQ/fastmcp/pull/5117) | fix(local-provider): apply transforms in get_tasks |
| 2026-09-15 | [crewAIInc/crewAI#7487](https://github.com/crewAIInc/crewAI/pull/7487) | fix(azure): key streamed tool calls by wire index |
| 2026-09-14 | [bytedance/deer-flow#5426](https://github.com/bytedance/deer-flow/pull/5426) | fix(mcp): treat a Human Input Card reply as the current user request |
| 2026-09-04 | [bytedance/deer-flow#5164](https://github.com/bytedance/deer-flow/pull/5164) | fix(mcp): keep ToolRuntime injection for sync-wrapped MCP tools |
| 2026-09-03 | [strands-agents/harness-sdk#4139](https://github.com/strands-agents/harness-sdk/pull/4139) | fix(openai): report max_tokens when a Responses function call is cut off |
| 2026-09-02 | [agno-agi/agno#9887](https://github.com/agno-agi/agno/pull/9887) | [fix] Resolve Gemini image MIME type instead of hard-coding image/jpeg |

---

## 三、修补 N = 3

判定标准：补丁确实进入上游，但不是以“本人 PR 被合并”的方式；必须有可核验的采纳证据（commit 作者保留、Co-authored-by、维护者明文写明来源）。

### 3.1 `modelcontextprotocol/servers` · Issue #4827

- 本人 PR：[#4828](https://github.com/modelcontextprotocol/servers/pull/4828)（关闭，未合并，仓库当时只接受 Issue）
- 上游落地：[#5013](https://github.com/modelcontextprotocol/servers/pull/5013)（@cliffhall，已合并）
- 证据：
  - commit [`1b01ea6dac`](https://github.com/modelcontextprotocol/servers/commit/1b01ea6dac44d326013279c2e09d862cc9ede0c9) 的 **author 仍是 BlueX888**；
  - PR #5013 正文写明：**“the first commit is @BlueX888's fix from #4828, cherry-picked with authorship kept”**。

### 3.2 `modelcontextprotocol/servers` · Issue #4813

- 本人 PR：[#4814](https://github.com/modelcontextprotocol/servers/pull/4814)（关闭，未合并）
- 上游落地：[#5036](https://github.com/modelcontextprotocol/servers/pull/5036)（@cliffhall，已合并）
- 证据：
  - PR #5036 正文：**“Ports the fix from #4814 by @BlueX888, with credit (`Co-authored-by` trailer)”**；
  - commit [`b5c5ccc`](https://github.com/modelcontextprotocol/servers/commit/b5c5cccb79a5d43b41247065fb9efd174363e799) 带 `Co-authored-by: BlueX888 <140241684+BlueX888@users.noreply.github.com>`。

### 3.3 `PrefectHQ/fastmcp` · Issue #5866

- 本人 PR：[#5867](https://github.com/PrefectHQ/fastmcp/pull/5867)（关闭，未合并）
- 上游落地：[#6100](https://github.com/PrefectHQ/fastmcp/pull/6100)（@jlowin，已合并）
- 证据：
  - PR #6100 正文末尾带 `Co-authored-by: 哈基米 <140241684+BlueX888@users.noreply.github.com>`；
  - commit [`e54bc65`](https://github.com/PrefectHQ/fastmcp/commit/e54bc65237853f0cd65adbc26de921220eb0b499) 保留该 trailer；
  - issue 讨论中维护者说明修复分支 **“carried forward from the author-closed #5867”**。

> 合计 **3** 项。三项都同时是“本人报告的问题”，但修复代码来自本人补丁，因此在互斥口径下归入“修补”，不再重复计入“问题获修”。

---

## 四、原型被致谢、但未采用本人补丁（2 项，未计入修补）

这两项上游 PR 明文写了“原型来自本人 PR”，但最终实现与本人补丁不同；按“补丁已被采纳”的严格口径 **不计入**，列出来供参考。

| 本人 PR | 上游 PR | 上游原文 | 最终实现 |
|---|---|---|---|
| [servers#4816](https://github.com/modelcontextprotocol/servers/pull/4816) | [servers#5298](https://github.com/modelcontextprotocol/servers/pull/5298) | “The prototype was #4816 by @BlueX888. Thank you.” | 直接删除损坏的 `iCCP` 块，而非修正 8 字节校验和 |
| [servers#4815](https://github.com/modelcontextprotocol/servers/pull/4815) | [servers#5360](https://github.com/modelcontextprotocol/servers/pull/5360) | “Prototype: #4815 by BlueX888 …” | 改为先整体 `rev_parse`、失败再拆分范围，与本人的 `..` 拆分实现不同 |

---

## 五、问题获修 N = 30

判定标准：本人为 Issue 作者；修复由**其他贡献者**完成；Issue 与修复之间有明确关联。关联强度分三档：

- `closing`：修复 PR 含 GitHub 自动关闭关键字（`Fixes/Closes #...`），Issue 被该 PR 自动关闭 —— 最强；
- `addresses`：修复 PR 正文明确写 `Addresses #...`，Issue 由维护者关闭；
- `maintainer`：维护者在 Issue 中明确回复已完成修复，且有对应 commit（无 commit 交叉引用）。

### 5.1 按仓库分布

| 仓库 | 问题获修数 |
|---|---:|
| bytedance/deer-flow | 7 |
| PrefectHQ/fastmcp | 5 |
| mastra-ai/mastra | 4 |
| Fei2411/DS-Bot | 4 |
| Arize-ai/phoenix | 3 |
| agentscope-ai/agentscope | 3 |
| modelcontextprotocol/servers | 3 |
| openai/openai-agents-python | 1 |
| e2b-dev/E2B | 1 |
| openai/openai-agents-js | 1 |
| livekit/agents | 1 |
| **合计** | **33**（含 3 个与修补重叠，去重后 **30**） |

### 5.2 完整清单（29 项 PR 级关联）

| Issue | 标题 | 修复 PR / 作者 | 关联 | 备注 |
|---|---|---|---|---|
| [Arize-ai/phoenix#16228](https://github.com/Arize-ai/phoenix/issues/16228) | [BUG]: Anthropic prompt adapter ignores `{{ variables }}` in str system messages, sending the literal template as the `system` kwarg | [#16316](https://github.com/Arize-ai/phoenix/pull/16316) @Anurag-M1 | closing |  |
| [Arize-ai/phoenix#16950](https://github.com/Arize-ai/phoenix/issues/16950) | [BUG]: [playground] AWS Bedrock run crashes with JSONDecodeError when a tool result message contains plain text | [#16951](https://github.com/Arize-ai/phoenix/pull/16951) @lx3133584 | closing |  |
| [Arize-ai/phoenix#17398](https://github.com/Arize-ai/phoenix/issues/17398) | [BUG]: Span annotation DataFrame logging skips required-column validation that the document path enforces | [#17433](https://github.com/Arize-ai/phoenix/pull/17433) @pcbeingused333 | closing |  |
| [PrefectHQ/fastmcp#5265](https://github.com/PrefectHQ/fastmcp/issues/5265) | CallToolResult.data is None when output_schema has uniqueItems on an array of objects | [#5270](https://github.com/PrefectHQ/fastmcp/pull/5270) @lzyruc | closing |  |
| [PrefectHQ/fastmcp#5816](https://github.com/PrefectHQ/fastmcp/issues/5816) | [Bug] Shared() dependencies become request-scoped without pydocket, and direct call_tool crashes with pydocket | [#5817](https://github.com/PrefectHQ/fastmcp/pull/5817) @HootRock | closing |  |
| [PrefectHQ/fastmcp#5866](https://github.com/PrefectHQ/fastmcp/issues/5866) | [Bug] FastMCPApp treats hash-shaped tool names as pre-addressed, breaking Prefab callbacks after composition | [#6100](https://github.com/PrefectHQ/fastmcp/pull/6100) @jlowin | closing | 同时计入修补 |
| [PrefectHQ/fastmcp#6117](https://github.com/PrefectHQ/fastmcp/issues/6117) | [Bug] FastMCPStdioTransport silently drops its args parameter | [#6119](https://github.com/PrefectHQ/fastmcp/pull/6119) @KashifManzer | closing |  |
| [PrefectHQ/fastmcp#6155](https://github.com/PrefectHQ/fastmcp/issues/6155) | [Bug] A kept-alive stdio transport keeps the first client's session and silently ignores a second client's timeout | [#6156](https://github.com/PrefectHQ/fastmcp/pull/6156) @HootRock | closing |  |
| [agentscope-ai/agentscope#2494](https://github.com/agentscope-ai/agentscope/issues/2494) | [Bug]: AnthropicChatModel streaming merges all `thinking` blocks of one response into a single block, keeping only the last `signature` | [#2495](https://github.com/agentscope-ai/agentscope/pull/2495) @RICARDO51167 | closing |  |
| [agentscope-ai/agentscope#2709](https://github.com/agentscope-ai/agentscope/issues/2709) | [Bug]: Grep: offset/head_limit pagination silently drops and duplicates matches because ripgrep output order is non-deterministic across invocations | [#2726](https://github.com/agentscope-ai/agentscope/pull/2726) @DavdGao | closing |  |
| [agentscope-ai/agentscope#3291](https://github.com/agentscope-ai/agentscope/issues/3291) | [Bug]: Read tool accepts offset <= 0, negative-slicing the file and returning its tail labeled with line numbers 0 or negative | [#3297](https://github.com/agentscope-ai/agentscope/pull/3297) @SSK988I | closing |  |
| [bytedance/deer-flow#5192](https://github.com/bytedance/deer-flow/issues/5192) | [bug] MindIE tool-enabled async streaming drops token usage | [#5195](https://github.com/bytedance/deer-flow/pull/5195) @Coder-xiaosuo | closing |  |
| [bytedance/deer-flow#5473](https://github.com/bytedance/deer-flow/issues/5473) | [bug] Claude credential loader raises AttributeError when ~/.claude/.credentials.json has a non-object claudeAiOauth container | [#5494](https://github.com/bytedance/deer-flow/pull/5494) @cyberspace-cs | closing |  |
| [bytedance/deer-flow#5846](https://github.com/bytedance/deer-flow/issues/5846) | [bug] skill_manage: parallel tool calls for the same (user, skill) deadlock forever on the sync client path (shared asyncio.Lock across per-call event loops) | [#7020](https://github.com/bytedance/deer-flow/pull/7020) @Totoro-qaq | closing |  |
| [bytedance/deer-flow#6471](https://github.com/bytedance/deer-flow/issues/6471) | [bug] DbRunEventStore: delete_by_run lowers the thread's max-seq watermark, so later puts reissue already-used seq values and become invisible to after_seq cursors | [#6477](https://github.com/bytedance/deer-flow/pull/6477) @yu1128-L | closing |  |
| [bytedance/deer-flow#7072](https://github.com/bytedance/deer-flow/issues/7072) | [Bug] Unreadable memory.json is silently overwritten instead of quarantined (data loss) | [#7076](https://github.com/bytedance/deer-flow/pull/7076) @LuckVd | closing |  |
| [bytedance/deer-flow#7077](https://github.com/bytedance/deer-flow/issues/7077) | [Bug] POST /threads/{id}/state silently ignores the checkpoint object and mutates the thread head | [#7115](https://github.com/bytedance/deer-flow/pull/7115) @gmll-star | closing |  |
| [bytedance/deer-flow#7086](https://github.com/bytedance/deer-flow/issues/7086) | [Bug] DeerFlowClient(config_path=...) silently uses the default config, and explicit reloads can be discarded | [#7092](https://github.com/bytedance/deer-flow/pull/7092) @Hugo-DDT | closing |  |
| [e2b-dev/E2B#1895](https://github.com/e2b-dev/E2B/issues/1895) | [Bug]: JS SDK: filesystem watch handle.stop() always fires onExit with a TimeoutError blaming 'requestTimeoutMs' | [#1912](https://github.com/e2b-dev/E2B/pull/1912) @harshitgavita-07; [#1923](https://github.com/e2b-dev/E2B/pull/1923) @devin-ai-integration | closing |  |
| [livekit/agents#7324](https://github.com/livekit/agents/issues/7324) | ChatContext.copy(tools=...) drops FunctionCallOutput with a default (empty) name, silently removing the whole function call + result pair from provider requests | [#7330](https://github.com/livekit/agents/pull/7330) @longcw | addresses |  |
| [mastra-ai/mastra#23980](https://github.com/mastra-ai/mastra/issues/23980) | [BUG] Top-level array structured output silently returns [] for arrays of primitives | [#24055](https://github.com/mastra-ai/mastra/pull/24055) @DanielSLew | closing |  |
| [mastra-ai/mastra#24516](https://github.com/mastra-ai/mastra/issues/24516) | [BUG] schema-compat/zodToJsonSchema: nullable zod v4 enum/literal widens to type:[X,"null"] but keeps enum/const, so exported schema rejects null | [#25086](https://github.com/mastra-ai/mastra/pull/25086) @breken-ai | closing |  |
| [mastra-ai/mastra#25208](https://github.com/mastra-ai/mastra/issues/25208) | [BUG] Array structured output textStream/elementStream keep the stale partial element when a later chunk completes it in place | [#25278](https://github.com/mastra-ai/mastra/pull/25278) @mastra-platform | closing |  |
| [mastra-ai/mastra#26481](https://github.com/mastra-ai/mastra/issues/26481) | [BUG] MCP image/audio tool results emitted as spec-v3 `image-data`/`file-data` in the v5 tool-result output — dropped by spec-v2 providers, rejected by spec-v4 (Bedrock throws) | [#26662](https://github.com/mastra-ai/mastra/pull/26662) @mastra-platform | closing |  |
| [modelcontextprotocol/servers#4808](https://github.com/modelcontextprotocol/servers/issues/4808) | everything: session resources evict another session's resource when two sessions use the same file name | [#5032](https://github.com/modelcontextprotocol/servers/pull/5032) @cliffhall | closing |  |
| [modelcontextprotocol/servers#4813](https://github.com/modelcontextprotocol/servers/issues/4813) | sequentialthinking: a branchId that collides with an Object.prototype key throws instead of creating the branch, and the failed call still extends thoughtHistory | [#5036](https://github.com/modelcontextprotocol/servers/pull/5036) @cliffhall | closing | 同时计入修补 |
| [modelcontextprotocol/servers#4827](https://github.com/modelcontextprotocol/servers/issues/4827) | server-memory: saveGraph rewrites memory.jsonl via temp-file + rename, dropping an existing file's permission bits (0600 -> 0644) and silently overwriting read-only files | [#5013](https://github.com/modelcontextprotocol/servers/pull/5013) @cliffhall | closing | 同时计入修补 |
| [openai/openai-agents-js#1976](https://github.com/openai/openai-agents-js/issues/1976) | MCP tool cache: invalidating server 'X' deletes the cached tools of an unrelated server named 'X:suffix' via the unscoped prefix-scan fallback | [#1977](https://github.com/openai/openai-agents-js/pull/1977) @jbeckwith-oai | closing |  |
| [openai/openai-agents-python#5348](https://github.com/openai/openai-agents-python/issues/5348) | ShellTool: empty ShellResult(output=[]) fabricates stdout "(no output)" in the model-visible shell_call_output and persisted shell_output | [#5423](https://github.com/openai/openai-agents-python/pull/5423) @jbeckwith-oai | closing |  |

### 5.3 维护者确认、但无 commit 交叉引用的 4 项（`Fei2411/DS-Bot`）

| Issue | 问题 | 对应修复 commit | 关联证据 |
|---|---|---|---|
| [Fei2411/DS-Bot#55](https://github.com/Fei2411/DS-Bot/issues/55) | dev/mock-llm.mjs 的 `长任务 N` 省略 K 时每一步都不产出文本块（`.map(Number)` 把缺失的 K 变成 NaN） | [`d9af38d`](https://github.com/Fei2411/DS-Bot/commit/d9af38d58a96bb59fa01fdc5d1f2f7fc944d0a7b) | 维护者在 issue 中回复「已完成修复」 |
| [Fei2411/DS-Bot#56](https://github.com/Fei2411/DS-Bot/issues/56) | `state.lock` 被另一台 host 接管后，写端点仍返回 ok:true 但 `save()` 静默失败 | [`7018a8b`](https://github.com/Fei2411/DS-Bot/commit/7018a8becec06c50d0d4b9ad4cccc5679487c12e) | 维护者在 issue 中回复「已完成修复」 |
| [Fei2411/DS-Bot#57](https://github.com/Fei2411/DS-Bot/issues/57) | 删除 Bot / 群聊后其定时任务成为孤儿：仍在 DSH 中待命，设置页不可见也无法删除 | [`2ceba39`](https://github.com/Fei2411/DS-Bot/commit/2ceba39a80927969e84b3615dc34564dd8ede46b) | 维护者在 issue 中回复「已完成修复」 |
| [Fei2411/DS-Bot#58](https://github.com/Fei2411/DS-Bot/issues/58) | Node 22 下 web-search 慢端点超时永不触发（`AbortSignal.timeout` 的 unref 定时器） | [`d9af38d`](https://github.com/Fei2411/DS-Bot/commit/d9af38d58a96bb59fa01fdc5d1f2f7fc944d0a7b) | 维护者在 issue 中回复「已完成修复」 |

> 这 4 个 issue 由维护者 @Fei2411 在 issue 中回复「已完成修复」并关闭；对应 commit 的标题与改动和本人给出的根因一一对应，但 commit message 没有引用 issue 编号，因此单列为 `maintainer` 档。若只接受 PR/commit 级引用，问题获修为 **29**（不去重）/ **26**（与修补去重）。

---

## 六、排除项与易混淆情况

| 项目 | 结论 | 原因 |
|---|---|---|
| `livekit/agents#7431` | 不计入问题获修 | 维护者 @longcw 明确回复 “The count is intentional”，认为不是 bug，随后关闭 |
| `bytedance/deer-flow#5589` | 不计入问题获修 | 该问题最终由**本人** PR [#5591](https://github.com/bytedance/deer-flow/pull/5591) 修复；PR 未写 closing 关键字，但已计入“合并 44” |
| `agno-agi/agno#10550` / `#9947` | 不计入问题获修 | 分别由本人 PR #10554 / #9948 修复，已计入“合并 44” |
| `openai/openai-agents-python#5053` | 不计入 | 维护者认为该用法不受支持，按“非 bug”关闭，无修复 |
| `openai/openai-agents-python#5041` | 不计入 | 对应修复 PR #5042 已关闭且未合并 |
| `PrefectHQ/fastmcp#6117` | 计为问题获修，不计为修补 | PR #6119 的 commit 带本人 Co-authored-by，但正文明确写 “Thanks to @BlueX888 for **reporting** this issue”；修复代码由其他贡献者准备，采纳证据不足 |
| `mcp-use/mcp-use#2878`（Canary） | 不计为修补 | 该 commit 带本人 Co-authored-by，但这是聚合发布 PR，内容包含本人已合并的 #2551 / #2651，属于派生而非独立采纳 |
| 本人仓库内 149 个已合并 PR | 不计入 | 非上游仓库 |
| 本人 204 个 Issue 中仍开启 / 由本人 PR 修复的部分 | 不计入问题获修 | 不满足“由其他贡献者完成修复” |

---

## 七、统计方法与可复现性

1. **PR**：GitHub Search `is:pr author:BlueX888 is:merged`，逐条读取 `repository_url`、`merged_at`，剔除 owner 为 `BlueX888` 的仓库 → 44。
2. **Issue**：GitHub Search `is:issue author:BlueX888` → 204；GraphQL 读取每个 Issue 的 `closedByPullRequestsReferences`、`CrossReferencedEvent`、`stateReason`，再逐条核对修复 PR 作者与仓库。
3. **Commit（修补）**：
   - `author:BlueX888` 的 commit 共 237 条（含 fork 中的副本）；去重并限定 12 个上游仓库后为 43 条；
   - 对每条 commit 查 `associatedPullRequests`：42 条属于本人已合并 PR，仅 `modelcontextprotocol/servers@1b01ea6dac` 属于他人 PR（#5013）→ 第 1 项修补；
   - 搜索带本人姓名 / noreply 邮箱的 `Co-authored-by` trailer，命中上游 commit 3 个：servers `b5c5ccc`（#5036）、fastmcp `e54bc65`（#6100）、fastmcp `baf255c`（#6119）→ 前两项为修补，第三项按上表排除；
   - 逐仓库搜索合并 PR 正文中的 `BlueX888`，补充发现 servers #5298 / #5360 的“原型致谢”，因未采用补丁单列。
4. **局限**：
   - 仅覆盖公开仓库，无法统计私有仓库 / 组织内仓库；
   - GitHub Search 存在索引延迟，刚合并的 PR / Issue 可能尚未计入；
   - 无作者或 co-author 署名、且维护者未在正文致谢的“静默采纳”无法举证，按“必须有采纳证据”的要求不计入；
   - 统计时点之后发生的合并、关闭、重开不会反映在本文件中。

---

## 八、一句话版本

- **合并 44**：以本人为作者、被 11 个上游仓库正式合并的 PR。
- **修补 3**：`modelcontextprotocol/servers` 2 项（#4827、#4813）+ `PrefectHQ/fastmcp` 1 项（#5866），补丁被他人 PR 采纳且有 commit / co-author 证据。
- **问题获修 30**：29 个 PR/commit 级关联（含 3 个与修补重叠）− 3 个重叠 + 4 个维护者确认的 DS-Bot issue。只算 PR/commit 级引用且与修补去重为 **26**；不去重为 **33**。
