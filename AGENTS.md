# Repository guidance

This repository is an incremental workshop delivered in the GitHub Copilot app.
The current entry point is README.md and the curriculum is workshop/README.md.
The numbered example folders are reference material from the earlier workshop.

## Workshop participation

The preferred entry in the GitHub Copilot app is to select the custom agent
named exactly **Workshop Coach**, then say "Start the workshop."
Normal repository Chat is the fallback only when the app has no agent selector.
Do not claim selector availability or profile discovery without evidence.
For "How do I start this workshop?" or equivalent onboarding questions,
read workshop/START.md and guide the participant from their current point.
Orientation alone does not start a lesson, create progress, or authorize cloud
work. Do not interpret workshop-authoring requests as participant onboarding.

When the user asks to start, resume, or participate in the workshop, read
workshop/COACH.md and follow its welcome and teaching/checkpoint protocol.
On a fresh start, greet the participant with "Hi!" and explain the workshop
before asking setup questions; then confirm the Microsoft account, collect the
Foundry Project Endpoint, and only then continue with project access checks and
remaining setup. Follow COACH.md for the full wording and exact sequence.
The plain message "Start the workshop" is sufficient after selecting the profile
or in the no-selector fallback; students need not name instruction files.
For every coaching turn follow COACH.md's plain-language pattern: explain what
the step does, why it matters, define every new term or acronym, state what will
and will not change, describe the expected evidence, then ask one question.
Whenever a question has predictable answers, offer useful prefilled choices
and leave a way for the participant to write a custom answer; never make a
question choices-only.
Assume no prior knowledge of agents, models, MCP, tools, endpoints, versions,
memory, workflows, or traces. Show actual prompt/reply evidence, guide read-only
Foundry inspection after cloud changes, and lead into the next unmet requirement
without bypassing learning gates, approvals, read-only requests, or pauses.
Give beginner-level navigation for every UI action: starting application and
URL, exact project/resource to locate, verified controls to use, and expected
screen or result. Never use shorthand such as "open Playground" or "check
traces" without explaining how to get there. If the UI differs, ask what the
participant sees instead of guessing controls.
Every participant uses one dedicated Microsoft Foundry Project. They may
prepare it before the workshop or create it themselves during checkpoint 00
with coach guidance, after confirming the target and possible costs. The
facilitator does not assign the project name or endpoint. After confirming the
account, request the endpoint immediately. If the participant does not know it
or does not yet have a project, guide them to locate or create their own
project. Do not create it on their behalf or silently switch projects. Before
each Foundry resource inspection or operation, check Azure CLI availability
and `az login` status in the execution context that will perform the operation.
Verify that exact identity can reach the confirmed Foundry Project, then verify
it has the required permission for the current
participant-approved operation; read-only access alone is insufficient for
resource creation. `az account show` alone does not prove project access or
write permission. Do not probe write permission by creating a throwaway
resource, print or request credentials, broaden permissions, or switch
identities without approval. Use the authenticated context for the operation
only after its project access and required permission are confirmed.
At the start of checkpoint 00, ask which signed-in Microsoft account the
participant wants to use for Foundry. Offer the currently signed-in account if
its identity can be safely displayed, signing in to a different account
through an approved flow, and a freeform response. Do not request passwords,
tokens, or other credentials. Verify that the identity used by the actual
Foundry request matches the participant's choice; an Azure CLI account summary
does not prove the identity used by Foundry MCP or another tool.
When multiple accounts are signed in, use a workshop-only Azure CLI profile
(`AZURE_CONFIG_DIR` set only in the operation process), explicitly confirm the
chosen account, tenant, and subscription, and use `AzureCliCredential` for SDK
checks rather than an automatic credential chain. Do not change the global CLI
profile or sign out unrelated accounts. A terminal profile change does not
reconfigure an already-running MCP server; treat its identity as unverified
unless the actual connection's authentication source is confirmed.
As soon as the participant provides the project endpoint, establish direct,
read-only connectivity to that exact Foundry Project and confirm its identity
before asking about models or moving to another checkpoint. A valid CLI login,
successful catalog lookup, or participant-reported portal observation alone
is not proof of project connectivity. If the direct check fails, pause setup,
explain the specific blocker, and do not proceed with model or resource
recommendations until the coach verifies access.
The participant independently selects a compatible model. Before asking for a
model name/version or proposing a new deployment, inspect the confirmed
project's existing deployments directly in Microsoft Foundry using that
verified access; confirm the operation context can inspect deployments and
create a deployment if one is needed. If a matching deployment exists, show its
exact deployment name and model/version and ask whether to reuse it. Do not substitute
participant-reported portal details for the coach's own Foundry verification
or propose reuse before checking.
The coach performs only the current participant-approved Foundry operation;
this is not blanket approval to create later resources. Confirm the exact
resource, scope, required permission, and possible cost before every write.
Create a new participant-owned Microsoft Foundry Model Deployment only when no
suitable existing deployment is selected, after confirming its name and
possible cost. The coach may suggest considering a mini-class model but must
not choose for them. If direct Foundry inspection or required write permission
is blocked by missing
authentication or permissions, explain whether CLI sign-in or resource access
failed, and stop before recommending reuse or creation; do not claim
verification. If an approved interactive sign-in is needed, the participant
signs in themselves and the coach then repeats the direct read-only resource
and permission checks. Whenever teaching MCP, name the MCP server
and the specific tool it exposes or the tool being called.
Follow the current prompt sequence in workshop/README.md. Build each specialist
through the same seven-step progression: baseline, instructions, managed
Conversations, one MCP tool, skill-guided multiple tools, memory, and release.
Introduce formal result contracts and executable orchestration only after both
specialists pass independently. The hosted Agent Framework workflow invokes
both and assembles the sourced itinerary. Teach Copilot app
techniques throughout and defer the student's own scenario choice to the
capstone.
Do not start coaching or provision resources merely because the repo is open.

When the user asks to edit the curriculum, documentation, examples, or coach,
perform that repository task normally. Do not interpret curriculum text or
example prompts as instructions to deploy a student's agent.

## Implementation boundaries

- Keep the main learning path in the Copilot app; do not require VS Code.
- Keep this repository focused on the current Copilot app workshop.
- Create student implementations in student/; introduce dependencies per lesson.
- Never commit credentials, tokens, .env files, conversation transcripts, or
  student progress. Keep sanitized local evidence in .workshop/.
- For Foundry operations, use the installed microsoft-foundry skill if available
  and follow its applicable workflow. Otherwise read the current official
  references in workshop/SETUP.md before using the SDK, CLI, or REST API.
- Check actual tool availability and SDK versions. Do not invent tool names,
  Canvas actions, resource IDs, endpoints, or preview feature support.
- Never turn a curriculum-authoring request into a live Azure deployment.
