# Workshop map

**First time here?** Follow [Start here](START.md), select **Workshop Coach**
in the GitHub Copilot app, then type **"Start the workshop."** Use normal
repository Chat only as the fallback when the app has no agent selector.

The coach runs in the **Copilot app**; the student's agents run in **Foundry**.
Learn both, one small change at a time. Changing the coach's instructions,
memory, skills, or MCP connections does not configure the deployed agent.

## Learning sequence

| Concept/reference | Prompt-agent lesson | Hosted-agent lesson |
|-------------------|---------------------|---------------------|
| `01_hello_agent.py` | 01: model, instructions, first response | 08: code, local host, remote runtime |
| Instruction refinement | 02: evidence-driven agent version | Reused throughout hosted versions |
| `03_multi_turn.py` | 03: observe and test Foundry-managed conversation boundaries | 10a: hosted sessions |
| `06_remote_mcp.py` | 04: connect one remote MCP, then two | 12: hosted MCP integrations |
| Skills | 05: version and statically compose a reviewed skill | 13: runtime skill loading |
| `04_memory.py` | 06: context vs persistent memory store | 10b: durable memory across host restarts |
| `02_add_tools.py` | Deferred: prompt agents do not package its Python function | 09: function implementation inside hosted runtime |
| `05_first_workflow.py` | Deferred: prompt agents do not package code workflows | 11: workflow inside hosted runtime |

The original examples remain concept references, but the live path now keeps
the prompt-agent phase publishable without a separate local executor. Custom
function code and deterministic workflow execution begin when students build a
hosted runtime. Memory extends the original in-process context example into a
real persistent store.

## Checkpoints

| ID | Lesson | Required test evidence | App practice |
|----|--------|------------------------|--------------|
| 00 | [Setup](SETUP.md) | Access, model lookup, ownership, capability inventory | Repo context and approvals |
| 01 | [Hello agent](01-prompt-agents.md#01-hello-agent) | B01-B03 | Explain vs implement |
| 02 | [Refine instructions](01-prompt-agents.md#02-refine-instructions) | I01 | Review a focused instruction diff |
| 03 | [Managed conversations](01-prompt-agents.md#03-observe-and-test-managed-conversations) | D01-D02 | App session vs runtime conversation |
| 04 | [One MCP, then two](01-prompt-agents.md#04-connect-one-remote-mcp-then-two) | C01-C03 | Compare coach and agent MCP connections |
| 05 | [Skills](01-prompt-agents.md#05-work-with-skills) | S01 | Review skill version and delivery strategy |
| 06 | [Memory](01-prompt-agents.md#06-add-and-test-persistent-memory) | M01-M03 | Save/resume vs agent memory |
| 07 | [Prompt release](PUBLISHING.md) | P01-P03 | Ask for evidence, not a completion claim |
| 08 | [Hosted hello agent](02-hosted-agents.md#08-hosted-hello-agent) | B01-B03 locally and remotely | Inspect scaffold; Chat vs supported Canvas |
| 09 | [Hosted tools](02-hosted-agents.md#09-hosted-tools) | T01-T03 locally and remotely | Read tests and narrowly scoped edits |
| 10 | [Hosted conversations and memory](02-hosted-agents.md#10-hosted-conversations-then-memory) | D01-D02, M01-M03 after restart | Reuse context vs a separate session |
| 11 | [Hosted workflow](02-hosted-agents.md#11-hosted-workflow) | W01-W02 remotely | Diagnose from logs and reproducible input |
| 12 | [Hosted MCP](02-hosted-agents.md#12-hosted-remote-mcp) | C01-C03 remotely | Inspect runtime and server boundaries |
| 13 | [Runtime skills](02-hosted-agents.md#13-hosted-runtime-skills) | I01, S01-S02 | Version review and change isolation |
| 14 | [Hosted release](PUBLISHING.md) | P01-P04 | Review endpoint version changes and rollback |
| 15 | [Choose a capstone](CAPSTONE.md#15-choose-and-scope) | K01 | Turn an idea into a bounded plan |
| 16 | [Build incrementally](CAPSTONE.md#16-build-and-test) | K02 and applicable regressions | Small tasks, diff review, focused debugging |
| 17 | [Release and demonstrate](CAPSTONE.md#17-release-and-demonstrate) | K03, P01-P04 | Handoff with evidence and cleanup choices |

Each checkpoint depends on the preceding checkpoint. Where a checkpoint has
substeps, test and pause between them. Do not scaffold the final project in the
first lesson. Capstone selection happens at 15, not during setup.

Each lesson also has an **App practice** and **Alternative**. Try the primary
approach and explain when the alternative is useful; repeating the whole lesson
is unnecessary. See [APP-GUIDE.md](APP-GUIDE.md) for examples and UI fallbacks.

## Student controls

| Say | Coach behavior |
|-----|----------------|
| "Start the workshop" | Begin 00; one question at a time |
| "Resume the workshop" | Recheck local progress and the target, then continue |
| "Give me a hint" | Explain the smallest missing idea without solving future steps |
| "Explain, don't edit" | Inspect and teach without modifying files or resources |
| "Help me implement this step" | Make only the current agreed change |
| "Show another way" | Compare a relevant alternative and its tradeoff |
| "Test this checkpoint" | Execute the current tests and applicable regressions |
| "Show my progress" | Show passed, failed, blocked, and not-started gates |
| "Pause the workshop" | Save progress; leave cloud resources unchanged |
| "Clean up" | List exact owned targets and ask before stopping/deleting |

## Completion

All required checkpoints must pass, with observed test evidence and student
teach-back. A compatible alternative app interaction can satisfy app practice;
an unavailable UI control must not block the course. An unavailable required
Foundry capability does block its integration checkpoint.

An explicitly approved partial route stays labeled incomplete. The facilitator
can review evidence the coach cannot verify; the coach is not an independent
examiner or a certification service. Follow [FACILITATOR.md](FACILITATOR.md) for
cohort preparation and rehearsal.
