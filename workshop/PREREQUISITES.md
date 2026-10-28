# Before the Agentic Workshop: participant prerequisites

Build two Microsoft Foundry agents and a coordinating workflow, guided by
**Workshop Coach in the GitHub Copilot app**. No prior agent development
experience is required. Prepare the following before attending; contact your
facilitator if anything is blocked.

Plan for **5-6 hours including breaks** for the guided two-agent-and-workflow
build. A capstone using your own scenario is an optional follow-on. Ready
prerequisites help protect hands-on time; access problems may require separate
facilitator support.

## 1. Prepare your device and Copilot access

Bring a computer with a web browser and permission to run organization-approved
tools. Install:

| Tool | What it is and why you need it |
|------|-------------------------------|
| [GitHub Copilot app](https://github.com/features/ai/github-app) | Your AI-assisted workspace, where Workshop Coach guides you through building agents and reviewing results. |
| [Git](https://git-scm.com/install/) | A version-control tool that lets the app retrieve workshop files and track your changes. |

Sign in to the app with a GitHub account that has the required Copilot access.
Open the repository link and exact revision supplied by your facilitator.
Your network must allow GitHub, Microsoft sign-in, Foundry, and the approved
Azure services; do not disable security controls.

The coach supplies the two selected public
[MCP services](MCP-SERVICES.md) during the lessons. These provide callable
weather and cultural-travel tools without a service account or API key. You
do not need a Cloudflare account or to build or host an MCP server. Your
network must allow `weather.datakoot.com` and `mcp.travel.art`; ask your
facilitator for help if either is blocked. Foundry still requires the Microsoft
account and Azure access below.

**Other required tools are checked in the coach's execution environment:**
Azure Command-Line Interface (CLI) is required before the first Foundry check;
Python and Foundry software development kit (SDK) packages run workshop code
and connect to Foundry; Azure Developer CLI (`azd`) deploys the later hosted
workflow. They may already be available. A facilitator can help prepare an
isolated environment in advance to avoid installations during teaching;
otherwise the coach guides missing-tool setup when needed.
**VS Code is not required.**

An optional advance readiness session checks installed tools and, after you
confirm your account/project and agree to read-only checks, access and later
lesson prerequisites. It does not build your agents, send paid test prompts
or authorize resource changes. The live workshop still confirms your account
and exact project. Flag missing memory, release or hosting support early rather
than discovering it near the end.

## 2. Prepare your Microsoft account and Azure access

Sign in to [Microsoft Foundry](https://ai.azure.com/) with your intended
Microsoft account, which may differ from your GitHub account. Arrange an
approved Azure subscription with access, permissions, and quota for projects,
models, and agents; ask your facilitator or administrator for access help.

**Signing in alone is not enough.** Ask your administrator to arrange Azure
roles at the appropriate resource scope:

| Activity | Access needed |
|----------|---------------|
| Build and test agents | **Foundry User** on the Foundry resource or appropriate project scope. |
| Publish agents during release lessons | **Foundry Project Manager** on the parent Foundry resource; this also supports agent development. |
| Create a project or deploy models | Additional management permissions, such as **Foundry Account Owner** on the Foundry resource; creating the resource itself requires permissions on the target resource group. |
| Inspect traces and query logs | **Log Analytics Reader** on connected telemetry resources; protected tables may require additional read access. |
| Deploy the hosted workflow | Permissions for supporting Azure resources and runtime identities, checked during deployment preparation. |

For a prepared environment, request **Foundry Project Manager** on your
dedicated Foundry resource plus telemetry-read access; an administrator can
prepare model deployments and supporting resources. Subscription-wide Owner
or Microsoft 365 Global Administrator access is not required. Azure
**Contributor alone does not grant Foundry agent data access**.
You may see the older role names **Azure AI User**, **Azure AI Project Manager**,
and **Azure AI Account Owner** in the portal. See
[Microsoft's Foundry role reference](https://learn.microsoft.com/azure/foundry/concepts/rbac-foundry).

Use **one dedicated Foundry Project**, the workspace for your agents and
connections, not a production project. Prepare your own project in advance or
create it yourself with coach guidance during checkpoint 00 (setup), after
confirming costs. The facilitator does not assign its name or endpoint.
If it exists, have its name and **Project Endpoint** (service address) ready;
the coach can help you locate it.

**Do not create a model deployment just for preparation.** A deployment makes
a model available to your agents. The coach checks existing deployments first;
you choose whether to reuse one or approve a new model deployment and its cost.

## 3. Prepare Application Insights for trace inspection

**Connect Application Insights to your project and arrange telemetry-read
access.** This Azure service stores execution records called **traces**, which
show what an agent actually did.

For an existing project, arrange this before attending; for a project created
during setup, plan it with the coach then. Follow
[Microsoft's tracing setup guidance](https://learn.microsoft.com/azure/foundry/observability/how-to/trace-agent-setup).
Ask your administrator about **Log Analytics Reader** access and any extra
permissions needed for protected log tables.

The coach checks readiness on the first project connection and before trace
exercises. A working model reply does not prove tracing is enabled.
Connecting or creating telemetry resources requires explicit approval and can
incur storage and ingestion costs; earlier executions may not appear afterward.

## 4. Agree on costs and safe practice data

Agree on an approved spending arrangement: models, memory, hosted compute,
and telemetry can incur charges, even with existing resources. The coach asks
for approval before changes or paid tests and shows available Foundry model
usage and cost estimates, excluding Copilot coaching and other service charges.

Use only **public or synthetic data**; traces may capture prompts and replies.
Never share credentials or confidential files. Agree on resource cleanup;
pausing a lesson does not stop paid Azure resources.

## 5. Be ready to start in the Copilot app

After cloning the repository provided by your facilitator (downloading a local
copy), open it as a project in the **GitHub Copilot app**, start a session,
select **Workshop Coach** in the agent selector, and send:

> Start the workshop.

The coach welcomes you and explains the workshop, then asks how experienced
you feel with **Microsoft Foundry** and the **GitHub Copilot app**, separately.
Choose Beginner, Intermediate or Advanced, or describe it in your own words.
The answers tailor explanations and navigation, not the goals or safety checks.
Setup starts next without another start command. You can say "explain more"
or "keep it brief" at any time; saved preferences are reused when you resume.

The core includes reusable **Foundry tool connections** and **Toolboxes**
(managed collections of tools). Your project must support their management
and your agents' runtime access; the facilitator checks this before delivery.
Public Weather/travel.art services require no keys, but that does not remove
Foundry permissions or possible costs. No VS Code setup is required.

You can also request coaching in your preferred language, for example:

> Start the workshop. Guide me in Swedish, and explain technical terms in
> Swedish with their English names in parentheses.

Replace Swedish with your preferred language. Keep resource names, commands,
code, and portal labels unchanged so you can match them to the actual tools.
The coaching language does not automatically change your Foundry agents'
instructions or test prompts. Ask your facilitator which languages have been
rehearsed for this workshop.

If there is no agent selector, use normal repository Chat. If the selector
exists but Workshop Coach is missing, use the [start guide](START.md) or ask
your facilitator; availability depends on the app build and configuration.

The coach runs in Copilot; your agents run in Foundry. The coach states when
to use the portal for inspection or testing. Do not duplicate tests in both places.

## Final readiness check

- [ ] I can sign in to the GitHub Copilot app and open the supplied repository revision.
- [ ] Git is installed, and I can install approved additional tools when needed.
- [ ] I know which Microsoft account and approved Azure subscription I will use.
- [ ] I can access my dedicated Foundry Project, or have arranged to create it during setup.
- [ ] Application Insights and telemetry-read access are ready, or I have flagged the setup needed with my facilitator.
- [ ] I understand that Azure usage can incur costs and will use only public or synthetic data.

If any item is blocked, contact your facilitator before the workshop. You do
not need to create agents, run paid model tests, or deploy a workflow in advance.
