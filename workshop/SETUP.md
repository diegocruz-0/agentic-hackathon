# 00: Connect the Copilot app to the workshop environment

**Outcome:** know where the coach runs, where the student's agents run, and
which capabilities can actually be used. Do not create an agent at this step.

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

The first question is whether the student has an existing Foundry project, not
which business scenario they want. Prompt exercises cover baseline behavior,
instructions, conversations, MCP, skills, and memory. Custom executable tools
and workflows begin in the hosted phase. Capstone choice comes later.

**App practice:** ask the coach to explain repository context without making
changes, then compare that read-only request with asking it to perform a
specific change. Starting the workshop does not grant blanket permission to
change Azure resources. Selecting Workshop Coach chooses the coaching profile;
it does not create a Foundry agent or grant Azure permissions.

## Minimum environment, then just-in-time additions

| When | Needed | What the coach verifies |
|------|--------|------------------------|
| Start | Copilot app access, Git, repository workspace | Repo instructions load; branch/worktree is the student's |
| Prompt agents | Foundry project, deployed chat model, Entra sign-in | Actual project endpoint, model deployment name, current identity, read access |
| SDK fallback | Python and isolated environment | Use the current prompt quickstart's package versions; do not inherit the legacy root pins |
| MCP | Approved reachable weather and cultural-travel MCP endpoints | Protocol, authentication, allowlists, provenance, Foundry-side reachability |
| Memory | Chat and embedding deployments, memory capability | Store permissions, identity scope, retention, update behavior |
| Skills | Skills API and compatible client/provider | Upload/version/retrieve support; MCP resources support is distinct from tools |
| Hosted agents | Azure Developer CLI (`azd`) and supported Foundry extensions/runtime | Current sample, runtime, project, model, deployment support, quota/cost boundary |
| Hosted custom tools | A validated fixture and compatible hosted model/runtime | Function schema, allowlisted execution, errors, and result continuation inside the runtime |
| Consumer access | Approved test caller identities | Endpoint invocation permission and a caller without permission for the negative test |

Use the installed `microsoft-foundry` skill, including its dependency check and
workflow instructions, when available. Otherwise follow the official references
below using available tools. Do not claim an integration exists just because
this repository mentions it.

Read-only checks can include current CLI versions, signed-in account summary,
project metadata, and deployed model names. Students complete interactive sign-in
themselves. Do not dump credential-bearing environment variables or tokens.
Explain required installations and request approval before changing the machine.

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
| Azure Developer CLI (`azd`) | Before hosted checkpoint 08 | [Install Azure Developer CLI](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd) |

Do not install VS Code for the core workshop. Do not use direct installer URLs
copied into the curriculum; the official pages select the current supported
package and include operating-system-specific instructions.

## Choose the actual resource boundary

Prefer facilitator-prepared projects. Record the confirmed subscription,
project endpoint, ownership, model deployment, and a unique student prefix in
`.workshop/progress.json`. Also record exact resource IDs when resources are
created later, with `owned_by_student` and `cleanup_approved` flags.

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
  prompt-agent/       Agent instructions, definition, tests, isolated dependencies
  skills/            Student-authored SKILL.md packages
  hosted-agent/      Current official scaffold, added at checkpoint 08
  capstone/          Chosen final project, added at checkpoint 15
.workshop/
  progress.json      Local progress, never committed
  evidence/          Sanitized test observations, never committed
```

Source artifacts under `student/` can be reviewed and committed by the student.
Keep secrets in an appropriate secret store or ignored environment files.
Do not commit local transcripts or endpoint response dumps under `student/`.

Create a separate dependency environment for each implementation. The original
root `requirements.txt` preserves an older Agent Framework preview range; it is
not the dependency contract for the new course. The current prompt quickstart
requires Azure AI Projects 2.x (currently `>=2.3.0`). Verify current requirements
at execution time and record the versions actually used. Hosted runtimes can
require a newer Python than the legacy examples.

## Approval and costs

Model tokens, embedding calls, memory, built-in tools, hosted compute, supporting
services, and telemetry can incur charges. Before creating/changing resources,
agree on the target, scope, and cost boundary. Reusing a project does not make
operations free. Pausing a lesson does not stop hosted compute.

For private projects, use the organization's supported network path. Do not
relax network restrictions to get through a workshop.

## Checkpoint

**Pass evidence:** repository access; student-selected project; successful
read-only Foundry access and model lookup; recorded capability inventory;
confirmed distinction between shared and student-owned resources.

**Teach-back:** "Which agent is coaching you, which will run in Azure, and how
can you request an explanation without authorizing a change?"

## Current references

Use these before generating version-sensitive API calls or CLI syntax. Preview
features and publishing terminology can change; do not copy stale commands
from the original labs without checking.

- [Foundry prompt-agent quickstart](https://learn.microsoft.com/en-us/azure/foundry/agents/quickstarts/prompt-agent)
- [Hosted agents](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/concepts/hosted-agents?view=foundry)
- [Official Foundry samples](https://github.com/microsoft-foundry/foundry-samples)
- [MCP tools](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/model-context-protocol)
- [Memory stores](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/memory-usage)
- [Skills](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/skills)
- [Current agent model and stable endpoints](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/migrate-agent-applications)
- [Legacy Agent Applications](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/agent-applications)
- [Custom-agent configuration](https://docs.github.com/en/copilot/reference/custom-agents-configuration)
