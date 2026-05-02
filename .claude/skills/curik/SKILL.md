---
description: Curik curriculum development tool dispatcher
---

# /curik

Dispatch to the Curik curriculum development tool. Parse the argument
after `/curik` and run the matching CLI command via Bash from the table below.

If `/curik` is called with **no arguments**, display this help listing
to the user and stop — do not execute any command.

## Available commands

| Command | Description | CLI call |
|---------|-------------|----------|
| `/curik status` | Show current project phase, open issues, active plans | `Bash("curik status --json")` |
| `/curik spec` | Display the current course specification | `Bash("curik spec get")` |
| `/curik phase` | Show the current development phase | `Bash("curik phase get --json")` |
| `/curik validate <path>` | Validate a lesson file | `Bash("curik validate lesson <path> --json")` |
| `/curik publish` | Run publish check, fix issues, and push | See **Publish workflow** below |
| `/curik publish check` | Quick readiness check (no push) | `Bash("curik publish check --json")` |
| `/curik publish guide` | Show full publishing setup guide | `Bash("curik publish guide")` |

Pass any remaining text after the subcommand as the argument to the
CLI command (e.g., `/curik validate content/01-intro/01-hello.md`).

## Publish workflow

When the user runs `/curik publish`, execute these steps in order:

1. **Run readiness check**: `Bash("curik publish check --json")`.
2. **Fix what you can**: If any checks fail:
   - Missing `course.yml` fields → fill them in with `Bash("curik config update '<json>'")`,
     using your best inference from the course content. Present the values to
     the user with `AskUserQuestion` for confirmation.
   - Missing `.gitignore` or workflow → run `Bash("curik init")`.
   - Wrong `baseURL` → run `Bash("curik hugo setup")`.
   - Hugo build fails → investigate and fix the build errors.
3. **Re-check**: Run `Bash("curik publish check --json")` again to confirm all green.
4. **Bump version**: Run `Bash("curik hugo bump-version --json")` to update the
   curriculum version in `hugo.toml`. This uses the format `0.YYYYMMDD.revision`.
5. **Commit**: Stage and commit all changes including the version bump.
6. **Push**: Run `git push` to deploy. The GitHub Actions workflow handles
   the rest (build + deploy to GitHub Pages).
7. **Report**: Show the user the target URL, the new version number, and
   remind them to check the post-publish checklist from `Bash("curik publish guide")`.

If a check fails that you cannot fix (e.g., no content, GitHub Pages not
enabled), use `AskUserQuestion` to tell the user what's needed.

## General guidance

Load the `start-curik` agent definition to begin the curriculum development
workflow.
