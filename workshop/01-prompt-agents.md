# Prompt agents: build two complementary specialists

Build two independently publishable Microsoft Foundry Prompt Agents. The
**Weather Research Agent** owns weather evidence. The **Cultural Travel Agent**
owns published art-tourism, museum, and cultural-trip evidence, including only
the accessibility information its sources actually supply.
Each follows the same seven-step learning progression so the second agent
reinforces the method rather than introducing a compressed shortcut.

Keep reproducible definitions and test clients under `student/prompt-agents/`.
Use current supported APIs and isolated dependencies, not the old root pins.
The coach pauses after each change and asks for a teach-back before advancing.
Use [TESTS.md](TESTS.md) and introduce the related
[app technique](APP-GUIDE.md) at each checkpoint.

Use the [mixed test plan](APP-GUIDE.md#where-tests-and-exploration-happen)
throughout both specialists, aiming for 50/50 coach-sent and participant-sent
test prompts across each specialist's lessons: the coach demonstrates from the Copilot app, then
the participant copies a prompt into the exact agent's Foundry Playground,
sends it once, and brings the actual result back for review. Allocate remaining
required tests between the routes, tracking the running split rather than
adding duplicate calls. Explain and record capability or participant-preference
exceptions to the target. Keep
controlled identity, failure, and consumer-endpoint checks on a supported client
when the Playground cannot supply the required evidence. Agree on each handoff,
its context, cost, and tool approvals before sending.

For both specialists, the coach supplies the selected server URL, actual tool
schemas, and configuration plan from [MCP-SERVICES.md](MCP-SERVICES.md).
Participants do not research endpoints, supply keys, or deploy MCP servers.
Use the same explain, approve, configure, test, inspect, and teach-back loop
for each. The shared New York trip develops into the two-agent workflow only
after both agents pass independently; do not jump ahead to orchestration.

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
Have the coach demonstrate B01, then guide the participant to send B02 and B03
in separate fresh Conversations and copy each reply back to the Copilot app.

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
Let the participant send at least one matched before/after prompt pair, with
the same input and fresh context on both versions; use the coach route for the
remaining comparisons. Plan the before-run before creating the candidate; if
it is already complete, reuse that evidence instead of repeating it for practice.

**App practice:** review the focused instruction diff before creating the version.
**Alternative:** request an instruction proposal without applying it.
**Teach-back:** "Which behavior changed, and what evidence ties it to the instructions?"

## 03: Test Weather managed Conversations

**Concept:** Microsoft Foundry automatically maintains history within one
Conversation identifier. Persistent memory is a separate capability.

**Before the tests:** verify the
[portal trace prerequisite](SETUP.md#portal-trace-prerequisite), including the
project's Application Insights connection and the participant's telemetry-read
access. Conversation history does not depend on this portal trace setup.
If tracing is unavailable, explain the blocker; preserve any completed
Conversation tests and inspect their service-returned evidence without claiming
the portal exercise passed. Do not connect resources or repeat paid tests
without separate approval.

In one Conversation, provide a destination and weather interest, then ask a
follow-up that relies on that context. In a new Conversation, ask the follow-up
again. Follow the [rehearsed navigation](APP-GUIDE.md#foundry-navigation-rehearsed-before-the-workshop):
**Build → Agents → the exact agent → Traces**. Use **Trace view** to find
a response and inspect its relevant span's **Metadata**, and **Conversation
view** to locate a saved Conversation (`conv_`). Explain that the Response
ID (`resp_`) identifies one reply, not the conversation, and the Trace ID
identifies its execution record. Fields vary by span; use a supported client
to verify identifier linkage when it is not exposed. Do not infer linkage
from a similar-looking reply or adjacent table row.
Do not build a custom history store or manually replay messages.

Run D01-D02 with weather-appropriate prompts. The application remains
responsible for mapping an authorized user/session to the correct Conversation
identifier. A GitHub Copilot app session is not a runtime Conversation.
Prefer participant-run messages for the complete sequence when the Playground
supports the required Conversation behavior and identifier evidence; otherwise
demonstrate with the supported client without claiming a UI feature exists.

**App practice:** contrast the coaching session with both runtime Conversations.
**Alternative:** discuss when a separate app session helps isolate another task.
**Teach-back:** "What did Microsoft Foundry manage, and what remains the client's responsibility?"

## 04: Connect the first Weather MCP tool

**Concept:** connect one remote evidence tool, prove its execution, and learn
the difference between a plausible answer and observed runtime evidence.

The coach provides the public **Weather MCP server** endpoint
`https://weather.datakoot.com/mcp` and discovers its current schemas without
credentials. Explain `weather_forecast` and its required numeric `lat` and
`lon` inputs; optional `hourly=false` selects daily periods. Use the first-tool
configuration and coverage guidance in [MCP-SERVICES.md](MCP-SERVICES.md).
After approval, connect only that tool to the Weather Agent's new candidate,
keep tool-call approval required, and independently read back the definition.
Do not ask the participant to supply server details or host a service.
Verify Foundry-side execution rather than assuming local discovery proves it.

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

Recheck the selected server's current schemas. Separately approve expansion
from `weather_forecast` to these four Weather MCP tools:

- `geocode` for supplied US addresses or city names;
- `weather_forecast` for future weather within the returned forecast horizon;
- `weather_current` for current station observations; and
- `weather_alerts` for relevant official US state alerts.

The coach supplies the verified inputs from MCP-SERVICES.md and guides the
allowlist change; other discovered tools remain excluded. Do not invent
coordinates or claim non-US weather coverage.

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
Repeat the demonstration/practice split: coach sends B01; participant sends B02
and B03 and brings each reply back, rather than making agent 2 coach-only.

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

Recheck the [portal trace prerequisite](SETUP.md#portal-trace-prerequisite) for
this project's current connection and inspection identity before the tests.
The Weather Agent's successful tracing exercise is not proof of trace access
for another project or identity.

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

Repeat the checkpoint 04 coaching behavior for agent 2. The coach provides
the public **travel.art MCP server** endpoint `https://mcp.travel.art/`,
discovers its current schemas without credentials, and explains
`find_museum_guide` and its optional `query`, `city`, and `country` filters.
Use [MCP-SERVICES.md](MCP-SERVICES.md), including the exact first-tool definition
and copy-ready New York museum prompt. Do not ask the participant to find an
endpoint, obtain a key, register a Cloudflare account, or deploy a server.

After approval, attach only `find_museum_guide` to this agent's new candidate,
retain tool-call approval, and independently read back the definition. Do not
change the released Weather Agent or attach its tools to Cultural Travel.
The source is travel.art's published museum guides, not live ticket inventory
or an official venue verification service.

Run C02 for a supported destination and C03 for unsupported or malformed input.
Inspect the MCP Server Endpoint, tool schema, arguments, result, `guideUrl`,
available `lastVerified` metadata, attribution, and grounded response. Do not
require an invented dataset version. Reuse the trace-inspection knowledge
from checkpoint 04: verify the tool span and result without repeating the full
navigation lesson unless the participant needs it.

**App practice:** inspect agent 2's runtime connection and one-tool allowlist.
**Alternative:** inspect a sanitized direct MCP response before the agent call.
**Teach-back:** "What proves the museum-guide tool supplied the attributed facts?"

## 12: Guide multiple Cultural tools with a skill

**Concept:** repeat skill-guided tool routing in a new evidence domain.

The coach supplies the live schemas and separately requests approval to expand
to the four selected travel.art tools: `find_museum_guide`, `find_art_events`,
`find_layover_itinerary`, and `recommend_art_trip`. See MCP-SERVICES.md for
their exact filters, date formats, catalogue limits, and source fields.
There is no standalone accessibility or etiquette tool.

Create a versioned cultural-research skill that guides which tool to use, in
what order, when not to call one, how to preserve guide attribution/freshness,
and how to expose partial failures. A provider-supplied cultural itinerary is
not our hosted workflow and contains no Weather Agent execution evidence.

The skill must distinguish missing accessibility information from proof that a
venue is accessible or inaccessible. If museum retrieval succeeds while an
event lookup fails, preserve the grounded museum guidance and report the event
failure. If accessibility information is absent from the returned guides,
state that it is unavailable; do not invent a separate retrieval.

Run S02 across museum lookup, art events, covered layovers, cultural trip
recommendations, missing accessibility information, unrelated-tool restraint,
and partial-failure cases. Use separate requests to exercise tool roles rather
than calling all four for every question.

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

Memory supplies the preference; travel.art MCP tools supply the published
museum, event, or cultural-trip facts. Do not store an unnecessary reason that
could reveal sensitive information.

**App practice:** pause, resume, and recheck the exact agent and memory scope.
**Alternative:** explain why a stateless design would be safer when memory adds no value.
**Teach-back:** "Which evidence came from memory, and which came from the MCP tools?"

## 14: Release the Cultural Travel Agent

**Concept:** the second specialist must independently pass the same release
discipline before orchestration begins.

Run the complete Cultural Agent regression suite. Verify its exact version,
skill revision, travel.art tool allowlist, memory configuration, source
attribution, and freshness caveats. Promote only a fully passing candidate to
its own Stable Agent Endpoint and run P01-P03.

Invoke both stable specialists independently for the same destination. The
Weather Research Agent must not claim cultural retrieval; the Cultural Travel
Agent must not claim weather retrieval. Record both names, versions, endpoints,
identities, tool connections, skill revisions, memory scopes, and release
evidence.

**App practice:** request a two-agent handoff table backed by live metadata.
**Alternative:** inspect sanitized raw responses from both endpoints.
**Teach-back:** "Why must both agents pass independently before workflow code is added?"
