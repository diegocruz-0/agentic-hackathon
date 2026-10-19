# Apply the architecture to a scenario of your choice

Choose a capstone only after releasing both guided specialists and the hosted
Trip Planning Workflow. The capstone proves transfer by applying the same
architecture to a different problem: two complementary prompt-agent
specialists coordinated by a hosted Agent Framework workflow.

## 17: Choose and scope

| Scenario | Specialist 1 | Specialist 2 | Workflow result |
|----------|--------------|--------------|-----------------|
| Learning plan | Curriculum research | Learner-support resources | Validated study plan |
| Community event | Venue research | Accessibility and transit research | Evidence-backed event plan |
| Developer onboarding | Repository guidance | Microsoft Learn documentation | Sourced onboarding path |
| Student-proposed scenario | One bounded evidence domain | A complementary evidence domain | A validated combined result |

Ask one question at a time: scenario, user need, specialist 1 responsibility,
specialist 2 responsibility, workflow result, non-goals, then evidence sources.
Leave `scenario` null until the participant chooses here.

Create a short source-controlled brief under `student/capstone/` containing:

- the user need and expected workflow result;
- two genuinely distinct specialist responsibilities;
- approved MCP servers and exact tools, or another approved evidence mechanism;
- conversation boundaries and any justified persistent-memory facts;
- skill responsibilities and delivery strategy;
- safety, privacy, authorization, cost, and data boundaries;
- proposed workflow result contracts and partial-failure policy;
- concrete specialist and workflow tests;
- independent specialist releases and hosted release target.

Persistent memory is optional when it provides no clear cross-conversation value
or creates unnecessary privacy risk. Custom executable functions are optional
unless the scenario requires them. Use public or synthetic fixtures.

Run K01 before implementation. Keep the guided Weather, Cultural Travel, and
Trip Planning releases unchanged for comparison.

**App practice:** ask for a plan with non-goals and acceptance criteria without authorizing execution.
**Alternative:** select a preset scenario or propose an equivalent bounded design.
**Teach-back:** "Why are these specialists complementary rather than duplicate?"

## 18: Build and release the specialists

Build each capstone Microsoft Foundry Prompt Agent using the practiced sequence:

1. tool-free baseline and evidence boundary;
2. one controlled instruction refinement;
3. managed Conversation continuity and isolation;
4. one approved MCP server tool with grounded trace evidence;
5. a skill guiding any justified multi-tool selection and sequencing;
6. optional consented persistent memory when genuinely useful;
7. full regressions and promotion of only a fully passing candidate.

Each specialist needs separate names, versions, Stable Agent Endpoints, MCP
server/tool allowlists, skills, memory scopes when configured, tests, and release
evidence. One specialist's success never substitutes for the other's.

Run K02 and the adapted B, I, D, C, S, M, and P tests appropriate to each
specialist. A known-failing candidate remains outside stable routing.

**App practice:** give Copilot one bounded change, inspect its diff and evidence, then debug narrowly.
**Alternative:** use an isolated experiment branch for one risky design change.
**Teach-back:** "What did this capability add, and which observed test proves it?"

## 19: Build, release, and demonstrate the workflow

Define versioned result contracts for both capstone specialists. Implement a
Microsoft Agent Framework workflow that invokes their Stable Agent Endpoints,
validates each result, and combines only supported evidence.

Run G01-G03 and W01-W03 locally, including:

- both specialists succeed;
- each specialist fails while the other remains valid;
- a specialist returns structurally invalid data;
- a dependency times out or rejects authorization;
- no missing evidence is fabricated;
- repeated runs preserve contract and release compatibility.

After explicit approval, deploy only a fully passing workflow candidate as a
Microsoft Foundry Hosted Agent. Run P01-P04 and K03 through its Stable Agent
Endpoint. Inspect the nested workflow trace and correlated specialist traces,
including contract validation and aggregation decisions.

Hand off the three exact released versions, endpoint responsibilities,
limitations, sanitized evidence locations, recovery target, and all owned
resources still running. Review cleanup separately.

**App practice:** request an evidence-backed handoff and compare it with live metadata and traces.
**Alternative:** demonstrate the same cases interactively; neither method excuses missing evidence.
**Teach-back:** "What did Copilot help create, and what runtime evidence did you verify independently?"

## Optional write actions

Read-only capstones are fully valid. If a scenario performs writes, require an
authenticated, participant-isolated synthetic service and run A01-A02. Verify
decline/no mutation, approved mutation, invalid input, not-found behavior, and
downstream failure independently. Never introduce real payments, bookings,
production tickets, or sensitive personal data.

Build any ticket-service integration under `student/` using the
facilitator-approved synthetic backend. Do not expose an unauthenticated local
demo through a tunnel.

The optional [IT support example app](../05-github-copilot/example_app/README.md)
can illustrate the scenario. Its browser UI and MCP server use separate state;
it is not a ready-made shared backend for Foundry.
