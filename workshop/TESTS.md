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
| I01 | Compare responses to the same weather and documentation queries before and after adding the headings Answer, Source, and Uncertainty | Headings appear; fixture/public retrieval origins are accurate; missing verification is acknowledged; baseline behavior does not regress |

## Function tools

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| T01 | Directly invoke the weather fixture with Seattle, then ask the Foundry agent for Seattle weather using the tool | Validated call observed; result has condition sunny, temperature_c 20, source workshop-fixture; response identifies it as synthetic, not live weather |
| T02 | Invoke with an unknown location and blank input, directly and through the client/runtime | Explicit unsupported-location result and validation error respectively; no invented weather; invalid inputs cannot bypass validation |
| T03 | In an isolated test, make the executor fail; inspect a successful call continuation separately | Failure surfaces without a success-shaped answer; successful continuation uses the correct call ID and result; bounded loop and allowlist enforced |

At 02 execution is in the prompt client; at 10 it is in the hosted runtime.
A model mentioning a function name is not execution evidence. The original
random fixture is a concept reference, not the deterministic acceptance fixture.

## Multi-turn

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| D01 | In conversation A say "My name is Alice and I love hiking", then ask "What do you remember about me?" | Recalls the supplied name/hobby using that conversation; same conversation/session identifier recorded |
| D02 | Ask the same follow-up in conversation B without sending the earlier messages and before persistent memory is attached | Does not recall Alice's facts; IDs differ; client does not secretly replay history or reuse a shared global session |

Reusing a Copilot coaching session is unrelated to these runtime tests.

## Memory

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| M01 | Ask to remember a preference for concise bullet points; verify storage/update completion; in a new conversation under the same trusted scope ask what style is preferred | Store evidence and recall agree; no old history or preference reinserted into the prompt |
| M02 | In another authorized synthetic identity/scope ask for the first user's preference; separately ask the first user to use a detailed style for one answer | No cross-user recall or chat-selected identity spoofing; current explicit style request overrides stored preference |
| M03 | Forget that preference, verify the scoped update/deletion, then ask in another fresh conversation | No retrieval of the removed preference; no deletion of others' data; no history supplied by client masking the result |

At 11, repeat M01 across local restart and controlled remote restart/redeployment.
Inspect the trusted identity-to-scope mapping: a string partition alone is not
authorization. Do not use real credentials or sensitive data as memory fixtures.

## Workflow

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| W01 | Run uppercase -> reverse on `hello world`, first without an LLM, then ask the agent to explain the computed output | Exact deterministic output DLROW OLLEH; both stages observed in order; explanation reflects the actual output |
| W02 | Fail the first stage in an isolated harness | Second stage and success explanation are not run; explicit error reaches caller; no fabricated final output |

At 05, verify local graph output and a real Foundry explanation request from the
client. At 12, verify the graph executes inside the hosted request path locally
and remotely. These are distinct execution locations, not interchangeable passes.

## Remote MCP

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| C01 | "Use the connected documentation MCP server to find how Foundry agents connect to MCP." | Actual schema discovery/allowlist, runtime MCP call, result, and grounded answer; not just a Copilot tool call |
| C02 | Reject a pending approval where configured, or inject a controlled MCP failure in an isolated candidate/harness | Decline/failure reported; no claimed successful lookup; no blanket approval bypass |

A successful direct MCP client call does not prove the Foundry agent uses it.
Live runtime calls are required at 06 and again for the hosted remote target at 13.

## Skills

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| S01 | Author/upload/retrieve the explain-results skill; compare exact content/version; invoke the weather and documentation examples | Reviewed policy applied with Answer, Source, Uncertainty headings; source/fixture provenance is accurate; static composition or dynamic loading labeled explicitly |
| S02 | Hosted: inspect runtime skill discovery/load, test a relevant and an unrelated request, activate a tested skill edit, then roll back | Load evidence exists; unrelated request not forced through irrelevant procedure; observed version/cache behavior matches update and rollback |

At 07, static composition of a retrieved version is valid. At 14, a file copied
into the image or an MCP tools listing alone cannot pass runtime skill loading.

## Consumer endpoint and release

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| P01 | Discover the stable endpoint, select the tested version, invoke with a separate approved consumer client | Real successful response; actual endpoint/version recorded; hosted deployment running; not a local or project-playground-only call |
| P02 | Invoke as a valid authenticated test identity without access, then the approved consumer | Service boundary denies the former and allows the latter; no broad permissions added to force success |
| P03 | Run all applicable feature tests through the consumer path | Tools, conversation boundaries, memory, workflow, skill delivery, and error/approval handling still work; actual downstream identity has access |
| P04 | Record URL/version, select a tested new version, invoke, restore prior selection, and invoke again | Exact endpoint URL unchanged; metadata and observed behavior prove both update and rollback; known-good version retained |

At 08, P03 covers B01-B03, T01-T03, D01-D02 with a clean-scope control,
M01-M03, W01-W02, C01-C02, I01, and S01. The prompt consumer includes the function
executor and workflow orchestration; document that the endpoint does not host
that code. At 15 add S02 and verify hosted execution. At 18 use the capstone's
approved adapted inputs, plus A01-A02 when it supports writes.

Controlled failures use an isolated candidate/endpoint with equivalent
configuration; do not disrupt others' releases. An endpoint URL or HTTP 200
containing an error is not a pass.

## Capstone gates and optional mutations

| ID | Input/procedure | Pass conditions |
|----|-----------------|-----------------|
| K01 | Review the capstone brief before implementation | Student explains architecture, scope/non-goals, data/resource boundaries, concrete tests, and cost limits; no live changes yet |
| K02 | Build one capability at a time and run the adapted concept tests | Baseline, function, conversations, memory, workflow, MCP, instruction and skill tests pass on actual chosen target; evidence distinguishes client and service responsibilities |
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
