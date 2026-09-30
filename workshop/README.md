# Workshop map

**First time here?** Follow [Start here](START.md), then type **"Start the
workshop"** in a normal repository Chat session. No agent selector is required.

The coach runs in the **Copilot app**; the student's agents run in **Foundry**.
Learn both, one small change at a time. Changing the coach's instructions,
memory, skills, or MCP connections does not configure the deployed agent.

## Follow the original concept sequence

| Original sample | Prompt-agent lesson | Hosted-agent lesson |
|-----------------|---------------------|---------------------|
| `01_hello_agent.py` | 01: model, instructions, first response | 09: code, local host, remote runtime |
| `02_add_tools.py` | 02: function schema and client-side execution | 10: function implementation inside hosted runtime |
| `03_multi_turn.py` | 03: conversation history | 11a: hosted sessions |
| `04_memory.py` | 04: context vs persistent memory store | 11b: durable memory across host restarts |
| `05_first_workflow.py` | 05: local deterministic graph, then client orchestration | 12: workflow inside hosted runtime |
| `06_remote_mcp.py` | 06: remote documentation tools | 13: hosted MCP integration |

This preserves the old learning order, not every old command. Function execution
for a prompt agent requires a client; it is not code magically running in the
Foundry prompt service. The first workflow is local/client-side orchestration,
not a claimed Foundry workflow deployment. Memory extends the original
in-process context example into a real persistent store.

## Checkpoints

| ID | Lesson | Required test evidence | App practice |
|----|--------|------------------------|--------------|
| 00 | [Setup](SETUP.md) | Access, model lookup, ownership, capability inventory | Repo context and approvals |
| 01 | [Hello agent](01-prompt-agents.md#01-hello-agent) | B01-B03 | Explain vs implement |
| 02 | [Tools](01-prompt-agents.md#02-add-tools) | T01-T03 | Read a tool call and review a diff |
| 03 | [Multi-turn](01-prompt-agents.md#03-multi-turn-conversations) | D01-D02 | App session vs runtime conversation |
| 04 | [Memory](01-prompt-agents.md#04-memory-and-context) | M01-M03 | Save/resume vs agent memory |
| 05 | [Workflow](01-prompt-agents.md#05-first-workflow) | W01-W02 | Plan before executing |
| 06 | [Remote MCP](01-prompt-agents.md#06-remote-mcp) | C01-C02 | Coach tools vs deployed tools |
| 07 | [Instructions and skills](01-prompt-agents.md#07-refine-instructions-and-work-with-skills) | I01, S01 | Review instructions vs reusable skills |
| 08 | [Prompt release](PUBLISHING.md) | P01-P03 | Ask for evidence, not a completion claim |
| 09 | [Hosted hello agent](02-hosted-agents.md#09-hosted-hello-agent) | B01-B03 locally and remotely | Inspect scaffold; Chat vs supported Canvas |
| 10 | [Hosted tools](02-hosted-agents.md#10-hosted-tools) | T01-T03 locally and remotely | Read tests and narrowly scoped edits |
| 11 | [Hosted conversations and memory](02-hosted-agents.md#11-hosted-conversations-then-memory) | D01-D02, M01-M03 after restart | Reuse context vs a separate session |
| 12 | [Hosted workflow](02-hosted-agents.md#12-hosted-workflow) | W01-W02 remotely | Diagnose from logs and reproducible input |
| 13 | [Hosted MCP](02-hosted-agents.md#13-hosted-remote-mcp) | C01-C02 remotely | Inspect runtime and server boundaries |
| 14 | [Runtime skills](02-hosted-agents.md#14-hosted-runtime-skills) | I01, S01-S02 | Version review and change isolation |
| 15 | [Hosted release](PUBLISHING.md) | P01-P04 | Review endpoint version changes and rollback |
| 16 | [Choose a capstone](CAPSTONE.md#16-choose-and-scope) | K01 | Turn an idea into a bounded plan |
| 17 | [Build incrementally](CAPSTONE.md#17-build-and-test) | K02 and applicable regressions | Small tasks, diff review, focused debugging |
| 18 | [Release and demonstrate](CAPSTONE.md#18-release-and-demonstrate) | K03, P01-P04 | Handoff with evidence and cleanup choices |

Each checkpoint depends on the preceding checkpoint. Where a checkpoint has
substeps, test and pause between them. Do not scaffold the final project in the
first lesson. Capstone selection happens at 16, not during setup.

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
