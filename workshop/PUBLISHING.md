# Release through stable Foundry endpoints

Use this guide at **07 for the Weather Research Agent**, **14 for the Cultural
Travel Agent**, **16 for the hosted Trip Planning Workflow**, and **19 for the
chosen capstone**. Keep separate names and endpoints so students can compare
both specialists and the orchestrator without overwriting evidence.
Tests and evidence requirements are in [TESTS.md](TESTS.md).

## Current model versus legacy publishing

The [current Foundry model](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications)
gives a newly created agent its own identity and stable endpoint. There is no
separate Agent Application creation step to obtain that endpoint. A version
selector controls the version consumers invoke.

In this workshop, **release** means selecting a tested version, configuring
consumer access, and proving invocation through the stable endpoint. Current
Foundry **publishing** terminology refers to distributing that endpoint to
Teams/Microsoft 365. That channel distribution is optional and is not required
for the core course.

Inspect actual agent metadata and available tooling to determine which model
the student's environment supports. Do not guess an endpoint URL, assume the
latest-created version is selected, or treat a project endpoint as the stable
agent endpoint.

## Release one fully tested version

1. **Review the candidate.** Run every required pre-release test. Record agent name/version, instructions, model,
   tools/allowlist, memory store/scoping, skill version/delivery strategy, and
   the passing test evidence. For a hosted update, identify the current
   known-good running deployment and the separately tested candidate source/
   configuration revision.
   A known-failing candidate is not promoted to stable routing and a known-failing
   hosted candidate is not deployed.
2. **Inspect endpoint metadata.** Read the service-returned stable endpoint,
   protocol configuration, version selector, and agent identity. Use current
   official APIs or the installed Foundry workflow. Resolve unsupported API
   versions rather than constructing likely-looking requests.
3. **Confirm the release action.** Explain the exact version routing change,
   consumer access, cost, and rollback target. Obtain approval before making
   changes. If the endpoint already selects the tested version, verify it
   rather than creating duplicate release resources.
4. **Configure least-privilege access.** Confirm the consumer identity can
   invoke the endpoint and the agent identity can access downstream tools,
   memory, and skills. Developer credentials succeeding locally do not prove
   the deployed identity has permission. Use current role/permission guidance;
   do not substitute an owner role for diagnosis.
5. **Invoke as a consumer.** Use a separate client configured for the returned
   endpoint and supported protocol. Verify the SDK's base-URL semantics so
   `/responses` is not appended twice. Do not print or persist bearer tokens.
   Run P01-P03 and inspect actual results.
6. **Save the release record.** Store the endpoint, selected version, identity/
   access configuration, test evidence, and rollback target in local progress.
   Never copy access tokens into a shareable handoff.

For the Weather Research Agent, verify its managed conversation behavior,
memory, Weather MCP server and forecast tool connection, instructions,
evidence-aware weather output and skill-guided tool behavior through the released
endpoint. It does not rely on a
local custom-function executor or client-side workflow.

Prompt checkpoint 07 stops here, after a teach-back. Preserve the prompt release
while the Cultural Travel Agent is developed.

At checkpoint 14, release the Cultural Travel Agent through its own stable
endpoint. Verify its instructions, conversation isolation, selected travel.art MCP,
skill-guided multi-tool behavior, and memory. Record both specialist versions
and prove neither claims the other's
tools or evidence domain.

## Hosted update and rollback

At checkpoint 16, first pass the same release checks for the hosted workflow.
Then make one small visible instruction change as a separate candidate version,
run the relevant regressions, and perform P04 after approval.

Route the existing endpoint to the tested new version. Inspect metadata and
invoke it; do not infer selection from creation order or an unverified answer.
Verify that the previous known-good code, configuration, contract, and
specialist versions remain available as the documented recovery target. Do not
route traffic back merely as a demonstration. Execute rollback only when an
unforeseen problem is discovered after promotion, then inspect metadata and
invoke the restored version.

At 19, repeat release and P04 for the capstone workflow. Preserve
both prompt-agent releases and the hosted workflow release; do not make the
capstone silently replace them.

**App practice:** compare the proposed routing change, the resulting metadata,
and an actual invocation. Discuss a raw-response inspection as an alternative
to a summary, or applicable hosted Canvas controls if available. A commit,
visual handoff, or successful deployment command alone does not prove behavior.

**Teach-back:** "What stays stable for the consumer, and which identities need
permission to call the agent and its tools?"

## Legacy Agent Applications: explicit compatibility route only

[Agent Applications](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agent-applications)
are the previous model: an application wraps a deployment referencing an agent
version. Existing applications continue to work, but they are not the default
new-course target.

If the environment only supports that model, mark the current-model release
checkpoint blocked. Ask the facilitator to approve a legacy/partial route or
provide a compatible environment; do not silently change the learning outcome.
Record `publishing_model` as `legacy` for any approved compatibility exercise.

Key differences to teach:

- Application creation and deployment are separate resources/operations.
- Prompt deployments use the managed type; hosted deployments use the hosted
  type and require a running hosted version.
- Publication introduces a different agent identity. Downstream permissions
  do not transfer automatically.
- Legacy application Responses endpoints support stateless requests; do not
  assume project `/conversations` behavior works there. Client-managed history
  is not a substitute for the separate memory-store lesson.
- Invocation permissions differ from current agent-endpoint permissions.
  Verify the correct role and scope rather than copying a newer role name.
- Migrating to a new-model agent changes the endpoint and identity. Do not
  promise that a legacy-to-new migration preserves the old consumer URL.

## Optional channel distribution

After the core endpoints work, the facilitator can arrange Teams/Microsoft 365
distribution using the current [publishing guide](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot).
Check tenant policies, permissions, and the available portal flow first. Never
invent a public publishing API. Channel distribution is a separate outcome
requiring its own approval and tests, not a side effect of creating an agent.

## End of workshop

Show the two prompt-agent endpoints, hosted workflow endpoint, and capstone
endpoint, their verified versions, evidence locations, and every workshop-owned
resource still running.
Ask before stopping or deleting specific
resources. Keep shared projects/models and other students' resources untouched.
If cleanup removes an endpoint, label it retired in the release record rather
than continuing to claim it is callable.
