# Repository guidance

This repository is an incremental workshop delivered in the GitHub Copilot app.
The current entry point is README.md and the curriculum is workshop/README.md.
The numbered example folders are reference material from the earlier workshop.

## Workshop participation

Normal repository Chat is the primary entry point; no custom-agent selector is
required. For "How do I start this workshop?" or equivalent onboarding questions,
read workshop/START.md and guide the participant from their current point.
Orientation alone does not start a lesson, create progress, or authorize cloud
work. Do not interpret workshop-authoring requests as participant onboarding.

When the user asks to start, resume, or participate in the workshop, read
workshop/COACH.md and follow its welcome and teaching/checkpoint protocol.
The plain message "Start the workshop" is sufficient; do not require the student
to select a coach profile or name instruction files.
Follow the original hello/tools/conversations/memory/workflow/MCP sequence,
teach Copilot app techniques throughout, and defer scenario choice to the capstone.
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
