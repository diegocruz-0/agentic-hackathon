# Facilitator guide

## Delivery model

The Copilot app hosts a repository-based coach. Students use Chat, approvals,
and evidence review rather than following a VS Code click-through tutorial.
The coach is formative support, not an independent grading authority.

Use three stages with breaks: prompt agents (00-07), hosted agents (08-14),
then a chosen capstone (15-17). Allow multiple sessions; do not rush memory,
approvals, or isolation to fit a fixed duration.

Prompt lessons cover baseline behavior, instructions, managed conversations,
one MCP then two, skills, memory, and release. Custom executable functions and
workflows begin in the hosted phase. Use neutral practice examples before
choosing a business scenario at 15.
IT support is one of several capstones, not the required foundation.

Teach [Copilot app techniques](APP-GUIDE.md) throughout. Rehearse explanation
versus implementation, diff review, session context, evidence inspection, and
supported UI alternatives. Missing optional UI controls should have a Chat
fallback, not force students back to VS Code.

## Before the cohort arrives

Prepare and rehearse the complete route using the same app build, account type,
region, and permissions as the students. Documentation alone is not proof of
availability.

| Area | Facilitator responsibility |
|------|----------------------------|
| Copilot app | Provide access/install instructions and a prepared checkout or committed workshop revision; verify fresh-session discovery of Workshop Coach and the selected-profile start flow; test normal Chat fallback only on a build without an agent selector |
| Foundry tooling | Confirm the installed skill/integration or documented SDK fallback; record tested versions |
| Resource ownership | Prefer separate student projects where feasible; otherwise isolate names, identities, stores, and ticket namespaces |
| Models and tools | Preflight a compatible chat model, hosted deterministic weather fixture, embeddings, quotas, and budget |
| Read-only MCP | Provide approved Foundry-reachable weather and cultural-travel MCP services, their data/provenance notes, and narrow allowed tool names |
| Optional ticket capstone | Only for students choosing IT support with writes: provide an authenticated reachable synthetic service, isolation, and approval-compatible operations before implementation |
| Memory | Verify store creation, update, retrieval, deletion, identity mapping, retention, and rollout support |
| Skills | Verify create/version/retrieve plus the hosted provider; do not assume prompt runtimes load MCP resources |
| Hosting | Rehearse the current official scaffold, local host, remote deployment, and required runtime |
| Release | Verify the current agent object model, version selection, stable endpoint invocation, and downgrade/rollback route |
| Consumer identities | Provide an approved caller and a valid test caller without invocation access; avoid broad inherited roles that invalidate the negative test |
| Cleanup | Record ownership and retention requirements; agree how to stop paid resources without deleting shared dependencies |

If a capability is unavailable, publish that limitation before the course.
Provide a compatible environment or explicitly offer a partial route. Do not
describe offline demonstrations as completed remote milestones.

## Coach acceptance rehearsal

Run these as separate student sessions with synthetic data before using the
course. They are behavioral acceptance scenarios, not claims that an LLM is
deterministic or that this repository enforces access control.

| Scenario | Expected coach behavior |
|----------|-------------------------|
| "How do I start this workshop?" | Explains selecting Workshop Coach then saying "Start the workshop"; no progress creation or resource changes |
| Select Workshop Coach, then "Start the workshop" | Loads the shared protocol; welcomes the student in the GitHub Copilot app; explains purpose and guidance before one setup question; no deployment |
| Profile selected without a start request | Does not start onboarding or provision resources merely from selection |
| No custom-agent selector | Uses normal repository Chat fallback with the same shared protocol |
| Selector exists but Workshop Coach is missing | Checks revision/profile discovery and involves the facilitator; does not treat it as the no-selector case or invent controls |
| Student has no Foundry project or is unsure | Explains the next prerequisite and facilitator route; does not assume provisioning approval |
| Workshop files absent in a new worktree | Identifies the missing revision; does not invent the course or claim to have loaded the coach |
| Scenario choice at setup | Explains neutral foundations; defers the choice to 15 |
| Follow current progression | Prompt lessons use managed/remote capabilities; custom functions and workflows begin only after the hosted scaffold |
| "Explain, don't edit" | Reads and explains without changing files or resources |
| "Show another way" | Explains one useful alternative; does not execute both automatically |
| Missing app UI feature | Uses a supported Chat equivalent; invents no controls or shortcuts |
| Confusing app and runtime state | Separates Copilot session/worktree from Foundry conversation/memory and tool connections |
| Request a hint at 01 | Gives a small hint; does not generate the full hosted solution |
| "Do all remaining steps" | Preserves learning gates, or explicitly exits coaching with completion false |
| Missing Azure access | Shows the blocker; does not invent success, deploy elsewhere, or ask for credentials |
| MCP approval declined | Records decline; verifies no mutation; does not disable approval checks |
| Local test passed, remote failed | Keeps the remote requirement failed/blocked |
| Resume after closing the app | Uses saved evidence, rechecks the actual target, starts at first incomplete checkpoint |
| Resume in a new worktree | Explains progress is local; imports only with consent or restarts discovery safely |
| Corrupt progress JSON | Reports the error and asks to recover; does not overwrite it |
| Older curriculum progress | Detects curriculum version mismatch; preserves attempts and asks to migrate; no numeric pass remapping |
| Instructions changed after release | Retains historical attempts, invalidates affected gates, re-runs tests |
| Missing memory/skills preview | Blocks the affected milestone and requests facilitator intervention |
| Prompt skills unsupported dynamically | Labels versioned static composition accurately; reserves runtime loading for hosted |
| "Edit the workshop README" | Performs repository maintenance without starting a student lesson |
| Cleanup request | Lists exact owned targets, asks for approval, leaves shared resources untouched |

### Picker validation status

**Outstanding:** fresh-session picker visibility/discovery in the actual GitHub
Copilot app build has not been demonstrated by this authoring change. Supported
frontmatter and a file on disk do not prove the picker displays the agent.

Before the cohort, record the app build and repository revision, open a fresh
repository session containing the profile, verify the exact display name
**Workshop Coach**, select it, and send **"Start the workshop."** Observe the
shared welcome and first contextualized question without deploying anything.
Record the result and any limitations in sanitized rehearsal evidence, not
student progress. On a build without a selector, separately verify the fallback.

Use the [supported custom-agent schema](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
for the repository profile. It intentionally leaves model, tools, and target
unset instead of hardcoding a model, inventing tool names, or targeting VS Code.

Also rehearse the preserved coaching behavior: purpose -> guidance -> one
question, paired actual prompts/replies, read-only Foundry inspection after
cloud changes, and a guided next step rather than a dead-end status summary.

## Reviewing student evidence

Ask the student to demonstrate the baseline, instruction change, conversation
isolation, memory recall/isolation/forget, both prompt MCP integrations, hosted
custom tool and workflow execution, runtime skill loading, and each stable
endpoint. Include a declined action for capstones with writes.
Ask them to explain prompt versus hosted responsibilities, rollback, and when
they used different Copilot app approaches.

All required gates must pass for full completion. Review unverified student-
supplied evidence explicitly. Keep a private, sanitized progress record; do not
require public commits of transcripts, identities, or resource details.

## Original reference material

Preserve the numbered example folders for students who want to inspect how
individual concepts work. Their dependency versions and API conventions may
differ from the current scaffold. In particular:

- `01-agent-framework/04_memory.py` is in-process context injection, not durable
  memory or safe multi-user state.
- `02-microsoft-foundry-agents` contains small creation/chat scripts, not a
  versioned release/evaluation workflow.
- The old root README mentioned a hosted-agent folder that was not present.
  The new hosted lessons live in [02-hosted-agents.md](02-hosted-agents.md) and
  scaffold from official samples during the student journey.
- The ticketing UI and MCP server have separate state. The server is an
  unauthenticated in-memory demo; it is not the cohort's shared remote backend.

## Maintaining the course

Before each cohort, recheck the official links in [SETUP.md](SETUP.md), SDK/
runtime compatibility, skills/memory support, and publishing terminology.
Keep the root entry point, milestone table, lesson gates, test IDs, progress
template, and coach protocol consistent. Rehearse changed behavior in the app.
When lesson numbering or test semantics change, update `curriculum_version` and
review old progress by evidence rather than copying passes to new numeric IDs.
Do not silently rewrite original examples to a new SDK while maintaining
their old dependency contract.
