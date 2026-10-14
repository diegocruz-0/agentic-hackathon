# Prompt agents: managed capabilities first

Build a publishable Foundry prompt agent using capabilities that Foundry can
manage or reach after release. Custom executable Python functions and explicit
code workflows are reserved for the hosted-agent phase. Do not choose a business
scenario yet. Use [TESTS.md](TESTS.md) and introduce the related
[app technique](APP-GUIDE.md) at each checkpoint.

Keep a reproducible definition and test client in `student/prompt-agent/`.
Use current supported APIs and isolated dependencies, not the old root pins.
The coach pauses after each change and asks for a teach-back before advancing.

## 01: Hello agent

**Concept:** a deployed model plus instructions creates a prompt agent.
Reference [hello agent](../01-agent-framework/01_hello_agent.py) for the idea
and [create-agent](../02-microsoft-foundry-agents/02-quickstart-create-agent.py)
for the prompt-agent pattern.

Ask the student to predict a minimal friendly assistant's answer to "What is
the capital of France?" Draft brief instructions: answer clearly, ask when
context is missing, and do not claim capabilities or access you do not have.
No tools, persistent memory, or scenario-specific policy yet.

After approval, create a uniquely named Foundry prompt agent using the installed
skill or the [current quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent).
Record its actual name/version. Invoke without creating another version just
to chat. Run B01-B03. Compare one complete response with streaming output if
supported, explaining that output delivery does not change the agent's abilities.

**App practice:** ask "Explain, don't edit," then separately request the change.
**Alternative:** ask for a proposed diff before accepting implementation.
**Teach-back:** "What defines this agent, and what has not been added yet?"

## 02: Refine instructions

**Concept:** improve a prompt agent through one evidence-driven instruction
change while holding the model and capabilities constant.

Review the baseline responses from 01. Add a small, measurable response contract,
such as the headings `Answer`, `Source`, and `Uncertainty`. Explain what belongs
under each heading and prohibit invented sources or capabilities. Create a new
agent version rather than silently changing the tested version.

Run I01 with the same inputs before and after the instruction change. Inspect
the actual version metadata and responses. Do not change the model, add tools,
or introduce a business scenario at the same time; otherwise the student cannot
attribute the observed difference to the instructions.

**App practice:** review the focused instruction diff before creating the version.
**Alternative:** ask the coach to propose the instruction change without applying it.
**Teach-back:** "Which observed behavior changed, and what evidence ties it to the instructions?"

## 03: Observe and test managed conversations

**Concept:** Foundry automatically maintains history inside a conversation.
The student highlights and tests that managed behavior rather than implementing
conversation storage. The application still decides when to continue an
authorized conversation and when to start a new one.
Reference [multi-turn](../01-agent-framework/03_multi_turn.py) and the
[Foundry chat example](../02-microsoft-foundry-agents/03-quickstart-chat-with-agent.py).

First use the Foundry playground. Say "My name is Alice and I love hiking",
then ask what the agent remembers in the same playground conversation. Explain
that Foundry created and maintained this conversation automatically; no student
conversation-store implementation is required.

Start a fresh playground conversation and ask the same follow-up. It should not
know Alice's facts. Then use the supported SDK/API only to make the boundary
observable: capture conversation A's identifier, reuse it for the two related
turns, and create conversation B for the clean-context test. Do not build a
custom history store, manually replay messages, or add persistent memory here.

Run D01-D02 and record the actual identifiers where exposed. The UI observation
demonstrates the experience; the identifiers prove whether the same or a fresh
Foundry conversation was used. Persistent memory has not been configured, so
conversation B must not know Alice's facts. Do not interpret the coach's own
recall as evidence about the Foundry agent.

**App practice:** contrast the current Copilot session with both runtime
conversations, without creating a second coaching session unnecessarily.
**Alternative:** discuss when a fresh app session helps isolate a separate task.
**Teach-back:** "What did Foundry manage automatically, and what decision remains
the client application's responsibility?"

## 04: Connect one remote MCP, then two

**Concept:** first understand one remote tool boundary, then test selection and
provenance when a prompt agent can use two independent MCP servers.
Reference [remote MCP](../01-agent-framework/06_remote_mcp.py) for the concept.

**First MCP:** connect the facilitator-approved, Foundry-reachable, read-only
weather MCP with a narrow allowlist. Discover its actual schemas, data source,
and approval requirements; do not assume it is live weather or reuse the old
random local function. Ask one supported weather question. Run C01 and inspect
discovery, selected tool, arguments, result, source, and the grounded response.

**Second MCP:** after the first integration passes, connect the approved
read-only cultural-travel MCP. Run C02 using one weather question, one cultural
travel question, and one request that makes the correct server choice observable.
Evidence must identify the server and tool used for each result; similar tool
names are not sufficient provenance. Do not turn this neutral integration
exercise into the capstone travel scenario.

Run C03 by declining an approval where configured or injecting a controlled
failure in one integration. The agent must expose the limitation rather than
claiming a successful lookup or silently treating the other MCP server as an
equivalent source. Never disable approvals globally to make the test pass.

Use current [Foundry MCP guidance](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol).
Attach both connections to the Foundry agent, not merely to the Copilot coach.

**App practice:** compare Copilot's MCP registrations with both agent runtime
connections and inspect which server handled each request.
**Alternative:** compare direct agent configuration with a supported Toolbox
only when useful; do not add duplicate connections for demonstration.
**Teach-back:** "How did you prove which MCP server supplied each result?"

## 05: Work with skills

**Concept:** package a reviewed procedure for reuse and make its delivery to the
prompt agent explicit.

Author `student/skills/explain-results/SKILL.md` with that procedure and a useful
trigger description. Require clear separation of general knowledge, evidence
retrieved from each MCP server, and uncertainty. It can also define how future
fixture data must be labeled without claiming such a fixture exists yet.
Upload a student-owned skill version and retrieve it
using the [current skills guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills).
Run S01 against the retrieved version and its resulting agent behavior.

For the portable prompt path, incorporate the reviewed skill content at build
time into a new agent instruction version. Label this **static composition**.
A skill uploaded to Foundry is not automatically loaded by the prompt runtime.
Toolbox skills use MCP resources, not just tools; verify runtime support before
claiming dynamic use. Hosted runtime loading is taught at 13.

Keep trust boundaries and authorization outside skills. Record the exact source
skill version; do not silently follow an untested shared default.

**App practice:** review the instruction and skill diff and explain the scope
of changes to the coach versus the runtime.
**Alternative:** use an editor panel if available or request a focused Chat diff.
**Teach-back:** "When does a skill update reach this agent, and what does it not control?"

## 06: Add and test persistent memory

**Concept:** injected context, conversation history, and durable memory differ.
Memory is added after the agent has useful instructions, remote capabilities,
and a reusable skill so the student can see what long-term personalization
changes—and what it must not silently change.
Reference [context provider](../01-agent-framework/04_memory.py): it keeps a
name in a Python object, not a persistent multi-user memory store.

First return to the observation from 03: a fresh conversation did not remember
Alice. Predict what would happen if the original Python process restarted.
Then add a real student-owned Foundry memory store using the
[current memory guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage).
Check chat/embedding deployments, permissions, supported API, and cost approval.
Allow only synthetic style/language preferences, with agreed retention.

Configure both retrieval and the documented write/remember path. Map memory
scope from trusted identity, not an ID asserted in a chat message. A static test
scope is acceptable only in an explicitly isolated synthetic harness.
Run M01-M03: recall in a new conversation, different-user isolation, explicit
current-request override, and forget. Confirm updates complete before checking
recall and report a bounded timeout.

Keep the earlier D02 no-memory observation as historical evidence. After adding
memory, use fresh empty test scopes to distinguish deliberate recall from leaks.
Re-run one MCP and skill-formatted response to prove memory personalizes style
without changing tool selection, provenance, authorization, or factual results.

**App practice:** save and resume workshop progress; identify where it is stored.
**Alternative:** discuss how a new app session could read that progress in the
same checkout, while a different worktree needs an approved import.
**Teach-back:** "What changed across a fresh conversation, and which agent
capabilities remained independent of memory?"

## 07: Release the prompt agent

Follow [PUBLISHING.md](PUBLISHING.md). Release the tested agent version with its
instructions, managed conversations, two approved MCP connections, reviewed
skill-delivery strategy, and memory configuration. No local Python function or
client-side workflow is part of this prompt-agent release.

**App practice:** request endpoint/version metadata and observed test evidence.
**Alternative:** inspect sanitized raw responses instead of a narrative summary.
**Teach-back:** "What does the released endpoint manage, and which access or
connection responsibilities still remain?"
