# Agentic Workshop in the GitHub Copilot App

Learn to build and test Microsoft Foundry agents with **GitHub Copilot as your
coach**. Follow the original workshop's concept sequence:

**Hello agent -> tools -> multi-turn conversations -> memory -> workflows ->
remote MCP.**

First explore these concepts with **prompt-based agents**, then with **hosted
agents**. Refine instructions, work with skills, and release tested versions
through stable, authenticated Foundry endpoints. At the end, apply what you
learned to a capstone of your choice.

Alongside agent development, learn to use the **Copilot app itself**: asking for
explanations or implementation, reviewing changes, inspecting tool calls,
working with sessions, and choosing between Chat and available visual tools.
VS Code is not required.

## Start here: no agent selector required

1. Open the workshop repository supplied by your facilitator as a project in
   the **GitHub Copilot app**.
2. Start a **normal Chat session in that project**, so Copilot can read the
   workshop files. You do not need to find or select "Workshop Coach".
3. Type:

   > Start the workshop.

Copilot will welcome you, explain how the guided lessons work, check that it can
read this repository, and help you through setup one question at a time. You do
not need to know an agent name, internal file path, or Azure command to begin.
If you already have local progress, the coach will help you resume safely.

**New to the app or not sure what to open?** Follow the
[participant start guide](workshop/START.md). You can also ask "How do I start
this workshop?" in the repository chat to get orientation before beginning.

The facilitator supplies the app-access instructions and the workshop repository
revision. Azure setup comes after the welcome; opening the project or sending
the starter message does not authorize creating paid resources.

## Learning path

| Stage | Agent concepts | Copilot app practice |
|-------|----------------|----------------------|
| 00 | Setup and resource ownership | Read repository context; understand approvals |
| 01-06 | Prompt hello agent, tools, conversations, memory, workflows, MCP | Explain vs implement; inspect calls; resume sessions; plan small changes |
| 07-08 | Instructions, versioned skills, prompt release | Review diffs; distinguish coach skills from runtime skills; verify outcomes |
| 09-13 | Hosted hello agent, tools, conversations/memory, workflows, MCP | Inspect generated files; compare local/remote evidence; troubleshoot precisely |
| 14-15 | Hosted runtime skills, release, rollback | Compare versions; use supported Canvas workflows when available |
| 16-18 | Choose, implement, and release a capstone | Write a scoped brief; review changes; demonstrate and hand off |

Every capability follows **predict -> change -> test -> explain -> checkpoint**.
The coach teaches one small change at a time and introduces one app technique
plus a useful alternative. Students do not have to complete the lesson twice.

## Capstone choices

The early exercises use small examples from the original workshop: greetings,
synthetic weather, conversation context, text transformations, and documentation
lookup. They are not a semester-long IT support project.

At the end, choose **IT support**, **a documentation research assistant**,
**a fictional travel-planning assistant**, or **your own approved scenario**.
Use synthetic/public data. The [capstone guide](workshop/CAPSTONE.md) defines
equivalent acceptance criteria and what extra infrastructure each choice needs.

## Workshop material

- [Checkpoint map and student controls](workshop/README.md)
- [Setup](workshop/SETUP.md) and [Copilot app techniques](workshop/APP-GUIDE.md)
- [Prompt-agent lessons](workshop/01-prompt-agents.md)
- [Hosted-agent lessons](workshop/02-hosted-agents.md)
- [Tests](workshop/TESTS.md) and [stable-endpoint release](workshop/PUBLISHING.md)
- [Capstone choices](workshop/CAPSTONE.md) and [facilitator guide](workshop/FACILITATOR.md)

Student implementations live in `student/`; local progress and sanitized test
evidence live in ignored `.workshop/` files. The coach is a formative tutor, not
an independent examiner or a secure grading system.

**Foundry terminology:** new-model agents receive a stable endpoint on creation.
Release checkpoints verify version selection and consumer access, not a separate
endpoint publishing operation. Teams/Microsoft 365 distribution is optional;
legacy Agent Applications are explained in the publishing guide.

## Original examples

| Folder | Role in this workshop |
|--------|-----------------------|
| [01-agent-framework](01-agent-framework/README.md) | The original six-step concept sequence and Python references |
| [02-microsoft-foundry-agents](02-microsoft-foundry-agents/README.md) | Prompt-agent creation and conversation references |
| [05-github-copilot](05-github-copilot/README.md) | Original VS Code tutorial; optional IT support capstone reference |

The root `requirements.txt`, `example.env`, and `Prereqs*.md` belong to those
original examples. New student projects use isolated environments appropriate
to current SDKs. Console samples are not ready-made hosted deployment servers.
