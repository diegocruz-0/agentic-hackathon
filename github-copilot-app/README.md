# Run the Agentic Hackathon from the GitHub Copilot app

The GitHub Copilot app provides a conversational way to create and improve AI agents.
Instead of beginning with every implementation detail, you can describe the agent you
want to build, the users it should help, the tools it may use, and the boundaries it
must follow. Copilot can then explore the workshop, ask or answer clarifying questions,
propose a plan, create the necessary files, run commands, and help you test the result.

This makes agent development an iterative conversation. You can begin with a goal such
as “create an agent that answers questions using official Microsoft documentation,”
review Copilot's proposed approach, and refine it with follow-up requests. As the agent
develops, you can ask Copilot to add tools, improve its instructions, diagnose a failed
run, or explain unfamiliar code. The **Plan**, **Files**, **Terminal**, and **Changes**
views keep that conversation connected to the real implementation, so you can move
from an idea to a working agent without losing visibility or control.

The GitHub Copilot app is an agentic workspace. It can read the repository, propose a
plan, edit files, and run commands in a terminal. That does not make every proposed
action correct. Think of Copilot as a capable workshop partner whose work you inspect,
not as an administrator that should make unreviewed decisions for you.

This workflow is based on the desktop app interface supplied for this workshop. The
interface includes repository sessions in the left sidebar and **Plan**, **Terminal**,
**Files**, and **Changes** views in a session. Optional plugins, such as Microsoft
Foundry, may appear in a side panel. GitHub can update labels or move controls, so use
the purpose of a control described here if its exact name has changed.

## First: understand the four views

You will move between these views repeatedly. Knowing why each exists makes the rest of
the workshop much easier.

| View | What it contains | Why you use it |
|------|------------------|----------------|
| **Plan** | Copilot's proposed steps for a task | Read this before execution so you know which files, commands, and services it intends to use. |
| **Terminal** | A command-line window and command output | This is where Git, Python, and Azure CLI actually run. Chat text alone does not install packages or execute a sample. |
| **Files** | The folders and files in the selected repository | Use it to open READMEs and source files and to confirm Copilot is working in the intended folder. |
| **Changes** | A before-and-after comparison of file edits | Review this before accepting work so accidental deletions, secrets, and unrelated edits do not slip through. |

The left sidebar keeps your **sessions**. A session is a conversation plus the
repository context and activity associated with one task. A session is not a separate
copy of your files. Two sessions that point to the same local repository can affect the
same files, which is why you should finish or pause one editing task before starting
another.

## Safety rules for this workshop

Follow these rules even if Copilot suggests otherwise:

1. Enter passwords, sign-in codes, API keys, and tokens only in the official sign-in
	experience or the local `.env` file. Never paste them into chat.
2. Review commands before allowing them to run, especially commands that install
	software, delete files, deploy resources, or modify Azure.
3. Review **Changes** before accepting edits. A confident explanation is not a substitute
	for reading the actual diff.
4. Do not ask Copilot to commit or push your work unless your instructor explicitly
	requests it.
5. Keep `.env` and `.venv` private and untracked. They can contain credentials or
	machine-specific packages.
6. Confirm the Azure subscription, Foundry project, model deployment, and expected cost
	before creating or publishing cloud resources.

## What you need

Complete the main [participant prerequisites](../Prereqs_Participant.md) before the
workshop. These tools have different jobs:

| Requirement | Why it is needed | Quick verification |
|-------------|------------------|--------------------|
| Git | Downloads the workshop and keeps track of file changes. | `git --version` prints a version. |
| Python 3.12+ | Runs the agent samples. Older Python versions are not supported by this workshop. | `python --version` prints 3.12 or newer. |
| Azure CLI | Signs your local Python code into Azure using your own identity. | `az --version` prints version information. |
| GitHub Copilot app | Provides the repository sessions, planning, editing, and terminal experience used by this guide. | The app opens and shows your signed-in GitHub account. |
| GitHub Copilot access | Allows the app to process prompts and work with code. | You can submit a simple question in the app without a subscription error. |
| Microsoft Foundry V2 project | Hosts the model and managed agents used in Labs 01, 02, and 04. Foundry V1 projects do not work with these samples. | You can open the project at [ai.azure.com](https://ai.azure.com/). |
| A deployed chat model | Produces the model responses used by the Python samples. The tested example uses a deployment of `gpt-4.1`. | The deployment appears under **Models + endpoints** in your Foundry project. |

To verify the command-line tools, open a PowerShell terminal and run each command on a
separate line:

```powershell
git --version
python --version
az --version
```

**Why run these checks first?** It is easier to fix one missing program now than to
diagnose a confusing Python or authentication error in the middle of a lab.

**Success looks like:** all three commands print version information, and Python reports
`3.12` or a newer version. A message such as “not recognized as the name of a cmdlet”
means the program is missing or is not on your `PATH`; install it and restart the app.

VS Code remains useful for the original inline-completion exercises in Lab 03, but it
is not required for the app-based path described below.

## 1. Clone the FY27 workshop

Cloning creates a local working copy of the workshop on your computer. The repository's
default branch is not the FY27 workshop, so the command must explicitly select the
`FY27` branch.

### Option A: ask the app to clone it

From **Home**, start a new task or session and enter:

```text
Clone the FY27 branch of https://github.com/haforsbe/agentic-hackathon.git into my
normal local source-code folder. Before running anything, show me the exact destination
and the git command. Do not overwrite an existing folder. After cloning, verify the
current branch and open the cloned repository as this session's workspace.
```

**Why ask for the destination and command first?** It prevents Copilot from cloning to
an unexpected directory or replacing an existing copy. Approve only a command that
contains both `--branch FY27` and the repository URL shown above.

### Option B: clone from a terminal yourself

Use this option if the app cannot start a terminal until a repository is open. Open
Windows PowerShell from the Start menu, choose a parent folder such as your Documents
or source-code folder, and run:

```powershell
git clone --branch FY27 https://github.com/haforsbe/agentic-hackathon.git
cd agentic-hackathon
git branch --show-current
```

Here is what each line does:

| Command | Explanation |
|---------|-------------|
| `git clone --branch FY27 ...` | Downloads the repository and checks out the FY27 workshop immediately. |
| `cd agentic-hackathon` | Moves the terminal into the newly downloaded folder. Commands in later steps assume this location. |
| `git branch --show-current` | Prints the active branch so you can verify that you did not accidentally clone the default branch. |

**Success looks like:** the clone completes without an error, and the final command
prints exactly `FY27`. The folder should contain `README.md`, `requirements.txt`, and
the numbered lab directories.

### If you already cloned the repository

Do not clone a second copy unless your instructor asks you to. Open a terminal in the
existing repository and run the following commands one at a time:

```powershell
cd agentic-hackathon
git status
git fetch origin
git switch FY27
git pull --ff-only origin FY27
```

`git status` checks for work that could conflict with the update. `git fetch origin`
downloads branch information without changing your files. `git switch FY27` selects
the workshop branch, and `git pull --ff-only` downloads newer FY27 commits only when Git
can do so without creating an unexpected merge commit.

**Stop if `git status` reports modified or untracked files you care about.** Ask the
instructor how to preserve them. Do not use `git reset --hard`, do not delete the files,
and do not let Copilot discard them merely to make the update succeed.

## 2. Open the repository in the app

The app needs repository context so it knows which files it may read and change.

1. Return to the GitHub Copilot app and select **Home** in the left navigation.
2. Choose the control for opening local work. Depending on the app version, it may be
	named **Open folder**, **Open repository**, **Add repository**, or **Start session**.
3. Browse to the `agentic-hackathon` folder itself, not its parent folder and not one
	individual lab folder.
4. Confirm or create the session.
5. Open **Files** and look for `README.md`, `requirements.txt`, `example.env`, and the
	folders beginning with `01-`, `02-`, `03-`, and `04-`.

**Why open the repository root?** The root contains the shared dependency file and
environment template. Opening only a lab subfolder can make relative paths fail and can
hide the shared setup files from Copilot.

**Success looks like:** `agentic-hackathon` appears under **Sessions**, **Files** shows
the complete workshop, and **Terminal** opens in a path ending in
`agentic-hackathon`. Run this command to confirm the path:

```powershell
Get-Location
```

If the path is wrong, change it with `Set-Location`, replacing the example path with
your real clone location:

```powershell
Set-Location "C:\path\to\agentic-hackathon"
```

Open a new chat for the repository and use this first prompt:

```text
Read README.md, Prereqs_Participant.md, and the README in each numbered lab folder.
Do not change any files yet. Summarize the workshop order, check my local prerequisites
from the terminal, and tell me the first failing prerequisite. Never request, display,
or write secrets in chat or source files.
```

The phrase “Do not change any files yet” matters: your first goal is orientation, not
implementation. Review the response in **Plan**. If the plan proposes editing files,
reply with “Keep this read-only and only report the prerequisite checks.” Use
**Terminal** to see actual command output rather than relying on Copilot's summary.

## 3. Prepare the Python environment

Python packages can conflict when different projects need different versions. A virtual
environment solves that problem by creating an isolated Python installation inside a
folder named `.venv`. Installing the workshop packages there avoids changing your
system-wide Python packages.

Run the following commands **one line at a time** in the app's **Terminal**. Waiting for
each command to finish makes it clear which command caused an error.

Windows PowerShell:

```powershell
python --version
git --version
az --version
python -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

What the Windows commands do:

| Command | Why you run it | Success looks like |
|---------|----------------|--------------------|
| `python --version` | Confirms the app's terminal can find Python 3.12+. | A version such as `Python 3.12.x`. |
| `git --version` | Confirms Git is available in the same terminal. | A Git version number. |
| `az --version` | Confirms Azure CLI is installed. | Azure CLI version details. |
| `python -m venv .venv` | Creates the isolated environment. It can take a few seconds and may print nothing. | A `.venv` folder exists and no error appears. |
| `Set-ExecutionPolicy ...` | Allows this PowerShell process to run the activation script. The setting ends when this terminal closes. | PowerShell returns to the prompt without an error. |
| `.\.venv\Scripts\Activate.ps1` | Makes `python` and `pip` use the isolated environment. | The prompt usually begins with `(.venv)`. |
| `python -m pip install -r requirements.txt` | Installs the exact package versions tested by the workshop. | The command ends successfully without a red error or traceback. |

macOS or Linux:

```bash
python3 --version
git --version
az --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Using `python -m pip` is deliberate: it guarantees that `pip` belongs to the same
Python interpreter that will run the samples.

Verify the active interpreter:

Windows PowerShell:

```powershell
python -c "import sys; print(sys.executable)"
```

macOS or Linux:

```bash
python -c 'import sys; print(sys.executable)'
```

**Success looks like:** the printed path includes `.venv`. If it does not, activate the
environment again. You must reactivate `.venv` whenever you open a new terminal; the
activation is intentionally temporary.

## 4. Sign in to Azure

The Python samples need permission to use your Foundry project. They obtain that
permission from your Azure CLI sign-in instead of storing your password in code.

Authentication is therefore a user-owned step. In **Terminal**, run:

```powershell
az login
az account show
```

`az login` opens an official Microsoft browser page. Complete the sign-in yourself and
return to the terminal. `az account show` then displays the active tenant and
subscription.

**Why verify the subscription?** A successful sign-in can still select the wrong Azure
subscription. In that case, the scripts may report that the Foundry project does not
exist or that you lack permission.

Read the `name`, `id`, and `tenantId` shown by `az account show`. If the wrong
subscription is active, run:

```powershell
az account set --subscription "<subscription-name-or-id>"
az account show
```

Replace the placeholder, including the angle brackets, with the real subscription name
or ID. Keep the quotation marks if the name contains spaces.

**Success looks like:** `az account show` returns the subscription that contains your
Foundry project. Do not paste this output into a public chat because it contains tenant
and subscription identifiers. Do not ask Copilot to invent credentials or bypass
authentication. If authentication expires during a lab, run `az login` again.

## 5. Configure the workshop

The samples need to know which Foundry project, model deployment, and agent name to use.
They read those settings from a local file named `.env`. Keeping the values there avoids
hard-coding participant-specific information in Python files.

First create `.env` by copying the safe template. Do not rename `example.env`; the copy
lets you keep the original reference unchanged.

Windows PowerShell:

```powershell
Copy-Item example.env .env
```

macOS or Linux:

```bash
cp example.env .env
```

Next, open `.env` from **Files**. If the app warns that it is ignored by Git, that is
expected and desirable.

Find the values as follows:

1. Open [Microsoft Foundry](https://ai.azure.com/) in your browser.
2. Select the **Foundry V2 project** supplied for the workshop.
3. On the project overview, copy the project endpoint for
	`AZURE_AI_PROJECT_ENDPOINT`. Copy the full URL exactly.
4. Open **Models + endpoints** and locate the deployed chat model.
5. Copy its **deployment name** for
	`AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME`. A deployment name can differ from the base
	model name, so do not assume it is `gpt-4.1`.
6. Choose a unique `AGENT_NAME`, preferably including your initials or workshop alias.
	This helps prevent participants from updating one another's agents in a shared
	project.

Replace the placeholders in `.env` with your values:

```dotenv
AZURE_AI_PROJECT_ENDPOINT=<your-project-endpoint>
AZURE_OPENAI_RESPONSES_DEPLOYMENT_NAME=<your-model-deployment-name>
AGENT_NAME=<your-unique-agent-name>
```

Remove the angle brackets when inserting real values. Keep values on one line. The
optional `AZURE_CLI_PROCESS_TIMEOUT="60"` controls how long a sample waits for Azure CLI
to provide a token; most participants can leave the template value unchanged.

The template also contains an optional `AZURE_AI_API_KEY` placeholder. The current FY27
commands in this guide do not require an API key; they use your Azure CLI identity.
Leave the placeholder unchanged unless your instructor provides a separate exercise
that explicitly requires it.

**Why must `.env` stay private?** It may contain an API key, and even non-secret
endpoints and identifiers belong to your environment rather than the shared workshop.
Never paste its contents into Copilot chat, commit it, or copy values into source files.

Verify that Git ignores both private, machine-specific paths:

```powershell
git status --short
git check-ignore .env .venv
```

`git status --short` should not list `.env` or `.venv`. `git check-ignore` should print
both names. If either path appears in `git status`, stop before committing and ask the
instructor for help.

## 6. Use Copilot as the workshop navigator

Use Copilot to reduce cognitive load, not to skip the learning. A strong workflow is:
**read, plan, approve, execute, inspect, validate**.

1. **Read:** Ask Copilot to read only the relevant README and source files. This grounds
	its answer in the actual FY27 workshop rather than a generic tutorial.
2. **Plan:** Open **Plan** and check the proposed files, commands, services, and expected
	result. Ask questions before execution.
3. **Approve:** Approve only the commands or edits you understand. Authentication,
	deployment, publication, and deletion always require your deliberate approval.
4. **Execute:** Watch **Terminal**. The first failing command is usually more useful than
	later follow-on errors.
5. **Inspect:** Open files in **Files** and inspect edits in **Changes**. Check for hard-
	coded endpoints, secrets, fabricated data, and unrelated modifications.
6. **Validate:** Run the smallest relevant sample or test and compare the result with
	the README's expected behavior.

Keep one repository session for setup, then consider a new session for each lab. This
keeps the conversation focused while preserving the same local files. At the start of
each lab, ask Copilot to read that lab's README and create a plan. For example:

```text
We are starting Lab 01. Read 01-microsoft-foundry-agents/README.md and the referenced
Python files. Give me a step-by-step run plan, but do not edit files. Check each command
against the current repository and wait for me to approve commands that create or
delete Azure resources.
```

If Copilot proposes a broad change, narrow it before approving. For example: “Only
explain and run the first sample. Do not edit files and do not continue to sample 2.”
This makes failures easier to understand and keeps you in control of the pace.

## 7. Lab 01: Microsoft Foundry agents

Lab 01 introduces the Foundry project client, the Responses API, and managed prompt
agents. Open [Lab 01](../01-microsoft-foundry-agents/README.md) in **Files** before
running anything.

The order matters:

| Script | What it teaches | What to look for |
|--------|-----------------|------------------|
| `01-quickstart-responses.py` | Connects to your Foundry project and calls the Responses API directly. | A model-generated response and no authentication error. |
| `02-quickstart-create-agent.py` | Creates or updates an immutable version of the prompt agent named by `AGENT_NAME`. | Output identifying the created or resolved agent/version. |
| `03-quickstart-chat-with-agent.py` | Resolves that existing agent by name and carries on a multi-turn conversation. | The agent responds across turns using the configured instructions. |

You must run script 02 before script 03 because the chat script looks up an existing
agent named by `AGENT_NAME`; it does not create one automatically. Foundry controls
version numbers. Re-running an unchanged definition can return the same version, while
changing the definition creates a new immutable version.

With `(.venv)` visible in the terminal prompt and Azure authentication working, run one
command, inspect its result, and only then continue:

```powershell
python "01-microsoft-foundry-agents/01-quickstart-responses.py"
python "01-microsoft-foundry-agents/02-quickstart-create-agent.py"
python "01-microsoft-foundry-agents/03-quickstart-chat-with-agent.py"
```

The quotation marks are required because other workshop paths contain spaces and using
them consistently prevents path parsing mistakes.

**Success looks like:** script 01 receives a response, script 02 identifies a managed
agent version, and script 03 finds that agent and responds. If script 03 says the agent
cannot be found, verify `AGENT_NAME` and rerun script 02 before changing code.

Use this prompt if a command fails:

```text
Diagnose the last terminal error using the current file and README. Do not change code
until you identify the root cause. Do not print values from .env. Propose the smallest
fix and a command that verifies it.
```

If the Microsoft Foundry plugin is available in the app, its panel can help you select
a project, configure models, tools, skills, or guardrails, and inspect or deploy an
agent. The Python samples remain the source of truth for this lab. Confirm the selected
project and deployment match your `.env` settings before using plugin actions that can
create billable Azure resources.

## 8. Lab 02: Agent Framework advanced

Lab 02 builds one concept at a time with Microsoft Agent Framework. Read
[Lab 02](../02-agent-framework%20ADVANCED/README.md), then run the samples in numerical
order. Later samples assume you understand the ideas introduced earlier.

| Sample | Why it exists | What you should learn |
|--------|---------------|-----------------------|
| `01_hello_agent.py` | Shows the smallest useful agent and both complete and streamed responses. | How an agent is created and run. |
| `02_add_tools.py` | Gives the model a local Python function decorated as a tool. | The difference between generating text and asking code to perform structured work. |
| `03_multi_turn.py` | Keeps conversation history in an agent session. | Why later turns can refer to facts from earlier turns. |
| `04_memory.py` | Injects dynamic runtime context through a custom context provider. | How external context differs from chat history. |
| `05_first_workflow.py` | Connects executors with explicit graph edges. | How a workflow controls the order of specialized processing steps. |
| `06_remote_mcp.py` | Connects an agent to a remote Model Context Protocol server. | How an agent discovers and calls tools exposed by another service. |

Run one command at a time:

```powershell
python "02-agent-framework ADVANCED/01_hello_agent.py"
python "02-agent-framework ADVANCED/02_add_tools.py"
python "02-agent-framework ADVANCED/03_multi_turn.py"
python "02-agent-framework ADVANCED/04_memory.py"
python "02-agent-framework ADVANCED/05_first_workflow.py"
python "02-agent-framework ADVANCED/06_remote_mcp.py"
```

After each sample, ask yourself what new behavior appeared compared with the previous
one. If a sample fails, stop there; later samples are unlikely to repair the same setup
problem. Some samples are interactive or use remote services. Read the file and its
README section before running it, and stop it with `Ctrl+C` when it remains active.

**Success looks like:** each sample completes its described interaction without an
authentication traceback. Tool samples should show behavior supported by actual tool
calls, and conversation samples should retain only the context the code intentionally
stores.

## 9. Lab 03: GitHub Copilot in the desktop app

The original [Lab 03](../03-github-copilot/README.md) teaches VS Code inline suggestions,
inline chat, smart actions, and agents. The desktop app is agent-first, so use this
equivalent path. This version teaches the app's plan-review-execute cycle instead of
editor keystrokes.

These are two related but different experiences:

| Activity | GitHub Copilot desktop app | VS Code |
|----------|----------------------------|---------|
| Ask an agent to plan and edit several files | Use the task composer, **Plan**, **Files**, and **Changes**. | Use Copilot Chat in Agent mode. |
| Run terminal commands | Use the session's **Terminal** view. | Use VS Code's integrated terminal. |
| Review an agent's file edits | Use **Changes**. | Review the proposed edits and select **Keep**. |
| Accept ghost-text suggestions while typing | Not reproduced by this app-based path. | Follow Lab 03 and press `Tab` to accept inline suggestions. |
| Open inline chat for selected code with `Ctrl+I` | Not reproduced by this app-based path. | Follow Lab 03 in the editor. |
| Use Command Palette and Source Control smart actions | Not reproduced by this app-based path. | Follow the original Lab 03 instructions in VS Code. |

Use the desktop app for the steps below. Open VS Code only when you intentionally want
to practice the editor-specific rows in the table.

1. Start a new session for Lab 03 and keep the same `agentic-hackathon` repository.
	**Why:** a focused conversation makes it easier for Copilot to follow this lab without
	carrying assumptions from the Azure samples.
2. Open the Lab 03 README in **Files** and read its feature requirements yourself.
	**Why:** you need a human understanding of the requested output to review Copilot's
	plan and changes.
3. Paste the app-focused prompt below into the task composer.
4. Open **Plan** before allowing edits. Confirm that Copilot will create only a new
	`app` directory and will not replace existing workshop files.
5. Let Copilot implement the plan. Watch **Terminal** if it runs any command.
6. Open `app/index.html`, `app/styles.css`, and `app/script.js` in **Files**. Confirm that
	content, styling, and behavior are separated into the three files.
7. Open **Changes** and inspect every added line. Look for semantic HTML, labels for form
	controls, keyboard-accessible buttons, input validation, and no external secrets.
8. Ask Copilot to start a local static web server. It may use a command such as
	`python -m http.server 8000 --directory app`. A local server lets the browser load
	the files over HTTP without deploying anything to the internet.
9. Open the localhost URL Copilot reports, normally `http://localhost:8000`. Add a place,
	try an empty submission, use every category filter, resize the window, and test dark
	mode. These actions validate behavior that a visual code review cannot prove.
10. Return to the app and report any specific failure. Ask Copilot to fix only that
	 failure, then review **Changes** and repeat the same browser test.
11. Stop the server with `Ctrl+C` in **Terminal**. Leaving it running can cause a port
	 conflict the next time you start it.

Use this app-focused prompt for the first implementation:

```text
Read 03-github-copilot/README.md. Implement its favorite-places application in a new
app directory using separate HTML, CSS, and JavaScript files. Preserve all existing
workshop files. Include the form, sample cards, category filters, validation, responsive
styling, accessibility, and dark mode described by the exercise. Then run a local
server and give me the localhost URL. Do not commit changes.
```

The app does not reproduce the original lesson's inline ghost-text and `Ctrl+I`
interactions. To practice those two specific skills, open the same repository in VS
Code and follow Lab 03 exactly. The resulting files can still be reviewed and improved
from the desktop app afterward.

This guide does not claim that Playwright automated the native desktop app. Playwright
automates browser pages, while this experience is a native application. The repository
workflow and supplied app interface were used to make these instructions realistic;
you should perform the clicks in your installed app and test the resulting web page in
your browser.

## 10. Lab 04: Agent examples

Lab 04 offers different paths rather than one linear sequence. Open
[Lab 04](../04-Agent%20Examples/README.md), read the comparison, and choose one path with
your instructor:

| Examples | Choose this path when you want to learn |
|----------|-----------------------------------------|
| 01-03 | How to design a scenario-specific Foundry prompt agent, test a no-tool baseline, attach a read-only MCP tool in a new version, inspect traces, and publish the tested version. |
| 04 | How to create a reusable GitHub Copilot custom agent that specializes in building professional Foundry prompt agents. |
| 05 | How a complete local web app, ticket store, MCP server, and Agent Framework client work together. This advanced path is already implemented. |

Ask Copilot to read only the chosen example's README before it plans work:

```text
Read 04-Agent Examples/README.md and the README for example 01. Explain the goal,
required Azure resources, files it will create, validation steps, and cleanup. Do not
implement anything until I approve the plan.
```

Examples 01 through 04 intentionally begin with instructions rather than completed
student code. Copilot helps you create the required files, but you must compare them
with the Lab 01 templates and review them before execution. Example 05 includes a local
web application, an MCP server, and an Agent Framework client. Run commands from the
selected example's README rather than guessing entry points.

For Examples 01-03, understand the purpose of the sequence:

1. Create an instructions-only agent version first. This becomes a behavioral baseline
	proving that the agent refuses to invent current facts when it has no data tool.
2. Test that baseline. A fluent current answer is a failure if no tool supplied the
	information.
3. Connect the exact documented read-only MCP endpoint in Foundry and keep approval
	enabled during development.
4. Inspect the server name, operation, arguments, result, and trace before trusting the
	answer. Good prose alone does not prove a tool ran.
5. Save the MCP-backed behavior as a new immutable version. Do not erase the baseline.
6. Publish only the version that passed testing, then repeat the acceptance prompts in
	**Test in website**.

Creating an agent version and publishing an Agent Application are separate operations.
Publishing can create a billable Azure resource and can require the `Foundry Project
Manager` role. Pause and ask the instructor if the option is unavailable or the cost is
unclear; do not weaken permissions or add credentials as a workaround.

When the app proposes deployment through the Microsoft Foundry panel, check the model,
project, region, authentication, and expected cost first. Use **Inspect Locally** before
**Deploy to Foundry** when that option is available.

## 11. Validate your work

Validation answers three different questions: did the command run, did it produce the
intended behavior, and did it avoid unintended changes? A successful exit code answers
only the first question.

Ask Copilot to run this final read-only review:

```text
Review my workshop progress without changing files. Show git status, list the samples I
successfully ran based on this session, identify unverified steps, check that .env and
.venv are ignored, and summarize any running local processes or Azure resources that I
should stop or delete.
```

Then run these checks yourself:

```powershell
git status --short
git diff --check
az account show
```

Interpret the commands as follows:

- `git status --short` lists changed and untracked files. Every listed path should be a
	change you intentionally made during the lab.
- `git diff --check` reports whitespace errors in tracked changes. No output means it
	found none.
- `az account show` reconfirms the Azure context before you inspect or clean up cloud
	resources.

Open **Changes** for the human review that commands cannot perform. Do not commit
generated credentials, `.env`, `.venv`, logs containing tokens, or unreviewed agent
changes.

## Troubleshooting

### The app cannot find the repository

Confirm the clone completed, then open the local `agentic-hackathon` directory from
**Home**. If a stale session points elsewhere, create a new session for the correct
folder. Open **Files** and check for the root `requirements.txt`; its presence is a quick
way to confirm you selected the repository root.

### The terminal is in the wrong folder

Run `Get-Location`. If the result does not end in `agentic-hackathon`, run
`Set-Location "C:\path\to\agentic-hackathon"` with your real path. Running workshop
commands from another folder commonly causes “file not found” errors.

### `python`, `git`, or `az` is not recognized

The program is either not installed or was installed after the app started. Install the
missing prerequisite, completely close and reopen the GitHub Copilot app, then rerun the
version command. Restarting matters because applications read the system `PATH` when
they launch.

### Python imports fail

An import error usually means the terminal is using system Python instead of `.venv`,
or package installation did not complete. Activate `.venv` in the current terminal,
confirm the interpreter path, and reinstall the tested dependencies:

```powershell
.\.venv\Scripts\Activate.ps1
python -c "import sys; print(sys.executable)"
python -m pip install -r requirements.txt
```

The interpreter path must include `.venv`. Do not solve the problem by installing
packages globally.

### PowerShell blocks virtual-environment activation

Change execution policy only for the current process, then activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\.venv\Scripts\Activate.ps1
```

### Azure authentication expired

Run `az login`, complete the browser flow yourself, and verify the subscription with
`az account show`. If sign-in succeeds but access still fails, compare the active tenant
and subscription with the Foundry project. Copilot cannot safely fabricate or replace
user credentials.

### The Foundry project or deployment cannot be found

Confirm all four layers before changing code: the active Azure subscription, the
Foundry V2 project, the full project endpoint in `.env`, and the deployment name under
**Models + endpoints**. The deployment name is not necessarily the model family name.
Close and rerun the sample after correcting `.env`; the workshop scripts load that file
at startup.

### The managed agent cannot be found

Confirm `AGENT_NAME` is identical in `.env`, then run Lab 01's
`02-quickstart-create-agent.py` before `03-quickstart-chat-with-agent.py`. The chat
sample resolves an existing agent and cannot chat with one that has not been created.

### A required environment variable is missing

Compare your private `.env` with `example.env`. Add the missing value locally without
pasting it into chat, save the file, and rerun only the failed sample. Do not include
the angle-bracket placeholders in a real value.

### A terminal command keeps running

Some servers and interactive samples are expected to remain active. Use `Ctrl+C` in
**Terminal** after testing, then confirm the process stopped before starting another
copy. If a later server reports that its port is already in use, return to the earlier
terminal and stop that process or choose a different unused port.

### Copilot wants to change unrelated files

Do not approve the plan. Reply with the exact allowed folder or files and state that all
other files must remain unchanged. If edits already occurred, inspect **Changes** and
reject only the unrelated changes; do not erase work you intended to keep.

## Finish and clean up

Cleanup prevents surprise Azure charges, port conflicts, and accidental secret commits.
At the end of the workshop:

1. Stop local servers and background tasks with `Ctrl+C` in their terminals. This frees
	ports and stops local tool endpoints.
2. Ask Copilot for a read-only list of resources created during the session, then verify
	that list in Foundry or the Azure portal yourself.
3. Delete only the Azure resources the facilitator says are no longer needed. Confirm
	the subscription and resource name before deletion because deletion may be permanent.
4. Open **Changes** and run `git status --short` one final time. Investigate every path
	you do not recognize.
5. Confirm `.env` and `.venv` remain ignored. Keep `.env` private and never commit
	`.venv`.
6. Close or archive completed app sessions if you no longer need them. This tidies the
	app but does not delete the local repository.

You are finished when the intended samples have been validated, no local server is
still running, the Azure resources are in the state requested by the instructor, and
Git shows only changes you knowingly chose to keep.
