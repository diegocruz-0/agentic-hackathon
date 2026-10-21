# 00: Connect the Copilot app to the workshop environment

**Outcome:** verify or help the participant create their dedicated Microsoft Foundry Project,
reuse a suitable existing Model Deployment or create one after explicit
approval, know where the coach and agents run, and inventory which
capabilities can actually be used. Do not create an agent at this step.

## Student experience

Follow the [participant start guide](START.md): in the GitHub Copilot app's
repository project, select **Workshop Coach**, then say **"Start the workshop."**
Use normal repository Chat only if the app has no agent selector.
The coach welcomes you before asking for setup information, checks
saved progress, and helps with one missing value at a time. There is no VS Code
extension setup in the core path.

The facilitator confirms organizational access and any managed-install policy.
Use the official links below rather than copied installers or guessed commands.
Verify that the app can read the repository and use its execution environment.

Every participant uses one dedicated Microsoft Foundry Project. They may create
it before the workshop or create it themselves at checkpoint 00 with coach
guidance after confirming the target and possible costs. The facilitator does
not assign the project name or endpoint. Follow this opening order: welcome and
explain the workshop, confirm which Microsoft account the participant wants to
use, then ask for the actual Project Endpoint. If they do not know the endpoint
or do not yet have a project, help them safely locate or create their own
project. The coach does not create it on their behalf or switch projects
silently. The shared story creates and enhances the Weather Research Agent,
repeats the evidence loop for the Cultural Travel Agent, then introduces hosted
workflow code. Capstone choice comes later.

**App practice:** ask the coach to explain repository context without making
changes, then compare that read-only request with asking it to perform a
specific change. Starting the workshop does not grant blanket permission to
change Azure resources. Selecting Workshop Coach chooses the coaching profile;
it does not create a Foundry agent or grant Azure permissions.

## Minimum environment, then just-in-time additions

| When | Needed | What the coach verifies |
|------|--------|------------------------|
| Start | Copilot app access, Git, repository workspace | Repo instructions load; branch/worktree is the student's |
| Participant project | Participant chooses the signed-in Microsoft account to use; coach execution identity can access the exact project and has the required permission for the current approved step; participant can create a dedicated project if one is not already available | Confirm the identity actually used by the Foundry request matches the participant's choice, then directly verify project identity and operation-specific permission; no shared or silently substituted project |
| Workshop model | Microsoft Foundry Model Catalog access, usable project quota, and model-deployment permissions | Inspect existing deployments first; participant chooses whether to reuse a suitable one or independently selects a compatible model and explicitly approves a new named deployment and possible cost |
| SDK fallback | Python and isolated environment | Use the current prompt quickstart's package versions in the student implementation |
| Weather MCP | Approved reachable read-only weather endpoint | Protocol, authentication, allowlist, upstream provenance, Foundry-side reachability |
| Cultural Travel MCP | Facilitator-owned Cloudflare authless MCP Worker | Stateless Streamable HTTP endpoint, narrow read-only tools, dataset license/version, input bounds, logs, and Foundry-side reachability |
| Memory | Chat and embedding deployments, memory capability | Store permissions, identity scope, retention, update behavior |
| Skills | Skills API and compatible client/provider | Upload/version/retrieve support; MCP resources support is distinct from tools |
| Hosted workflow | Azure Developer CLI (`azd`), Agent Framework, supported Foundry extensions/runtime, and tracing | Current sample, runtime, both downstream endpoints/contracts, deployment support, quota/cost boundary |
| Consumer access | Approved test caller identities | Endpoint invocation permission and a caller without permission for the negative test |

Use the installed `microsoft-foundry` skill, including its dependency check and
workflow instructions, when available. Otherwise follow the official references
below using available tools. Do not claim an integration exists just because
this repository mentions it.

Read-only checks can include current CLI versions, signed-in account summary,
project metadata, available catalog models, and quota. Students
complete interactive sign-in themselves. Do not dump credential-bearing
environment variables or tokens. The participant chooses independently from the
Microsoft Foundry Model Catalog. The coach may recommend considering a
compatible mini-class model to reduce cost and quota use, but must not make the
choice or imply that the facilitator provides the model.

Before creating a project, confirm the participant's intended target and
acknowledgment that the operation may incur cost. At the start of checkpoint
00, after the welcome and workshop overview, ask which signed-in Microsoft
account the participant wants to use for Foundry. Offer the currently signed-in
account if it can be identified safely, an approved sign-in flow for a different
account, and freeform input. Do not request credentials. After account
confirmation, ask for the exact Project Endpoint; do not ask whether the
participant already has a project first. Verify the identity used by the actual
Foundry request matches the participant's selection; `az account show` does not
prove which identity Foundry MCP uses.

With multiple signed-in accounts, use a separate workshop CLI profile through
a process-scoped `AZURE_CONFIG_DIR` outside the repository. Have the participant
sign in interactively and confirm the exact account, tenant, and subscription;
tenant selection alone does not select a user. Run the read-only SDK check
with explicit `AzureCliCredential` in that same profile, not an automatic
credential chain. Do not change global profile settings or sign out unrelated
accounts. An already-running MCP server does not automatically inherit these
settings; verify its authentication source separately and distinguish its
results from the selected-account SDK check.

Before each Foundry resource inspection or operation, check Azure CLI
availability and `az login` status in the execution context that will perform
it. `az account show` confirms account context only, not access to the Foundry
Project or permission to create resources. Immediately after receiving the
project endpoint, make a direct authenticated request to that exact project and
confirm its identity. Then verify the operation-specific permission required
for the current step; read-only access alone is insufficient to create
resources. Never probe write access by creating a throwaway resource, print or
request credentials, broaden permissions, or switch identities without
approval. Use the existing authenticated context for read-only discovery and
approved operations. If sign-in, direct project access, or required permission
is unavailable, state which check failed and pause before recommending or
performing the operation.

Once direct project connectivity and the current step's permission are
verified, inspect its existing model deployments in Microsoft Foundry before
asking for a model name/version or proposing reuse or a new deployment.

Once the project is confirmed and directly readable, inspect its existing
model deployments in Microsoft Foundry before asking for a model name/version
or proposing reuse or a new deployment.
If a suitable deployment exists, show its directly verified deployment name,
model/version, status, and project, then ask whether the participant wants to
reuse it. A project endpoint is not a resource ID; use supported discovery
rather than reconstructing an ID. Do not ask the participant to inspect the
portal in place of the coach's lookup or treat their report as independent
verification.

If no suitable deployment is selected, the participant independently chooses a
compatible model from the Microsoft Foundry Model Catalog. After the selection,
check once more for an existing deployment matching that model name/version
before asking for a new deployment name. Before creating a new deployment,
confirm the participant's project, model name/version, deployment name, and
acknowledgment that creation may incur cost. Before reuse, confirm the exact
target and the participant's explicit choice; explain that model usage may
still incur cost. Detailed region, SKU, capacity, quota, and pricing review is
not required for the core lesson unless the selection or an error makes it
necessary. Create only the participant's dedicated project and only an
explicitly approved new deployment inside it, then inspect the result.

## Official installation links

Install tools just in time, not all at workshop startup. On organization-managed
devices, follow the facilitator's software-distribution policy even when an
official public installer exists.

| Tool or service | Needed | Official link |
|-----------------|--------|---------------|
| GitHub Copilot app | Before checkpoint 00 | [App download page](https://github.com/features/ai/github-app) and [getting-started guide](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app) |
| Git | Before checkpoint 00 | [Git downloads](https://git-scm.com/install/) |
| Microsoft Foundry portal | Checkpoint 00 onward | [Open Microsoft Foundry](https://ai.azure.com/) |
| Python | Only when a lesson needs the SDK or the hosted scaffold | [Python downloads](https://www.python.org/downloads/) |
| Foundry development tooling | Before SDK-based Foundry work | [Prepare the Foundry development environment](https://learn.microsoft.com/azure/foundry/how-to/develop/install-cli-sdk) |
| Azure CLI | Only when the selected authentication or diagnostic path requires it | [Install Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) |
| Azure Developer CLI (`azd`) | Before hosted checkpoint 15 | [Install Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) |

Do not install VS Code for the core workshop. Do not use direct installer URLs
copied into the curriculum; the official pages select the current supported
package and include operating-system-specific instructions.

## Choose the actual resource boundary

Use only the participant's own dedicated project, whether prepared before the
workshop or created by the participant at checkpoint 00. Record the confirmed
subscription, project endpoint, ownership, participant-created model deployment,
and a unique student prefix in `.workshop/progress.json`. Also record exact
resource IDs when resources are created later, with `owned_by_student` and
`cleanup_approved` flags.

An existing project endpoint is not an ARM resource ID. Resolve resource IDs
through supported discovery; do not reconstruct them from guessed names.
Do not create new infrastructure or change IAM to bypass missing access.

The facilitator must preflight all later capabilities. At checkpoint 00, mark
each capability `available`, `unavailable`, or `unverified`, with evidence.
Initial prompt access must work to pass 00. Later capabilities can be unverified
at this point, but their own checkpoints cannot pass until verified.

## Student workspace

The coach creates only files needed for the current lesson:

```text
student/
  prompt-agents/      Both agent definitions, tests, isolated dependencies
  skills/            Student-authored SKILL.md packages
  hosted-agent/      Trip Planning Workflow and result contracts, added at checkpoint 15
  capstone/          Chosen final project, added at checkpoint 17
.workshop/
  progress.json      Local progress, never committed
  evidence/          Sanitized test observations, never committed
```

Source artifacts under `student/` can be reviewed and committed by the student.
Keep secrets in an appropriate secret store or ignored environment files.
Do not commit local transcripts or endpoint response dumps under `student/`.

Create a separate dependency environment and dependency manifest for each
implementation under `student/`. The current prompt quickstart
requires Azure AI Projects 2.x (currently `>=2.3.0`). Verify current requirements
at execution time and record the versions actually used. Confirm the Python
version required by the selected hosted runtime before installation.

## Approval and costs

Model tokens, embedding calls, memory, built-in tools, hosted compute, supporting
services, and telemetry can incur charges. Before creating/changing resources,
agree on the target, scope, and cost boundary. Reusing a project does not make
operations free. Pausing a lesson does not stop hosted compute.

For private projects, use the organization's supported network path. Do not
relax network restrictions to get through a workshop.

## Checkpoint

**Pass evidence:** repository access; participant project identity and ownership;
direct connection to the exact Microsoft Foundry Project; verified permission
for the current approved operation (including deployment creation if needed);
participant-confirmed choice to reuse a suitable existing deployment or
explicit approval for a new Model Deployment observed in the project; recorded
capability inventory; confirmed distinction between facilitator-provided and
participant-owned resources.

**Teach-back:** "Which agent is coaching you, which will run in Azure, and how
can you request an explanation without authorizing a change?"

## Current references

Use these before generating version-sensitive API calls or CLI syntax. Preview
features and publishing terminology can change; verify commands against these
references before use.

- [Foundry prompt-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent)
- [Hosted agents](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry)
- [Official Foundry samples](https://github.com/microsoft-foundry/foundry-samples)
- [MCP tools](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol)
- [Cloudflare authless remote MCP template](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/)
- [Cloudflare Workers limits](https://developers.cloudflare.com/workers/platform/limits/)
- [Memory stores](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage)
- [Skills](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills)
- [Current agent model and stable endpoints](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications)
- [Legacy Agent Applications](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agent-applications)
- [Custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
