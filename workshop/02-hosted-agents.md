# Hosted agents: repeat the concepts with custom execution

Keep the tested prompt release. Build a separate hosted practice agent, adding
one capability at a time. Do not port every capability in the scaffold. Hosted
code adds custom execution and operational responsibilities; tools and memory
alone are not reasons that every agent must be hosted.

Use [TESTS.md](TESTS.md) and [APP-GUIDE.md](APP-GUIDE.md). Use a current official
hosting sample and the installed Foundry skill workflow, not an old console
script as a server entry point.

## 08: Hosted hello agent

Verify hosting support, CLI/extensions, runtime, project, and cost boundary.
After approval, scaffold the smallest appropriate
[official sample](https://github.com/microsoft-foundry/foundry-samples) in
`student/hosted-agent/`, with its own dependency environment. Record sample
source/revision and dependency versions. Preserve the hosting protocol and
health behavior. Add only the neutral baseline instructions from 01.

Run the local server and B01-B03. Pause to explain those results. Then request
approval for the specific remote deployment, deploy into the agreed project,
inspect running/healthy state, and run B01-B03 remotely. A console response or
successful build is not proof of a hosted endpoint.

**App practice:** inspect the generated entry point and configuration before
running them; identify the files responsible for hosting.
**Alternative:** a supported hosted-agent operation can use Foundry Canvas when
available and applicable under the app's routing rules. Chat remains the path
for explanation, mixed tasks, and troubleshooting. Resume the learning gate
after any Canvas handoff.
**Teach-back:** "What does local success prove, and what does remote success add?"

## 09: Hosted tools

Introduce the deterministic weather fixture as a validated, allowlisted
function in the hosted runtime. Reference
[add tools](../01-agent-framework/02_add_tools.py) for the idea, adapting to the
current SDK. Keep the fixture labeled as synthetic. This is the first required
custom executable function in the workshop; unlike a prompt-agent function-call
schema, its implementation is packaged with the hosted runtime.

Run T01-T03 directly and through the local agent, then deploy the approved
change and run them remotely. Explain why consumers no longer execute this
function themselves. Keep errors visible and never execute arbitrary code
returned by the model.

**App practice:** request a change to just the function and its tests; review
the diff before deployment.
**Alternative:** ask for a hint or explanation before asking Copilot to implement.
**Teach-back:** "What moved from the client into the hosted runtime?"

## 10: Hosted conversations, then memory

Teach these as two substeps, each with its own test and pause.

**First, conversations:** implement supported per-conversation session handling.
Run D01-D02 before connecting persistent memory, locally and remotely. Inspect
the IDs and state boundaries. A global shared session is not a valid solution.

**Then, memory:** connect a dedicated store with the same narrow preference
policy as 06. Use a trusted identity-to-scope mapping and the documented write/
read paths. Do not assume prompt-agent automatic memory behavior exists in the
hosted SDK. Reuse the prompt store only with explicit approval and compatible
scope/ownership boundaries.

Run M01-M03. Restart locally and repeat recall without replaying history. After
approved deployment, repeat remotely across a controlled restart/redeployment.
Neither a global dictionary nor the container filesystem proves persistence.
If identity isolation cannot be implemented, block multi-user release.

**App practice:** compare the coach session, runtime session, and memory scope.
**Alternative:** use a fresh app session for independent work only when useful;
pass relevant artifact paths and do not assume prior chat context transfers.
**Teach-back:** "Which state survives a restart, and how are users separated?"

## 11: Hosted workflow

Introduce the deterministic uppercase -> reverse graph in the hosted request
path. Keep the stages observable. Reference
[first workflow](../01-agent-framework/05_first_workflow.py) for graph concepts.
Use the model only to explain the computed output, not to impersonate execution.

Run W01-W02 locally and remotely. A controlled intermediate failure must stop
the graph and reach the caller explicitly, without a fabricated final result.
Contrast this executable workflow with the prompt release, which contains no
custom workflow code.

**App practice:** present a reproducible input, observed failure, and expected
result when requesting diagnosis. Ask for a focused fix.
**Alternative:** inspect sanitized logs in an available terminal or via Chat;
do not require a particular debugging UI.
**Teach-back:** "Where does this workflow execute now, and why is its order reliable?"

## 12: Hosted remote MCP

Connect the same two approved read-only MCP services from 04, with explicit
tools, authentication, provenance, and approval handling. Run C01-C03 locally
and remotely. Confirm the deployed identity and network path rather than
assuming developer access transfers.

Keep the core exercise read-only. The old ticketing MCP demo is an optional
capstone reference, not a required shared service for this lesson. Foundry cannot
reach a laptop's localhost. Never tunnel the unauthenticated demo onto the
internet to avoid arranging a supported endpoint.

**App practice:** inspect connection configuration and execution location.
**Alternative:** compare direct MCP configuration with a supported Foundry
Toolbox when useful; do not add a Toolbox merely to demonstrate another UI.
**Teach-back:** "Which permissions and network path changed when we deployed?"

## 13: Hosted runtime skills

Reuse the versioned `explain-results` skill from 05. Integrate a current supported
skills provider: approved skill download or compatible Toolbox MCP resources.
Show discovery and loading, not merely a Markdown file in the image.

Configure the runtime identity's access, pin a skill version for the controlled
release, and record provider cache behavior. Run I01 and S01-S02. Test one skill
change, deliberately activate it, observe the result, and roll back. Restart or
redeploy when the provider requires it.

Keep authorization outside the skill. A skill asking permission is not an
approval mechanism. Contrast runtime loading with prompt static composition.

**App practice:** review the skill-only diff and loaded version before changing
the active configuration.
**Alternative:** use a separate branch/worktree for a larger experiment, but
first verify which source and local evidence it contains.
**Teach-back:** "How do you know which skill content this process loaded?"

## 14: Hosted release

Follow [PUBLISHING.md](PUBLISHING.md) and run P01-P04. Demonstrate the same
consumer endpoint across upgrade and rollback. Record what remains running.

**App practice:** request a precise release handoff and compare it with live
endpoint/version evidence.
**Alternative:** use applicable supported Canvas controls when available,
without treating the handoff itself as success.
**Teach-back:** "Which responsibilities belong to your hosted code rather than Foundry?"

Then proceed to [capstone selection](CAPSTONE.md). Students now have the concepts
needed to choose an architecture for their own scenario.
