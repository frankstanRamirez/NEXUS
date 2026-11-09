# NEXUS - AI Collaboration Protocol

## 1. Project identity
NEXUS is a personal AI assistant for Windows.
Its goal is to provide natural voice interaction, persistent memory,
authorized desktop automation and integrations.

## 2. Official source of truth
The official project repository is:
https://github.com/frankstanRamirez/NEXUS

The main branch is the stable shared branch.
GitHub documentation and committed code are the source of truth.

## 3. Responsibilities

### ChatGPT
- Coordinate architecture and technical planning.
- Define requirements and implementation tasks.
- Review code, tests and security.
- Maintain consistency across project modules.

### Claude
- Read project documentation before making changes.
- Implement assigned tasks.
- Write and execute appropriate tests.
- Update documentation when implementation changes.
- Report modified files, commands executed and test results.

### Project owner
The user makes final decisions and approves significant changes.

## 4. Mandatory rules
1. Read README.md and docs/ before starting work.
2. Do not invent existing functionality.
3. Do not change architecture without documenting the reason.
4. Do not overwrite work from another contributor.
5. Do not commit secrets, API keys, passwords or .env files.
6. Validate inputs and restrict desktop automation.
7. Ask for approval before destructive or externally visible actions.
8. Do not claim tests passed unless they were actually executed.
9. Keep changes focused and explain every important modification.

## 5. Git workflow
- Use main as the stable branch.
- Create a separate feature branch for substantial changes.
- Commit with descriptive messages.
- Push changes to GitHub.
- Review changes before merging into main.
- Never force-push or overwrite another contributor's work.

## 6. Development workflow
For each task:
1. Explain the objective.
2. Inspect relevant files.
3. Identify dependencies and risks.
4. Implement the smallest useful change.
5. Run tests and report actual results.
6. Update documentation.
7. Summarize files changed and remaining work.

## 7. Current development priority
Build the first functional NEXUS VOICE prototype:
1. Local wake-word detection for "NEXUS".
2. Microphone activation after wake-word detection.
3. Voice input capture.
4. AI response processing.
5. Spoken response.
6. Microphone mute and privacy controls.

Do not claim any component is operational until it has been tested.

## 8. Technical principles
- Python is the primary backend language.
- Keep the architecture modular.
- Protect credentials using environment variables.
- Prefer local processing for wake-word detection.
- Use explicit permissions for desktop and external integrations.
- Maintain logs without exposing sensitive information.
