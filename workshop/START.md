# Participant start guide

Build two AI agents and a coordinating workflow in Microsoft Foundry, guided
by Workshop Coach in the GitHub Copilot app. Complete the
[prerequisites](PREREQUISITES.md) before attending. VS Code is not required.

## 1. Start the GitHub Copilot app

Open the app, select **Sign in to GitHub** if prompted, and sign in with your
workshop-approved account. You should see **Projects** in the sidebar.

## 2. Clone the workshop repository

Cloning downloads the workshop files to your computer.

1. Click **+** beside **Projects**, then **GitHub repository**.
2. Find **`haforsbe/agentic-hackathon`** and follow the prompts to clone it:
   https://github.com/haforsbe/agentic-hackathon
3. Use the facilitator-confirmed **`FY27`** branch
   (the named workshop revision), not an unconfirmed default branch.

If branch selection is unavailable, ask your facilitator for help, or run this
in a terminal from a folder where you keep projects:

```text
git clone --branch FY27 https://github.com/haforsbe/agentic-hackathon.git
```

Then choose **Projects → + → Local folder or repository** and select the newly
created `agentic-hackathon` folder. If you already have the correct checkout,
add that folder instead of cloning again.

## 3. Open the workshop

Under **Projects**, find **`agentic-hackathon`** and click **+** beside it to
start a session. Choose a local execution location unless your facilitator
specifies otherwise. Use this repository session, not the general **Chats** area.

## 4. Select Workshop Coach and start

1. Below the prompt field, set the session mode to **Interactive** so you stay
   involved in decisions.
2. In the agent selector, choose **Workshop Coach**, the teaching profile.
3. Send:

   > Start the workshop.

If there is **no agent selector**, use the repository session's normal Chat
and send the same message. If a selector exists but **Workshop Coach** is
missing, ask your facilitator; do not select an unrelated agent.

**Expected result:** the coach welcomes you, explains the workshop, and guides
you through confirming your assigned Foundry Project and choosing a model.
Nothing is deployed without your approval. You can say **"Explain without
editing"**, **"Give me a hint"**, or **"Pause the workshop"** at any time.

## If something looks different

Show your facilitator what you see rather than guessing controls. If the coach
gives a generic answer, first confirm the repository contains `AGENTS.md` and
`workshop/COACH.md`, then send:

> Read AGENTS.md and workshop/COACH.md from this repository and start the
> guided workshop at checkpoint 00. Ask one question at a time.

If those files are missing, request the correct workshop revision. Do not delete
old progress to restart; let the coach explain safe recovery.

**Facilitators:** distribute a committed/pushed revision or prepared checkout;
fresh clones do not include uncommitted edits. Verify Workshop Coach discovery
in the participant app build. See [facilitator guidance](FACILITATOR.md).

App navigation follows the official
[quickstart](https://docs.github.com/en/copilot/get-started/quickstart-copilot-app)
and [session guide](https://docs.github.com/en/copilot/how-tos/github-copilot-app/agent-sessions).
