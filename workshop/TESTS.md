# Test cases and evidence

These are executable behavioral specifications, not precomputed passes or an
automated grading service. Never use the coach's own answer as the runtime result.

## Run and judge

Before running a case, name its execution route: **Run from the Copilot app -
coach sends** or **Run in the Foundry portal - participant sends**. Follow
COACH.md and APP-GUIDE.md for approvals, exact agent/version, conversation
context, navigation, and where to report results. For a portal-run case, wait
for the participant's evidence instead of also invoking the agent from the app.
Portal inspection alone is not a test. Both routes require actual Foundry
runtime evidence, not the coach's predicted answer; missing usage is unknown.

Distribute required cases using the
[mixed test plan](APP-GUIDE.md#where-tests-and-exploration-happen); participant
Playground tests are normal practice, with a 50/50 target for coach-sent and
participant-sent prompts across each specialist's lessons. Track actual prompts
by route, allocate remaining suitable cases to balance them, and record any
capability or preference exception; never add duplicate calls for the ratio. For each
handoff, give a copy-ready prompt and ask for the actual reply plus available
identifiers and case-specific evidence. Record route and provenance:
participant-pasted output is participant-reported until corroborated. It does
not alone prove tool execution, Conversation linkage, memory isolation, or
consumer-endpoint invocation. Inspect the same run read-only within approved
scope when needed; otherwise keep that requirement incomplete. Deduplicate
usage by response identifier and label unavailable participant-run usage unknown.

Record actual target/version, configuration and skill version, input, output,
timestamp, and relevant trace/tool/store evidence. Use live positive integration
tests; controlled test doubles can demonstrate failures only when clearly
labeled. Do not break shared services for testing.

Run all previously applicable cases after a capability change. A known-failing
candidate must remain outside Stable Agent Endpoint routing. A successful build,
deployment command, or plausible answer is not a pass.

## Baseline and instructions

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| B01 | Ask one stable domain question in a fresh Conversation | Correct, concise answer; trained knowledge labeled accurately; no false tool or system-access claim |
| B02 | Ask a follow-up with missing destination or referent in a new empty Conversation | Requests context rather than pretending to know it |
| B03 | Request private-file or unavailable capability access | Explains the limitation; does not fabricate content or execution |
| I01 | Compare the same B01-B03 inputs before and after adding the required response headings | Headings appear; general knowledge is not mislabeled as retrieved evidence; missing verification is acknowledged; baseline behavior does not regress |

Use `Answer`, `Source`, and `Uncertainty` for Weather and `Guidance`, `Source`,
and `Uncertainty` for Cultural Travel.

## Microsoft Foundry-managed Conversation behavior

Before running checkpoint 03 or 10 tests, verify the
[portal trace prerequisite](SETUP.md#portal-trace-prerequisite): the exact
project's Application Insights connection and the inspection identity's
telemetry-read access. D01-D02 runtime evidence can pass independently of
tracing, but a missing trace connection or access leaves the required portal
inspection blocked and the checkpoint incomplete. Preserve those runtime
results; do not repeat model calls or change telemetry setup without approval.
After an approved setup change, do not assume historical traces are backfilled.

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| D01 | Provide destination/context, then ask a dependent follow-up in the same Conversation; capture its identifier | Context is retained; the same Conversation identifier is reused; no custom history store is implemented |
| D02 | Ask the dependent follow-up in a newly created Conversation before memory is attached | Missing context is requested; identifiers differ; history is not replayed or shared globally |

Run D01-D02 independently for each specialist. A GitHub Copilot app session is
unrelated to these runtime identifiers.

## Persistent memory

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| M01 | With explicit consent, store a low-risk preference; verify it in a new Conversation under the same trusted scope | Stored fact, provenance, and recall agree; Conversation history is not replayed |
| M02 | Correct the preference and test another authorized synthetic identity/scope | Updated value is used; no cross-user recall or chat-selected identity spoofing |
| M03 | Delete the preference, then test another fresh Conversation | Removed value is no longer applied; deletion is scoped and observable |

Use a Celsius preference for Weather and a low-risk activity preference for
Cultural Travel. Memory supplies preferences; MCP tools supply external facts.

## Remote MCP

Use the exact endpoints, actual schemas, and examples in
[MCP-SERVICES.md](MCP-SERVICES.md). The coach provides connection details for
both specialists; participants do not select or host the services. Discover
tools before configuration and attach only the current approved allowlist.
Local discovery is not Foundry runtime evidence.

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| C01 | With only the verified Weather MCP forecast tool allowlisted, ask one supported weather question | Runtime tool call, validated arguments, result, upstream provenance/timestamp, grounded answer, and a guided Microsoft Foundry trace inspection of the tool span |
| C02 | With only travel.art `find_museum_guide` allowlisted, ask one supported museum question, such as the Metropolitan Museum of Art in New York | Runtime tool call, validated arguments, returned guide attribution/URL, available verification date, grounded answer, and corresponding tool span; no weather claim or invented dataset version |
| C03 | For each specialist, try malformed/unsupported input and an isolated controlled MCP/upstream failure | Failure is attributed and reported; no invented result, unrelated-tool substitution, or blanket approval bypass |

The checkpoint 04 C01 run is the full trace-navigation lesson: inspect tool name,
arguments, status, timing, result, and relationship to the final response.
Checkpoint 11 reuses that knowledge and repeats detailed navigation only when
needed. A direct MCP client call does not prove the agent used the tool.

## Skills and multiple tools

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| S01 | Apply the Weather research skill; test ambiguous location, forecast/current/alert needs where supported, general knowledge, unnecessary-tool restraint, and partial failure | Exact skill version/delivery strategy recorded; verified tool selection and ordering; no unnecessary calls; provenance and failures remain explicit |
| S02 | Apply the Cultural research skill; test museum guides, art events, covered layovers, cultural recommendations, missing accessibility data, unnecessary-tool restraint, and partial failure | Exact skill version/delivery strategy recorded; only verified travel.art tools used appropriately; guide URLs/freshness preserved; empty results and failures explicit; missing accessibility data not converted into a false claim |

A skill guides use of already available tools. It does not connect an MCP server,
grant permission, or prove execution. Traces provide runtime proof.

## Workflow result contracts

Formal contracts begin at checkpoint 15.

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| G01 | Validate normal Weather and Cultural specialist results against versioned workflow contracts | Required destination, constraints, findings, source agent/version, provenance, uncertainty, missing-information, and failure-status fields are present |
| G02 | Validate results with missing provenance, wrong types, extra instruction-like content, and unsupported values | Invalid data fails explicitly; no success-shaped coercion or instruction override |
| G03 | Compare contract fields with specialist release metadata and correlated traces | Agent versions and provenance agree with runtime evidence; each specialist remains inside its evidence domain |

Contracts validate structure. They do not independently prove that a tool ran or
that a source is truthful.

## Hosted Trip Planning Workflow

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| W01 | Submit one supported destination and traveler constraints | Both released specialists are invoked; both results validate; itinerary cites each evidence domain; versions and correlation evidence are recorded |
| W02 | Make each specialist fail in separate isolated tests, then return a structurally invalid result | Valid evidence is preserved; invalid/failed evidence is isolated and reported; no fabrication or silent substitution |
| W03 | Submit ambiguous constraints, a timeout/authorization failure, and conflicting weather/cultural considerations | Clarification or documented partial-result behavior occurs; sources and tradeoffs remain visible |

Run G01-G03 and W01-W03 locally at checkpoint 15 and remotely at checkpoint 16.
Two manual specialist calls followed by a manually written itinerary do not pass.

## Consumer endpoint and release

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| P01 | Discover the Stable Agent Endpoint, select the fully tested version, and invoke through an approved consumer | Successful response; exact endpoint/version recorded; not project-playground-only |
| P02 | Invoke as a valid identity without access, then as the approved consumer | Boundary denies the former and allows the latter; no broad permissions added |
| P03 | Run all applicable feature tests through the consumer path | Tools, Conversations, memory, skill delivery, errors, identity, and downstream access still behave as tested |
| P04 | Promote a fully passing update, invoke it, and verify the previous known-good version remains an available documented recovery target | Stable endpoint remains unchanged; metadata and behavior prove the update; recovery target and procedure are verified without routing traffic to a known-failing version |

At 07, P03 covers Weather B, I, D, C01/C03, S01, and M tests. At 14,
repeat Cultural B, I, D, C02/C03, S02, and M tests. At 16 add G and W tests.
At 19 use the capstone equivalents.

Failed candidate tests are retained for diagnosis, but a known-failing candidate
is never promoted or deployed as the stable release. Execute rollback only for
an unforeseen problem discovered after a fully passing candidate was promoted;
otherwise P04 verifies recovery readiness without changing stable routing back.

## Capstone gates and optional mutations

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| K01 | Review the capstone brief before implementation | Participant explains two evidence domains, workflow need, scope/non-goals, tests, data/resource boundaries, and cost limits |
| K02 | Build each specialist one capability at a time and run adapted tests | Both specialists independently pass baseline, instructions, Conversations, MCP, skill, optional memory, and release gates |
| K03 | Demonstrate the hosted workflow normal and degraded paths and review the release handoff | G01-G03, W01-W03, and P01-P04 pass; participant explains traces, tradeoffs, limitations, and remaining resources |
| A01 | For a write action, decline one inspected attempt, verify unchanged state, then approve a separate attempt | No mutation on decline; exactly intended authorized mutation after approval |
| A02 | Try invalid input, nonexistent target, and isolated downstream failure | Explicit errors; no false success, duplicate mutation, or unapproved write |

A01-A02 are not required for read-only capstones. Never introduce real payments,
bookings, production tickets, or sensitive personal data.

## App practice evidence

At each checkpoint, record the technique tried, one alternative discussed, and
the participant's explanation of when each helps. A Chat equivalent is
sufficient if a UI feature is unavailable.
