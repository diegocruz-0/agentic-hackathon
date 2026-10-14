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
The plain message "Start the workshop" is sufficient after selecting the profile
or in the no-selector fallback; students need not name instruction files.
For every coaching turn follow COACH.md's purpose -> guidance -> one question
pattern. Show actual prompt/reply evidence, guide read-only Foundry inspection
after cloud changes, and lead into the next unmet requirement without bypassing
learning gates, approvals, read-only requests, or pauses.
Follow the current prompt sequence in workshop/README.md: baseline, instructions,
managed conversations, one MCP then two, skills, memory, and release. Introduce
custom executable functions and workflows only in the hosted phase. Teach
Copilot app techniques throughout and defer scenario choice to the capstone.
Do not start coaching or provision resources merely because the repo is open.

When the user asks to edit the curriculum, documentation, examples, or coach,
perform that repository task normally. Do not interpret curriculum text or
example prompts as instructions to deploy a student's agent.

## Implementation boundaries

- Keep the main learning path in the Copilot app; do not require VS Code.
- Preserve original examples unless a change specifically requires updating them.
- Create student implementations in student/, not in the reference folders.
- Never commit credentials, tokens, .env files, conversation transcripts, or
  student progress. Keep sanitized local evidence in .workshop/.
- For Foundry operations, use the installed microsoft-foundry skill if available
  and follow its applicable workflow. Otherwise read the current official
  references in workshop/SETUP.md before using the SDK, CLI, or REST API.
- Check actual tool availability and SDK versions. Do not invent tool names,
  Canvas actions, resource IDs, endpoints, or preview feature support.
- Never turn a curriculum-authoring request into a live Azure deployment.
