# Participant start guide

**Select Workshop Coach in the GitHub Copilot app, then say "Start the workshop."**
This is the preferred live entry. VS Code and its extensions are not required.
Normal repository Chat is a fallback only when the app has no agent selector.

## Before opening the app

Your facilitator provides access to the GitHub Copilot app and the repository
link/revision containing this workshop. If you do not have those, ask the
facilitator for them. You do not need to provision Azure resources before you
can get help starting.

## Open the workshop

1. Open the GitHub Copilot app and open/add the workshop repository as a project
   using the controls available in your app build. If the repository is already
   listed as a project, use that project.
2. Start a session **inside that project**, rather than an unrelated general
   chat. In the app's agent selector, select the agent named exactly
   **Workshop Coach**.
3. With Workshop Coach selected, type:

   > Start the workshop.

That is the entire starter prompt. The repository defines Workshop Coach in
`.github/agents/workshop-coach.agent.md`; its teaching protocol is shared with
the fallback. If your app has no agent selector, start normal repository Chat
and send the same message. Selecting the profile alone does not start the lesson.

Controls vary by app build. If you cannot open the project or start its session,
tell the facilitator what you see. Do not follow guessed menu paths or switch
to VS Code to complete this course.

## What should happen next

The coach should welcome you and explain:

- You will first build small prompt-agent exercises, then hosted agents, and
  finally choose your own capstone.
- Each lesson makes one small change, runs a test, and checks your understanding
  before continuing. You also learn an app technique and an alternative.
- Copilot is your coach here; your application agents run separately in Foundry.
  You remain in control of file changes, cloud operations, and resource costs.

It checks the workshop files and any saved progress before guiding you through
checkpoint 00. For a fresh start, its first setup question is whether you have
an existing Foundry project. "No" or "I'm not sure" is fine: it explains what is
needed and helps you coordinate with the facilitator, not silently provision it.

After starting, you should not be asked to choose IT support, install all
future dependencies, or deploy a complete solution at this point.

## Your first app controls are plain-language requests

| Say | What it does |
|-----|--------------|
| "How do I start this workshop?" | Explains the entry steps without starting cloud work |
| "Explain this without editing anything." | Keeps the interaction read-only |
| "Give me a hint." | Helps with the current concept without solving future lessons |
| "Show me another way." | Compares a useful alternative; does not automatically run it |
| "Pause the workshop." | Saves local progress; does not stop or delete Azure resources |
| "Resume the workshop." | Checks saved progress and the target before continuing |

## If the profile or welcome does not appear

Picker visibility has not yet been verified in a fresh participant session.
The supported profile file is not proof that your app build discovers it.
If you have a selector but Workshop Coach is absent, check that this checkout
contains `.github/agents/workshop-coach.agent.md` and the current curriculum.
Have the facilitator verify discovery in a fresh session using that revision.
Do not switch to VS Code, invent a refresh command, or select an unrelated agent.
If the app has no selector at all, use the normal repository Chat fallback.

First verify that this is a repository session containing `AGENTS.md` and
`workshop/COACH.md`. If the selected coach (or no-selector fallback) gives a
generic answer despite those files being present, send:

> Read AGENTS.md and workshop/COACH.md from this repository and start the
> guided workshop at checkpoint 00. Ask one question at a time.

This is a recovery prompt, not a requirement to memorize file paths. If those
files are missing, ask your facilitator for the workshop-enabled revision.
Never ask Copilot to invent the missing curriculum.

If you see old progress, the coach should explain whether it can resume or needs
your permission to migrate it. Do not delete progress to force a fresh start.
Progress lives in the current checkout; a different worktree will not
automatically contain it.

## For facilitators testing local changes

Give participants a committed/pushed revision or a prepared checkout containing
the complete materials. A new worktree from an older commit does not inherit
uncommitted edits. Check that the participant can read the start guide before
asking them to troubleshoot coaching behavior.

The startup acceptance scenarios are in [FACILITATOR.md](FACILITATOR.md).
