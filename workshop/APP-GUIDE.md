# Learn the Copilot app while building agents

This is a companion to every lesson, not a separate product tour. Practice one
app technique when it becomes useful. The coach should show a primary approach,
briefly compare an alternative, and let the student choose. Do not introduce
several new UI concepts while also debugging an agent.

App features depend on build, policy, and available tools. Inspect what is
actually exposed. Never invent buttons, keyboard shortcuts, slash commands,
custom-agent selectors, or Canvas actions. The example prompts below work in
the selected Workshop Coach session, or normal repository Chat when the app
has no agent selector. Do not confuse that entry fallback with optional visual
alternatives later in the lessons.

## Techniques to introduce along the way

| Checkpoints | Primary approach to practice | Useful alternative and tradeoff |
|-------------|-----------------------------|--------------------------------|
| 00 | Select Workshop Coach in the GitHub Copilot app, send "Start the workshop", then try "Explain without editing." | If the app has no selector, use normal repository Chat with the same prompt and protocol |
| 01, 08 | "Explain this agent definition before editing it." Then explicitly request the small change | Ask for a proposed diff first to retain more control; direct implementation is faster for a clear, bounded task |
| 02 | Review the focused instruction diff and compare the same test before and after | Ask for an instruction proposal without applying it; this keeps analysis separate from version creation |
| 03, 10 | Keep this coaching session; create a separate runtime conversation for the agent test | Use a new app session for an independent task, but supply the relevant files/brief; do not assume it inherits chat history |
| 04, 12 | Inspect the actual registered tools, MCP server, and caller/runtime for each result | Compare MCP configured for Copilot with MCP configured for Foundry; the former helps the developer, the latter helps the application |
| 05, 13 | Review the skill diff and exact version/delivery strategy before changing the active agent | Use a file/editor panel if available, or ask Chat to show a focused diff; reading an artifact is not evidence it was deployed |
| 06, 10 | "Pause and save my progress." Then "Resume and recheck my target." | A new app session can read progress in the same checkout; a new worktree needs an approved progress import |
| 07, 14 | "Show the endpoint, selected version, and actual test results; don't infer success." | Use supported Foundry Canvas controls for hosted operations when available; return to Chat for teaching and failure diagnosis |
| 09 | "Show the tool name, validated arguments, result, and which hosted process executed it." | Read raw sanitized tool output or a test result when the app has no visual trace view |
| 11 | "Propose a two-step workflow and its tests. Do not implement yet." | Use Plan mode if exposed; a planning-only Chat request teaches the same separation without it |
| 15 | Write a brief with scope, non-goals, tests, and cost boundaries before building | Choose a preset capstone to reduce design decisions, or propose a custom scenario with equivalent criteria |
| 16 | "Change only this function and run these tests." Review the resulting diff | Use an isolated branch/worktree for a larger experiment; first verify which source and local evidence it contains |
| 17 | Ask for a handoff with verified endpoints, versions, limitations, and owned resources | Compare that handoff with a live demonstration; neither a commit nor a deployment command's exit code proves behavior |

## Teach control, not just prompting

**Request types:** explanation is read-only; a plan is a proposal; implementation
changes artifacts; execution can affect live resources. Teach students to state
which they want. "Show another way" is not approval to execute both alternatives.

**Changes:** review the proposed scope and resulting diff. Committing saves
source history, but does not deploy it. Pushing shares source, not the student's
local `.workshop/` evidence. Never silently commit or publish student work.

**Tool permissions:** the app's permission prompt controls what Copilot may do.
It is distinct from the deployed agent's tool approval, Azure RBAC, memory
scope, and the consumer's access. Approving a shell command does not authorize
every future cloud mutation.

**Sessions:** a Copilot app session, a worktree, a Foundry conversation, and a
memory store are four different things. A new runtime conversation can be
tested from the same coaching session. A new app session does not prove memory
is persistent in Foundry. Reusing a worktree also does not automatically share
app conversation history.

**Context:** point the coach at the relevant file or error rather than pasting
an entire environment dump. Ask it to separate observed evidence from guesses.
Do not paste credentials, secrets, or personal data.

**Alternatives:** use a direct SDK/CLI operation when it gives a needed,
inspectable result and no suitable app integration exists. Use the installed
Foundry skill when available. Prefer the smallest supported path; comparing
approaches does not mean installing extra extensions or provisioning duplicates.

## Optional visual surfaces

When an appropriate surface is actually available, the coach can use an editor
for an artifact, a terminal for a process the student should watch, or the
browser for a relevant preview. The core path does not require these surfaces.

Foundry Canvas is for supported hosted-agent operations under the app's routing
rules. Prompt-agent creation, explanation, troubleshooting, and mixed tasks
remain in Chat. Never route a teaching question into a deployment. A Canvas
handoff is not success evidence; return to the learning gate after the action.

## App learning evidence

At each checkpoint, record a brief `app_practice` object in the local attempt:
the technique used, the alternative discussed, and the student's explanation of
when to use it. A Chat equivalent is sufficient if a UI feature is unavailable.
Do not record full app transcripts or screenshots containing sensitive details.
