# Weather baseline

Minimal workshop agent using the existing `gpt-5.4-mini` deployment. No tools,
skills, or persistent memory are configured. The parent folder's existing
definitions are not modified.

Create an isolated Python environment for this folder and install
`requirements.txt`. Keep the environment outside the repository, or in an
ignored local folder. Set `AZURE_CONFIG_DIR` in the operation process to the
workshop-only CLI profile and sign in interactively. Never commit sign-in
caches, credentials, transcripts, or local progress.
The client allows 120 seconds for CLI authentication because the default
10-second subprocess timeout was insufficient on the workshop machine.

Run `client.py --help` for required target and identity arguments. `create`
refuses an existing agent name, creates one version, and reads it back without
calling the model. Save the returned version in ignored local workshop
progress, not this definition.

After separate approval, `test --version <exact-version> --test B01` sends one
model request, which may incur charges. B02 and B03 are separate commands.
Each request omits previous response/conversation identifiers, so it does not
reuse another test's history. These isolated baseline requests do not prove
managed Conversation or persistent-memory behavior.

| Test | Expected observation |
|------|----------------------|
| B01 | Concise, accurate general knowledge; no invented live source |
| B02 | Requests missing location rather than assuming another test's context |
| B03 | Explains lack of private-file access; fabricates neither contents nor execution |

An automated response is evidence to review, not an automatic pass. Never run
tests until their target, input, and possible usage cost have been approved.
