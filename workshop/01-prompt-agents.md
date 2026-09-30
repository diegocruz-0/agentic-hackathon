# Prompt agents: the original six steps

Follow the original samples' concept order with small, neutral exercises.
Do not choose a business scenario yet. Use [TESTS.md](TESTS.md) and introduce
the related [app technique](APP-GUIDE.md) at each checkpoint.

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

## 02: Add tools

**Concept:** the model requests a function; another component executes it.
Reference [add tools](../01-agent-framework/02_add_tools.py).

Use the sample's weather idea, but make the new exercise deterministic:
`get_weather("Seattle")` returns a labeled fixture with `condition: sunny`,
`temperature_c: 20`, and `source: workshop-fixture`. An unknown location returns
an explicit unsupported-location result; blank input is a validation error.
Never present this synthetic data as a live weather service.

For a prompt agent, define the supported function schema and implement execution
in the local test client. Inspect each function-call argument, dispatch only
allowlisted functions, validate inputs, and return the result using the matching
call ID and supported continuation protocol. Bound the tool loop and report
errors; do not evaluate arbitrary model-generated code.

The Python decorator in the original Agent Framework sample is not a drop-in
prompt-agent registration API. Confirm the current function-calling contract.
Run T01-T03 directly and through the actual Foundry agent. Inspect execution,
not just the assistant's text. This is real tool execution with synthetic data.

**App practice:** inspect tool name, arguments, result, and execution location.
**Alternative:** inspect sanitized client logs when no trace viewer exists.
**Teach-back:** "Who actually ran the function: the model, the service, or our client?"

Later, a supported built-in tool can be compared as an optional extension.
Do not replace the original function-calling lesson with search-only behavior.

## 03: Multi-turn conversations

**Concept:** conversation history persists across requests to the same
conversation, not automatically across every invocation.
Reference [multi-turn](../01-agent-framework/03_multi_turn.py) and the
[Foundry chat example](../02-microsoft-foundry-agents/03-quickstart-chat-with-agent.py).

In a conversation, say "My name is Alice and I love hiking." Ask what the agent
remembers. Then start a new conversation without replaying that history.
Run D01-D02 and record the actual conversation identifiers. Persistent memory
has not been configured, so the new conversation should not know that fact.
Do not interpret the coach's own recall as evidence about the Foundry agent.

**App practice:** contrast the current Copilot session with both runtime
conversations, without creating a second coaching session unnecessarily.
**Alternative:** discuss when a fresh app session helps isolate a separate task.
**Teach-back:** "Which conversation contained Alice's name, and why?"

## 04: Memory and context

**Concept:** injected context, conversation history, and durable memory differ.
Reference [context provider](../01-agent-framework/04_memory.py): it keeps a
name in a Python object, not a persistent multi-user memory store.

First inspect that reference and predict what happens when the process restarts.
Then add a real student-owned Foundry memory store using the
[current memory guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage).
Check chat/embedding deployments, permissions, supported API, and cost approval.
Allow only synthetic style/language preferences, with agreed retention.

Configure both retrieval and the documented write/remember path. Map memory
scope from trusted identity, not an ID asserted in a chat message. A static test
scope is acceptable only in an explicitly isolated synthetic harness.
Run M01-M03: recall in a new conversation, different-user isolation, and forget.
Confirm the update completes before checking recall; report a bounded timeout.

Keep the earlier D02 no-memory observation as historical evidence. After adding
memory, use fresh empty test scopes to distinguish deliberate recall from leaks.

**App practice:** save and resume workshop progress; identify where it is stored.
**Alternative:** discuss how a new app session could read that progress in the
same checkout, while a different worktree needs an approved import.
**Teach-back:** "Which state survives a new conversation, and where is it stored?"

## 05: First workflow

**Concept:** explicit execution order instead of one large prompt.
Reference [first workflow](../01-agent-framework/05_first_workflow.py).

Begin with its two deterministic steps: uppercase text, then reverse it.
Predict and verify that `hello world` becomes `DLROW OLLEH`. Inspect both steps.
Run the local part of W01 before adding a model call.

Next, let the local client run that deterministic workflow and ask the Foundry
prompt agent to explain its output. Verify both the deterministic result and the
actual remote response. Fail a step in an isolated test and run W02; do not
report a final result or call the next step after failure.

This is **client-side orchestration around a prompt agent**, not a deployed
Foundry workflow or custom code running inside a prompt definition. The hosted
phase will move execution into the runtime. Do not assume a visual Foundry
workflow builder is available or needed.

**App practice:** ask for a plan and expected outputs before implementation.
**Alternative:** use Plan mode if exposed; otherwise use a planning-only Chat
request. Neither is approval for resource changes.
**Teach-back:** "Which parts are deterministic, and where do they execute?"

## 06: Remote MCP

**Concept:** discover and call external tools through a standard protocol.
Reference [remote MCP](../01-agent-framework/06_remote_mcp.py).

Use a facilitator-approved read-only documentation service, such as the
Microsoft Learn MCP endpoint documented in the
[Foundry MCP guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol).
Discover real schemas; configure only needed read-only tools and authentication/
approval behavior. Attach it to the student's Foundry agent, not just Copilot.

Ask a public documentation question and run C01. Inspect the discovery,
invocation, result, and grounding. Handle approval requests with the documented
continuation if required. Run C02 for decline/error behavior in an isolated test;
never disable approvals globally to get a green result.

**App practice:** compare Copilot's registered tools with the runtime's tool
configuration. Similar names do not mean they are the same connection.
**Alternative:** compare a supported direct SDK client with an available app
integration, without executing both or adding duplicate resources.
**Teach-back:** "Where does the MCP server run, and which agent is its client?"

## 07: Refine instructions and work with skills

**Concept:** use test evidence to improve instructions, then extract a reusable
procedure. This extends the original sequence rather than replacing its steps.

Review the weather and documentation responses. Make one instruction change,
such as the headings `Answer`, `Source`, and `Uncertainty`. Run I01 with the
same inputs before and after the new version. Do not change the model at the
same time or fabricate a source for a general-knowledge answer.

Author `student/skills/explain-results/SKILL.md` with that procedure and a useful
trigger description. Require clear separation of fixture data, retrieved
evidence, and uncertainty. Upload a student-owned skill version and retrieve it
using the [current skills guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills).
Run S01 against the retrieved version and its resulting agent behavior.

For the portable prompt path, incorporate the reviewed skill content at build
time into a new agent instruction version. Label this **static composition**.
A skill uploaded to Foundry is not automatically loaded by the prompt runtime.
Toolbox skills use MCP resources, not just tools; verify runtime support before
claiming dynamic use. Hosted runtime loading is taught at 14.

Keep trust boundaries and authorization outside skills. Record the exact source
skill version; do not silently follow an untested shared default.

**App practice:** review the instruction and skill diff and explain the scope
of changes to the coach versus the runtime.
**Alternative:** use an editor panel if available or request a focused Chat diff.
**Teach-back:** "When does a skill update reach this agent, and what does it not control?"

## 08: Release the prompt agent

Follow [PUBLISHING.md](PUBLISHING.md). The consumer test client must support the
function-call loop from 02; the endpoint alone does not host that function.
Document the workflow's client-side location as well.

**App practice:** request endpoint/version metadata and observed test evidence.
**Alternative:** inspect sanitized raw responses instead of a narrative summary.
**Teach-back:** "What must a consumer implement, and what does Foundry manage?"
