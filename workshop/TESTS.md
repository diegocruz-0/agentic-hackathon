# Test cases and evidence

These are executable behavioral specifications, not precomputed passes or an
automated grading service. The coach and student grow a small test client as
capabilities are added. Never use the coach's own answer as the runtime's result.

## Run and judge

Record actual target/version, configuration and skill version, input, output,
timestamp, and relevant tool/store evidence. All listed conditions must hold.
Use live positive integration tests; controlled test doubles can demonstrate
failures only when clearly labeled. Do not break shared services for testing.

For baseline/instruction comparisons, use two fresh conversations per case and
retain both outcomes. Judge observable meaning rather than exact prose except
explicit formatting, deterministic outputs, and identifiers.

Run all previously applicable cases after a capability change. Earlier
pre-memory conversation tests remain historical; after memory is attached, use
fresh empty scopes for the no-memory control and M01-M03 for intentional recall.
Never grant completion for unavailable or unverified behavior.

## Baseline and instructions

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| B01 | "What is the capital of France?" and "Tell me one brief fact about France." as independent baseline requests | Correct, concise answers; no false tool or system-access claims |
| B02 | "What is its size?" in a new empty conversation | Requests context rather than pretending to know the referent |
| B03 | "Read a private file from my laptop and tell me its contents." without a file tool | Explains it lacks that access; does not fabricate file content or claim execution |
| I01 | Compare B01-B03 responses before and after adding the headings Answer, Source, and Uncertainty | Headings appear; general knowledge is not mislabeled as retrieved evidence; unsupported access and missing verification are acknowledged; baseline behavior does not regress |

## Function tools

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| T01 | Directly invoke the weather fixture with Seattle, then ask the Foundry agent for Seattle weather using the tool | Validated call observed; result has condition sunny, temperature_c 20, source workshop-fixture; response identifies it as synthetic, not live weather |
| T02 | Invoke with an unknown location and blank input, directly and through the client/runtime | Explicit unsupported-location result and validation error respectively; no invented weather; invalid inputs cannot bypass validation |
| T03 | In an isolated test, make the executor fail; inspect a successful call continuation separately | Failure surfaces without a success-shaped answer; successful continuation uses the correct call ID and result; bounded loop and allowlist enforced |

Function execution begins at hosted checkpoint 09. A model mentioning a
function name is not execution evidence. The original random fixture is a
concept reference, not the deterministic acceptance fixture.

## Foundry-managed conversation behavior

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| D01 | In the Foundry playground, say "My name is Alice and I love hiking", then ask "What do you remember about me?" in the same conversation; repeat through the SDK/API while capturing the managed conversation identifier | Recalls the supplied name/hobby; Foundry-managed continuity is observed in the UI; the same conversation identifier is reused in the evidence path; no custom conversation store is implemented |
| D02 | Start a fresh playground conversation and ask the same follow-up; repeat with a newly created conversation B through the SDK/API before persistent memory is attached | Does not recall Alice's facts; identifiers differ where exposed; the client does not replay history or reuse a shared global conversation |

Foundry creates and stores these conversation items automatically. The exercise
tests continuity and isolation; it does not ask the student to implement history
storage. A production client remains responsible for associating an authorized
user/session with the correct conversation identifier. Reusing a Copilot
coaching session is unrelated to these runtime tests.

## Memory

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| M01 | Ask to remember a preference for concise bullet points; verify storage/update completion; in a new conversation under the same trusted scope ask what style is preferred | Store evidence and recall agree; no old history or preference reinserted into the prompt |
| M02 | In another authorized synthetic identity/scope ask for the first user's preference; separately ask the first user to use a detailed style for one answer | No cross-user recall or chat-selected identity spoofing; current explicit style request overrides stored preference |
| M03 | Forget that preference, verify the scoped update/deletion, then ask in another fresh conversation | No retrieval of the removed preference; no deletion of others' data; no history supplied by client masking the result |

At 10, repeat M01 across local restart and controlled remote restart/redeployment.
Inspect the trusted identity-to-scope mapping: a string partition alone is not
authorization. Do not use real credentials or sensitive data as memory fixtures.

## Workflow

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| W01 | Run uppercase -> reverse on `hello world`, first without an LLM, then ask the agent to explain the computed output | Exact deterministic output DLROW OLLEH; both stages observed in order; explanation reflects the actual output |
| W02 | Fail the first stage in an isolated harness | Second stage and success explanation are not run; explicit error reaches caller; no fabricated final output |

Workflow execution begins at hosted checkpoint 11. Verify the graph executes
inside the hosted request path locally and remotely.

## Remote MCP

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| C01 | With only the approved weather MCP connected, ask one supported weather question | Actual schema discovery, runtime MCP call, result, data-source provenance, and grounded answer; not merely a Copilot tool call or the old local fixture |
| C02 | Connect the cultural-travel MCP; ask one weather question, one cultural question, and one request that makes server selection observable | Correct server/tool selected for each request; evidence names the source of each result; no tool-name ambiguity, invented cross-server synthesis, or accidental capstone commitment |
| C03 | Reject a pending approval where configured, or inject a controlled failure into one MCP integration | Decline/failure reported; no claimed successful lookup, silent substitution of the other server, or blanket approval bypass |

A successful direct MCP client call does not prove the Foundry agent uses it.
Live runtime calls are required at 04 and again for the hosted remote target at 12.

## Skills

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| S01 | Author/upload/retrieve the explain-results skill; compare exact content/version; invoke one query per connected MCP and one general-knowledge query | Reviewed policy applied with Answer, Source, Uncertainty headings; each MCP result has accurate server/tool provenance; general knowledge is distinguished from retrieval; static composition or dynamic loading is labeled explicitly |
| S02 | Hosted: inspect runtime skill discovery/load, test a relevant and an unrelated request, activate a tested skill edit, then roll back | Load evidence exists; unrelated request not forced through irrelevant procedure; observed version/cache behavior matches update and rollback |

At 05, static composition of a retrieved version is valid. At 13, a file copied
into the image or an MCP tools listing alone cannot pass runtime skill loading.

## Consumer endpoint and release

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| P01 | Discover the stable endpoint, select the tested version, invoke with a separate approved consumer client | Real successful response; actual endpoint/version recorded; hosted deployment is running when the target is hosted; not a local or project-playground-only call |
| P02 | Invoke as a valid authenticated test identity without access, then the approved consumer | Service boundary denies the former and allows the latter; no broad permissions added to force success |
| P03 | Run all applicable feature tests through the consumer path | Architecture-appropriate MCP/tools, conversation boundaries, memory, workflow, skill delivery, and error/approval handling still work; actual downstream identity has access |
| P04 | Record URL/version, select a tested new version, invoke, restore prior selection, and invoke again | Exact endpoint URL unchanged; metadata and observed behavior prove both update and rollback; known-good version retained |

At 07, P03 covers B01-B03, I01, D01-D02 with a clean-scope control,
M01-M03, C01-C03, and S01. The prompt endpoint has no required local function
executor or client-side workflow. At 14 add T01-T03, W01-W02, S02, and verify
hosted execution. At 17 use the capstone's approved architecture-specific
inputs, plus A01-A02 when it supports writes.

Controlled failures use an isolated candidate/endpoint with equivalent
configuration; do not disrupt others' releases. An endpoint URL or HTTP 200
containing an error is not a pass.

## Capstone gates and optional mutations

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| K01 | Review the capstone brief before implementation | Student explains architecture, scope/non-goals, data/resource boundaries, concrete tests, and cost limits; no live changes yet |
| K02 | Build one capability at a time and run the adapted concept tests | Baseline, conversations, memory, MCP, instruction, and skill tests pass on the actual target; hosted capstones also pass function and workflow tests; evidence distinguishes managed, remote, and hosted-code responsibilities |
| K03 | Demonstrate normal/ambiguous/failure cases and review the release handoff | P01-P04 pass; student explains observed behavior, tradeoffs, app techniques, limitations, and remaining resources |
| A01 | For a write action, inspect parameters, decline once and verify unchanged state, then approve a separate attempt | Enforced approval and authorization; no mutation on decline; exactly intended mutation after approval; independently observed state |
| A02 | Try invalid input, nonexistent target, and an isolated downstream failure | Explicit errors, no false success or unapproved writes; ambiguous results reconciled before retry rather than duplicate mutations |

A01-A02 are not required for read-only capstones; record reviewed non-applicability.
All implemented mutations must pass them. Do not introduce real payments,
bookings, production tickets, or sensitive personal data for these exercises.

## App practice evidence

At each checkpoint, record the technique tried, one alternative discussed, and
the student's explanation of when each helps. The [app guide](APP-GUIDE.md)
lists equivalent Chat approaches when a visual feature is absent.
Using a specific UI button is not a prerequisite; understanding the task,
scope, context, permissions, and evidence is.
