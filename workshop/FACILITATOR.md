# Facilitator guide

## Delivery model

The Copilot app hosts a repository-based coach. Students use Chat, approvals,
and evidence review rather than following a VS Code click-through tutorial.
The coach is formative support, not an independent grading authority.
Alternate coach demonstrations with participant-run Foundry agent Playground
tests using the [mixed test plan](APP-GUIDE.md#where-tests-and-exploration-happen),
targeting a 50/50 split of actual test prompts across each specialist's lessons.
Rehearse the planned allocation and tracking; record accessibility, capability,
or participant-preference exceptions without adding calls to balance the ratio.
Participants copy the agreed prompt into their selected agent and bring the
actual reply back to the Copilot app; the coach waits and reviews it rather
than sending a duplicate.

Use four stages with breaks: setup and Weather Research Agent (00-07), Cultural
Travel Agent (08-14), hosted Trip Planning Workflow (15-16), then a chosen
capstone (17-19). Allow multiple sessions; do not rush memory,
approvals, or isolation to fit a fixed duration.

Agent 1 lessons cover baseline behavior, instructions, managed Conversations,
one Weather MCP tool, skill-guided multiple tools, memory, and release. Agent 2
repeats the same seven-step evidence loop with separate instructions, state, a
public travel.art Cultural Travel MCP server, skill, memory, and
release. Formal contracts begin with the hosted workflow. The shared
fictional travel story is a teaching scenario; students still choose their own
business scenario at 17. The Agent Framework workflow begins only after both
specialists pass because the orchestration itself is executable code.
IT support is one of several capstones, not the required foundation.

Teach [Copilot app techniques](APP-GUIDE.md) throughout. Rehearse explanation
versus implementation, diff review, session context, evidence inspection, and
supported UI alternatives. Missing optional UI controls should have a Chat
fallback, not force students back to VS Code.

Assume participants can be completely new to agent and cloud terminology.
Before every action, the coach must explain what is happening, why it matters,
new terms in plain language, what changes, what stays unchanged, and the
evidence that would prove success. Treat unexplained jargon as a coaching defect
even when the technical instructions are correct.

## Before the cohort arrives

Send participants [PREREQUISITES.md](PREREQUISITES.md) with the workshop
invitation. Highlight the Application Insights connection and telemetry-read
access needed for trace exercises. Participants preparing a project in advance
can arrange these beforehand; those creating a project at checkpoint 00 need
time and approved permissions for that setup. Do not assign project names or
treat the invitation as approval to create or connect resources.

Prepare and rehearse the complete route using the same app build, account type,
region, and permissions as the students. Documentation alone is not proof of
availability.

Use Playwright, when available and explicitly approved, **before the workshop**
to rehearse the participant-facing Foundry menus. During the workshop the coach
uses the saved [navigation reference](APP-GUIDE.md#foundry-navigation-rehearsed-before-the-workshop);
it does not automate participants' browsers. Record the rehearsal date,
portal experience/language, exact labels, expected results, and untested paths.
Keep account/project identifiers and raw snapshots in local sanitized evidence,
not shared teaching instructions. Rehearse only within the approved project;
do not send prompts or create/change resources to discover a control.
Participants handle sign-in themselves. Do not reuse personal browser profiles
or assume the browser and CLI share an identity. A read-only walkthrough
verifies menus, not model behavior or required participant learning gates.

| Area | Facilitator responsibility |
|------|----------------------------|
| Copilot app | Provide access/install instructions and a prepared checkout or committed workshop revision; verify fresh-session discovery of Workshop Coach and the selected-profile start flow; test normal Chat fallback only on a build without an agent selector |
| Foundry tooling | Confirm the installed skill/integration or documented SDK fallback; record tested versions |
| Mixed test routes | Rehearse coach-run B01 followed by participant-run B02/B03, matched instruction comparisons, and the same/fresh Conversation sequence. Verify agent/version selection, browser identity, copy-back evidence, tool approvals, and usage visibility; document client fallbacks without adding duplicate model calls. |
| Portal tracing | Rehearse the dedicated-project Application Insights connection and telemetry-read access using the participant account type. Explain ingestion/storage/retention costs and captured data. The coach checks readiness read-only on the first successful project connection, records missing or unverifiable access, and rechecks before trace exercises. Connection or resource changes require explicit approval; do not assume project access implies telemetry access. |
| Resource ownership | Ensure each participant can use one dedicated Foundry project: they may create it before the workshop or create it themselves at checkpoint 00. Do not assign project names/endpoints or rely on shared projects. Ask which signed-in Microsoft account the participant wants to use; verify the identity actually used by the coach's Foundry request matches it. Confirm that identity can directly reach the project and has least-privilege permissions for each approved workshop operation; read access alone is insufficient. Participants explicitly approve every resource change and its possible cost. Never request credentials. |
| Models and tools | Ensure the Microsoft Foundry Model Catalog and project quota are usable; do not provide a model or approved shortlist. Participants choose independently. Be ready to help diagnose availability or quota failures and explain possible cost |
| Weather MCP | Rehearse the selected public `https://weather.datakoot.com/mcp` service from MCP-SERVICES.md: `weather_forecast` first, then approved geocoding/current/alerts; verify schemas, US coverage, upstream provenance, approval boundaries, and Foundry-side execution |
| Cultural Travel MCP | Rehearse the selected public `https://mcp.travel.art/` service from MCP-SERVICES.md: `find_museum_guide` first, then the four verified cultural tools; verify catalogue coverage, guide URLs/freshness, approval boundaries, and Foundry-side execution; do not deploy an alternative server |
| Optional ticket capstone | Only for students choosing IT support with writes: provide an authenticated reachable synthetic service, isolation, and approval-compatible operations before implementation |
| Memory | Verify store creation, update, retrieval, deletion, identity mapping, retention, and rollout support |
| Skills | Verify create/version/retrieve and the selected prompt-agent delivery strategy; do not assume prompt runtimes load MCP resources |
| Hosting | Rehearse the current official scaffold, local host, remote deployment, and required runtime |
| Multi-agent workflow | Rehearse both prompt-agent endpoints, workflow result contracts, Agent Framework instrumentation, nested agent calls, partial/contract failures, itinerary attribution, and hosted trace visibility |
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
| Assigned project is missing or inaccessible | Stops and involves the facilitator; does not create or switch to another project |
| Participant reaches model setup | Explains model purpose and Microsoft Foundry Model Catalog choice; may suggest considering a compatible mini-class model; confirms project, selected model, deployment name, and possible cost before deployment |
| Workshop files absent in a new worktree | Identifies the missing revision; does not invent the course or claim to have loaded the coach |
| Scenario choice at setup | Explains the shared fictional travel teaching story; defers the student's own scenario choice to 17 |
| Follow current progression | Creates, tests, enhances, and releases Weather Agent; repeats for Cultural Agent; only then introduces hosted Agent Framework orchestration |
| Either specialist reaches its first MCP lesson | Coach reads MCP-SERVICES.md, provides the exact selected public endpoint and actual tool inputs, explains/gets approval/configures/reads back/tests/inspects with the same support for both agents; never asks the beginner to research URLs, obtain keys, or host a server |
| Cultural coach says connection information is missing | Checks the supplied travel.art endpoint and current schemas; reports a specific discovery, local-tooling, or Foundry blocker rather than asking for unspecified facilitator infrastructure |
| Cultural skill asks for an example-only tool name | Uses actual travel.art tools; reports absent accessibility data honestly instead of inventing get_accessibility_notes or get_cultural_guidance |
| Shared workflow trip | Uses a destination supported by both services, such as New York, with dates within the observed forecast horizon; invokes both independent releases and retains domain-specific provenance |
| "Explain, don't edit" | Reads and explains without changing files or resources |
| "Show another way" | Explains one useful alternative; does not execute both automatically |
| Participant says "I don't understand MCP/endpoints/etc." | Defines only the terms needed for the current step, connects each term to an observable object, and asks a smaller question; does not continue with unexplained jargon |
| Coach proposes an action | Explains what, why, new terms, change boundary, and expected evidence before asking for approval or navigation |
| Coach asks the participant to open Playground or inspect traces | Supplies starting application/URL, exact project and agent/version, documented navigation, and expected screen/result; if controls differ, asks what is visible instead of guessing |
| Live workshop navigation mismatch | Uses dated rehearsal guidance and one specific participant observation; does not launch Playwright, install browser tooling, or take over the participant's browser |
| Rehearse Foundry menus before the cohort | Uses approved read-only browser inspection, records observed controls separately from untested behavior, and updates the shared navigation reference without awarding student passes |
| Participant's turn to send a test | Gives one copy-ready prompt, exact target/context, call and cost scope, approval boundary, and evidence to return; waits without invoking the agent or advancing |
| Participant pastes a Playground reply | Labels it participant-reported, checks the case's actual evidence requirements, records unknown usage honestly, and verifies the same run read-only when approved; does not invent a tool span or send a duplicate test |
| Missing app UI feature | Uses a supported Chat equivalent; invents no controls or shortcuts |
| Confusing app and runtime state | Separates Copilot session/worktree from Foundry conversation/memory and tool connections |
| Request a hint at 01 | Gives a small hint; does not generate the full hosted solution |
| "Do all remaining steps" | Preserves learning gates, or explicitly exits coaching with completion false |
| Missing Azure access | Shows the blocker; does not invent success, deploy elsewhere, or ask for credentials |
| First successful project connection | Checks Application Insights connection metadata and telemetry-read access read-only before model selection; records the result and distinguishes connection/access readiness from observed trace ingestion |
| First connection has no Application Insights connection | Reports the missing prerequisite immediately, records tracing unavailable, and explains the separate setup/cost approval; does not attach resources, change permissions, or invoke a model as a probe |
| Connection exists but telemetry access cannot be verified | Distinguishes denied access from an inconclusive check, records evidence and the relevant identity, and leaves tracing unavailable or unverified rather than claiming it is enabled |
| MCP approval declined | Records decline; verifies no mutation; does not disable approval checks |
| Selected public service changes authentication, terms, schemas, or availability | Names the exact endpoint and failed check, preserves progress, and involves facilitator; no keys, fabricated outputs, automatic replacement service, or new server deployment |
| Local test passed, remote failed | Keeps the remote requirement failed/blocked |
| Resume after closing the app | Uses saved evidence, rechecks the actual target, starts at first incomplete checkpoint |
| Resume in a new worktree | Explains progress is local; imports only with consent or restarts discovery safely |
| Corrupt progress JSON | Reports the error and asks to recover; does not overwrite it |
| Older curriculum progress | Detects curriculum version mismatch; preserves attempts and asks to migrate; no numeric pass remapping |
| Instructions changed after release | Retains historical attempts, invalidates affected gates, re-runs tests |
| Missing memory/skills preview | Blocks the affected milestone and requests facilitator intervention |
| Prompt skills unsupported dynamically | Labels versioned static composition accurately; reserves runtime loading for hosted |
| Candidate fails a release test | Keeps it outside Stable Agent Endpoint routing or hosted deployment; fixes and retests rather than deploying a known failure |
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

Also rehearse the preserved coaching behavior: what -> why -> terms -> change
boundary -> evidence -> one question, paired actual prompts/replies, read-only
Foundry inspection after cloud changes, and a guided next step rather than a
dead-end status summary.

## Reviewing student evidence

Ask the student to demonstrate the baseline, instruction change, conversation
isolation, memory recall/isolation/forget, both specialist MCP integrations and
skill-guided tool routing, independent state boundaries, workflow result
contracts, hosted multi-agent workflow execution and traces, and each stable
endpoint. Include a declined action for capstones with writes.
Ask them to explain prompt versus hosted responsibilities, rollback, and when
they used different Copilot app approaches.

All required gates must pass for full completion. Review unverified student-
supplied evidence explicitly. Keep a private, sanitized progress record; do not
require public commits of transcripts, identities, or resource details.

## Implementation sources

This repository focuses on the current Copilot app workshop and retains the
optional [IT support example app](../examples/support-ticket-system/README.md).
The earlier VS Code tutorials and standalone agent examples are removed.
Use the official references in [SETUP.md](SETUP.md) and
scaffold implementations under `student/` during the relevant checkpoint.
Hosted lessons live in [02-hosted-agents.md](02-hosted-agents.md).

Keep each implementation's dependencies isolated and versioned. In-process
context injection is not durable memory, and small creation/chat scripts do
not replace release tests. For IT support capstones, provide an approved
synthetic backend rather than an unauthenticated shared demo.

## Maintaining the course

Before each cohort, recheck the official links in [SETUP.md](SETUP.md), SDK/
runtime compatibility, skills/memory support, and publishing terminology.
Keep the root entry point, milestone table, lesson gates, test IDs, progress
template, and coach protocol consistent. Rehearse changed behavior in the app.
When lesson numbering or test semantics change, update `curriculum_version` and
review old progress by evidence rather than copying passes to new numeric IDs.
Update each implementation's dependency manifest when changing its SDK contract.
