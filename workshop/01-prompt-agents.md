# Prompt agents: build two complementary specialists

Build two independently publishable Microsoft Foundry Prompt Agents. The
**Weather Research Agent** owns weather evidence. The **Cultural Travel Agent**
owns curated destination, cultural, attraction, and accessibility evidence.
Each follows the same seven-step learning progression so the second agent
reinforces the method rather than introducing a compressed shortcut.

Keep reproducible definitions and test clients under `student/prompt-agents/`.
Use current supported APIs and isolated dependencies, not the old root pins.
The coach pauses after each change and asks for a teach-back before advancing.
Use [TESTS.md](TESTS.md) and introduce the related
[app technique](APP-GUIDE.md) at each checkpoint.

## 01: Create the Weather Research Agent

**Concept:** a Microsoft Foundry Model Deployment plus instructions creates a
Microsoft Foundry Prompt Agent.

Create a minimal Weather Research Agent without tools, persistent memory, or a
skill. It can explain stable weather concepts from trained model knowledge, but
it must not claim current weather without an external source. Ask when location
or time context is missing and do not claim access the agent does not have.

After approval, create a uniquely named agent using the installed skill or the
[current quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent).
Record its actual name/version and run B01-B03 with weather-appropriate inputs.

**App practice:** ask "Explain, don't edit," then separately request the change.
**Alternative:** ask for a proposed definition diff before implementation.
**Teach-back:** "What defines this agent, and what has not been added yet?"

## 02: Refine Weather instructions

**Concept:** improve one measurable behavior while holding the model and
capabilities constant.

Add headings such as `Answer`, `Source`, and `Uncertainty`. Require general
knowledge to be labeled accurately and prohibit invented sources, current
weather claims, or unsupported capabilities. Create a candidate version rather
than silently changing the tested version.

Run I01 with the same inputs before and after the change. Inspect the actual
version metadata and responses. Do not change the Microsoft Foundry Model
Deployment or add tools at the same time.

**App practice:** review the focused instruction diff before creating the version.
**Alternative:** request an instruction proposal without applying it.
**Teach-back:** "Which behavior changed, and what evidence ties it to the instructions?"

## 03: Test Weather managed Conversations

**Concept:** Microsoft Foundry automatically maintains history within one
Conversation identifier. Persistent memory is a separate capability.

In one Conversation, provide a destination and weather interest, then ask a
follow-up that relies on that context. In a new Conversation, ask the follow-up
again. In the Playground, open the trace window for each relevant response and
inspect its details for the Conversation ID (`conv_`). Explain that the Response
ID (`resp_`) identifies one reply, not the conversation. Use a supported client
to verify the identifier linkage when available.
Do not build a custom history store or manually replay messages.

Run D01-D02 with weather-appropriate prompts. The application remains
responsible for mapping an authorized user/session to the correct Conversation
identifier. A GitHub Copilot app session is not a runtime Conversation.

**App practice:** contrast the coaching session with both runtime Conversations.
**Alternative:** discuss when a separate app session helps isolate another task.
**Teach-back:** "What did Microsoft Foundry manage, and what remains the client's responsibility?"

## 04: Connect the first Weather MCP tool

**Concept:** connect one remote evidence tool, prove its execution, and learn
the difference between a plausible answer and observed runtime evidence.

Connect the facilitator-provided, Microsoft Foundry-reachable, read-only
**Weather MCP server** and allowlist only its verified forecast tool, such as
`get_forecast`. Discover the actual MCP Server Endpoint, schema, upstream source,
fixture/live-data labeling, and limits. Do not invent a tool name if the server
exposes a different one.

Run C01 with a supported location and C03 with invalid input or an isolated
upstream failure. For the first successful MCP call in the workshop, guide the
participant through Microsoft Foundry trace inspection. Locate the forecast
tool span and inspect its arguments, status, timing, returned source/timestamp,
and relationship to the final response. The agent must report failure rather
than invent weather.

Registering an MCP server for the GitHub Copilot app does not attach it to the
Microsoft Foundry agent. Never disable approvals globally to make a test pass.

**App practice:** compare Copilot's MCP registrations with the agent's runtime connection.
**Alternative:** inspect a sanitized direct MCP response before the agent call.
**Teach-back:** "Which trace evidence proves the forecast tool supplied the result?"

## 05: Guide multiple Weather tools with a skill

**Concept:** a skill can guide how an agent selects and sequences already
available tools; it does not connect tools or grant authorization.

Expand the allowlist only with verified Weather MCP server tools. Example roles,
when the live server actually supports them, include:

- `resolve_location` for ambiguous place names;
- `get_forecast` for future weather;
- `get_current_conditions` for current observations; and
- `get_weather_alerts` for relevant official alerts.

Author a versioned weather-research skill under `student/skills/`. It should
guide input validation, tool selection, ordering, restraint, provenance,
partial failures, and stopping when prerequisite evidence is missing. For
example, resolve an ambiguous location before requesting its forecast, but do
not call every weather tool for every question.

Use the supported prompt-agent skill-delivery mechanism. If the environment
requires reviewed static composition, label it accurately; do not claim dynamic
loading. Run S01 across targeted, ambiguous, general-knowledge, and controlled
failure cases. Inspect traces to verify the chosen tool sequence, but checkpoint
04 remains the full trace-navigation lesson.

Formal machine-readable result contracts are intentionally deferred until
checkpoint 15, when workflow code needs to validate two agent results.

**App practice:** review the skill diff, exact version, delivery strategy, and allowlist change.
**Alternative:** validate the procedure against recorded fixtures before a paid call.
**Teach-back:** "How can a skill guide tool use without granting access?"

## 06: Add and test Weather memory

**Concept:** managed Conversation history and persistent memory solve different
problems.

Add a student-owned persistent-memory capability using the
[current memory guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage).
Use a low-risk, explicitly consented preference such as Celsius temperature
units. Store only the minimum useful fact, map scope from trusted identity, and
support inspection, correction, and deletion.

Run M01-M03 with weather-appropriate preferences. In a new Conversation, memory
may supply the preferred unit while Weather MCP tools still supply current
weather evidence. A retrieval failure must not become a false claim that the
preference was remembered.

Re-run one MCP and skill-guided response to prove memory personalizes
presentation without changing tool authorization, provenance, or factual data.

**App practice:** save and resume workshop progress; identify where it is stored.
**Alternative:** discuss progress import into another worktree without confusing it with agent memory.
**Teach-back:** "What came from memory, and what still had to come from the Weather MCP server?"

## 07: Release the Weather Research Agent

**Concept:** release selects a fully tested candidate behind a Stable Agent
Endpoint. A known-failing candidate is never promoted as the stable release.

Follow [PUBLISHING.md](PUBLISHING.md). Run the complete Weather Agent regression
suite, verify its exact agent version, skill revision, tool allowlist, memory
configuration, and Microsoft Foundry Model Deployment, then run P01-P03 through
the Stable Agent Endpoint.

The released agent returns a consistent evidence-aware weather briefing with
destination, dates, findings, tool/source provenance, timestamps, uncertainty,
and missing information. It does not provide cultural recommendations or a
complete itinerary.

Retain failed candidate test evidence for diagnosis, but keep that candidate
out of stable routing. Rollback is reserved for an unforeseen issue discovered
after a fully passing version was promoted.

**App practice:** request endpoint/version metadata and observed test evidence.
**Alternative:** inspect sanitized raw responses instead of a narrative summary.
**Teach-back:** "Why can only a fully passing candidate become the stable release?"

## 08: Create the Cultural Travel Agent

**Concept:** the second specialist repeats the same lifecycle with a different
evidence responsibility.

Create a separate Cultural Travel Agent without tools, memory, or copied Weather
Agent state. It may answer stable, general cultural questions while labeling
them as general knowledge. It must not claim current opening hours,
accessibility conditions, event schedules, prices, or weather without evidence.
Run B01-B03 with cultural-travel inputs.

**App practice:** compare the two minimal agent definitions.
**Alternative:** request a proposed definition before implementation.
**Teach-back:** "What is independent about agent 2, and what has not been added?"

## 09: Refine Cultural instructions

**Concept:** improve the second specialist through the same controlled
instruction-version comparison.

Add `Guidance`, `Source`, and `Uncertainty` headings. Require respectful language,
stereotype avoidance, missing-context questions, and clear separation between
general knowledge and current venue-specific evidence. Keep the Microsoft
Foundry Model Deployment and capabilities unchanged. Run I01.

**App practice:** review the focused instruction diff and matched tests.
**Alternative:** keep the change proposal-only until expectations are clear.
**Teach-back:** "What can this tool-free version explain, and what can it not verify?"

## 10: Test Cultural managed Conversations

**Concept:** repeat Conversation continuity and isolation for the second agent.

Within one Conversation, state a destination and interest, then ask a follow-up.
In a new Conversation, verify that the destination is not imported
automatically. Run D01-D02 with cultural-travel prompts.

The Cultural Travel Agent has its own authorized Conversation mapping. It
cannot read the Weather Research Agent's Conversation history.

**App practice:** keep one coaching session while testing separate runtime Conversations.
**Alternative:** use a separate app session only for a genuinely separate task.
**Teach-back:** "Why does a new Cultural Agent Conversation ask for context again?"

## 11: Connect the first Cultural Travel MCP tool

**Concept:** connect one curated cultural-evidence tool before introducing
multi-tool routing.

Connect the facilitator-owned authless **Cloudflare Cultural Travel MCP server**
and allowlist one verified tool, such as `get_attractions`. The Worker must use
a versioned, licensed or synthetic curated dataset and expose no arbitrary URL
fetching, writes, secrets, or unrestricted web search.

Run C02 for a supported destination and C03 for unsupported or malformed input.
Inspect the MCP Server Endpoint, tool schema, arguments, dataset version,
result, attribution, and grounded response. Reuse the trace-inspection knowledge
from checkpoint 04: verify the tool span and result without repeating the full
navigation lesson unless the participant needs it.

**App practice:** inspect agent 2's runtime connection and one-tool allowlist.
**Alternative:** inspect a sanitized direct MCP response before the agent call.
**Teach-back:** "What proves the curated dataset supplied the attraction facts?"

## 12: Guide multiple Cultural tools with a skill

**Concept:** repeat skill-guided tool routing in a new evidence domain.

Expand the allowlist only with verified tools, such as `search_destinations`,
`get_attractions`, `get_cultural_guidance`, and `get_accessibility_notes`.
Create a versioned cultural-research skill that guides which tool to use, in
what order, when not to call a tool, how to preserve dataset provenance, and
how to expose partial failures.

The skill must distinguish missing accessibility information from proof that a
venue is accessible or inaccessible. If attraction retrieval succeeds while
accessibility retrieval fails, preserve the grounded attraction evidence and
state that accessibility evidence is unavailable.

Run S02 across destination search, attraction, etiquette, accessibility,
unrelated-tool restraint, and partial-failure cases.

**App practice:** review the skill and allowlist diffs separately.
**Alternative:** validate recorded tool results before live agent calls.
**Teach-back:** "How did the skill choose only the tools needed for this request?"

## 13: Add and test Cultural memory

**Concept:** repeat the persistent-memory lifecycle with an independent,
low-risk cultural preference.

Use a preference such as museums over nightlife. Obtain consent, store the
minimum fact, inspect its scope, verify retrieval in a new Conversation, correct
it, delete it, and prove the deleted value is no longer applied. Run M01-M03
against the Cultural Agent's separately approved memory scope.

Memory supplies the preference; Cloudflare Cultural Travel MCP tools supply the
curated attraction or guidance facts. Do not store an unnecessary reason that
could reveal sensitive information.

**App practice:** pause, resume, and recheck the exact agent and memory scope.
**Alternative:** explain why a stateless design would be safer when memory adds no value.
**Teach-back:** "Which evidence came from memory, and which came from the MCP tools?"

## 14: Release the Cultural Travel Agent

**Concept:** the second specialist must independently pass the same release
discipline before orchestration begins.

Run the complete Cultural Agent regression suite. Verify its exact version,
skill revision, Cloudflare tool allowlist, memory configuration, and dataset
expectations. Promote only a fully passing candidate to its own Stable Agent
Endpoint and run P01-P03.

Invoke both stable specialists independently for the same destination. The
Weather Research Agent must not claim cultural retrieval; the Cultural Travel
Agent must not claim weather retrieval. Record both names, versions, endpoints,
identities, tool connections, skill revisions, memory scopes, and release
evidence.

**App practice:** request a two-agent handoff table backed by live metadata.
**Alternative:** inspect sanitized raw responses from both endpoints.
**Teach-back:** "Why must both agents pass independently before workflow code is added?"
