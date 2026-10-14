# Apply the concepts to a scenario of your choice

Choose a capstone only after the foundational prompt and hosted lessons.
**IT support is one option, not the default journey.** The coach helps scope
the work; it does not generate a complete solution before the student makes
design choices and predicts behavior.

## 15: Choose and scope

| Option | Possible outcome | Boundaries and additional prerequisites |
|--------|------------------|----------------------------------------|
| IT support assistant | Explain incidents, retrieve documentation, and manage synthetic tickets | An authenticated, Foundry-reachable, student-isolated test service for writes; no production incidents |
| Documentation research assistant | Search approved public sources and produce an evidence-backed brief | Approved read-only MCP source; cite retrieved evidence and expose uncertainty |
| Fictional travel-planning assistant | Compare synthetic itineraries using tools and remember style preferences | Synthetic fixture data only; no real booking, payment, or live-weather claims |
| Student-proposed scenario | A narrowly scoped useful agent | Facilitator-approved data/tools/costs and the same acceptance criteria |

Ask one question at a time: scenario, user/task, desired output, non-goals, then
architecture. Leave `scenario` null until the student chooses here. If a student
mentions an idea earlier, record it as a candidate, not a committed course theme.

Create a short source-controlled brief under `student/capstone/` containing:
the user need, expected behavior, exclusions, prompt or hosted choice and why,
approved MCP sources, conversation behavior, memory scope and retention,
reusable skill and delivery strategy, tests, cost boundary, and release target.
For a hosted architecture, also define the custom function and workflow
contracts. Use public/synthetic fixtures.

A prompt implementation uses Foundry-managed or remote capabilities and does
not claim to package custom Python functions or code workflows. A hosted
implementation can own custom executable functions and workflows in its runtime.
Neither choice automatically implies better quality.
Keep the two practice releases unchanged for comparison.

Run K01: the student explains the design and every resource/data boundary is
explicit. Agree on concrete tests before implementation.

**App practice:** ask for a plan with non-goals and acceptance criteria, without
authorizing execution.
**Alternative:** select a preset scenario to reduce design decisions or bring a
custom idea with equivalent tests.
**Teach-back:** "Why is this agent type appropriate, and what will you not build?"

## 16: Build and test

Apply the concepts appropriate to the selected architecture. Every capstone
must cover baseline behavior, instruction refinement, conversation boundaries,
scoped memory, approved remote MCP integrations, skill delivery, and release
evidence. A hosted capstone must additionally cover a custom function and an
explicit executable workflow. Reuse reviewed components, not old progress
passes. Pause and test at every addition.

The prompt architecture is not failed for omitting custom executable code it
cannot package. The hosted architecture must prove that its function and
workflow execute inside the deployed runtime. Both architectures require two
approved MCP connections unless the facilitator records why one is unavailable
and explicitly approves a partial route. A read-only capstone is fully valid.
Do not introduce writes just to make the project look more advanced.

For each concept, adapt the corresponding test inputs in TESTS.md and record
the exact inputs/expected results in the capstone brief. Preserve test IDs for
traceability. Choose deterministic fixtures and do not compare exact prose
unless the requirement specifies a format.

Any mutation requires an enforced authorization/approval mechanism, not just
instructions. Demonstrate decline/no mutation and approved mutation, plus
invalid input and not-found behavior. Verify state independently. Run A01-A02
only for capstones with writes; record the reviewed non-applicability for
read-only designs. Never silently skip a test for an implemented capability.

Run K02 after all required capability tests pass on the actual selected target.
Keep failures visible and regression-test each integration.

**App practice:** give Copilot one bounded task, inspect its diff and evidence,
then ask a focused debugging question if it fails.
**Alternative:** use an isolated experiment branch for a risky design change,
not an autonomous parallel build of the whole capstone.
**Teach-back:** "What did this capability add, and which test proves it?"

## 17: Release and demonstrate

Use [PUBLISHING.md](PUBLISHING.md) for the capstone's selected architecture.
Run P01-P04 on its stable endpoint with the approved consumer client, including
rollback. Demonstrate K03: normal case, ambiguous input, both MCP boundaries,
memory recall/isolation/forget, skill version behavior, and endpoint invocation.
For a hosted capstone, also demonstrate its custom function and workflow failure.
Include rejected action evidence if the capstone writes data.

Hand off the endpoint, selected version, consumer responsibilities, limitations,
sanitized evidence locations, rollback target, and still-running owned resources.
Review cleanup separately; a source commit or successful deployment command is
not proof of behavior.

**App practice:** request an evidence-backed handoff and review the actual
changes and resource list.
**Alternative:** demonstrate the same cases interactively rather than relying
only on a written report; neither method excuses missing evidence.
**Teach-back:** "What did Copilot help you do, what did you verify independently,
and what would you change before production use?"

## IT support reference notes

Use [the original ticket demo](../05-github-copilot/example_app/README.md) and
[MCP server](../05-github-copilot/example_app/mcp_server.py) only for this option.
The [support-triage skill](assets/support-triage/SKILL.md) is an optional example,
not a required skill for other students.

The server is unauthenticated and in-memory; run it only on loopback for local
experiments. Before remote testing, arrange an authenticated reachable test
service with a per-student namespace. Do not expose the demo through a tunnel.
Discovery reveals an extra mutation alias, `close_vlads_ticket`; use explicit
allowlists, not the assumption that its README enumerates every tool.

The browser UI and MCP server keep separate state. The browser is not evidence
that a tool changed the server's tickets. Verify mutations through independent
server reads. A remote service unavailable to the student blocks this capstone,
not the earlier read-only MCP lessons or other capstone choices.
