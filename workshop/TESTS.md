# Test cases and evidence

These are executable behavioral specifications, not precomputed passes or an
automated grading service. Never use the coach's own answer as the runtime result.

## Run and judge

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

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| C01 | With only the verified Weather MCP forecast tool allowlisted, ask one supported weather question | Runtime tool call, validated arguments, result, upstream provenance/timestamp, grounded answer, and a guided Microsoft Foundry trace inspection of the tool span |
| C02 | With only the verified Cloudflare Cultural Travel MCP introductory tool allowlisted, ask one supported attraction question | Runtime tool call, validated arguments, dataset version/attribution, grounded answer, and corresponding tool span; no weather claim |
| C03 | For each specialist, try malformed/unsupported input and an isolated controlled MCP/upstream failure | Failure is attributed and reported; no invented result, unrelated-tool substitution, or blanket approval bypass |

The checkpoint 04 C01 run is the full trace-navigation lesson: inspect tool name,
arguments, status, timing, result, and relationship to the final response.
Checkpoint 11 reuses that knowledge and repeats detailed navigation only when
needed. A direct MCP client call does not prove the agent used the tool.

## Skills and multiple tools

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| S01 | Apply the Weather research skill; test ambiguous location, forecast/current/alert needs where supported, general knowledge, unnecessary-tool restraint, and partial failure | Exact skill version/delivery strategy recorded; verified tool selection and ordering; no unnecessary calls; provenance and failures remain explicit |
| S02 | Apply the Cultural research skill; test destination search, attractions, cultural guidance, accessibility notes, unnecessary-tool restraint, and partial failure | Exact skill version/delivery strategy recorded; verified tool selection and ordering; missing accessibility data is not converted into a false claim |

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
