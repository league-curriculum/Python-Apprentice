# Curriculum Review Guide

This repository is the League's Python Apprentice curriculum, aligned with the Python Institute's [PCEP](https://pythoninstitute.org/pcep) (entry-level) exam. Students are typically middle school and early high school age. Lessons live in `lessons/` as Jupyter notebooks organized into numbered category directories.

When asked to review a lesson or set of lessons, use the criteria below.

## Voice

Aim for a fun adult tone — a good teacher who respects the reader, not a kids-TV host or a cheerleader. Silly topic choices (badgers, mushrooms, snakes) are fine; breathless enthusiasm is not.

**Do:**
- Write like you'd explain something to a smart 12-year-old.
- Use "you" — the student is the reader.
- Allow at most one exclamation point per lesson, and only when the emphasis is genuinely earned.

**Don't:**
- Use "super", "awesome", "amazing", "fantastic", "incredible" as intensifiers.
- Write "We're so excited", "Don't worry!", "Let's go!", "You've got this!", "Ready to have some fun?".
- Use ALL-CAPS warnings or stacked exclamation points.
- Use emojis as substitutes for words (e.g. "turn left 🡐", "move forward ⬆️"). Decorative emojis in small doses are fine.
- Adopt kid-speak or corporate-training-speak.

**Example:**
- Okay: *"The turtle draws a line behind it as it moves."*
- Not okay: *"The turtle draws a SUPER cool line as it zooms around! 🚀"*

## Content flow

Within each lesson and across lessons in a category, check:

- **Logical progression** — each step follows from the last.
- **No prerequisites from later lessons** — every concept used in code or exercises has been introduced already, or is flagged with a brief "we'll cover this later".
- **No abrupt jumps** — difficulty increases smoothly.
- **Callbacks where warranted** — reference earlier lessons when it reinforces the current one, but don't force it.
- **Consistent terminology** — once we call it a "function", don't switch to "method" or "routine" without reason. Flag terminology drift across lessons.
- **No holes** — if a lesson uses a skill the student hasn't seen, that's a hole worth flagging.

**Motivation vs. mechanics:** Kids often do fine being handed a mechanic and getting the reason after they've tried it, as long as the mechanic itself is sensible. Don't flag missing motivation unless the lesson genuinely doesn't make sense without it.

**One concept per lesson:** The general preference is focused lessons, but existing structure takes priority. Note serious violations in the review, but **do not rewrite lessons to split concepts without explicit approval**.

## Technical quality

- Code examples must run as written.
- Examples should be realistic — not `foo()` / `bar()` placeholders — but not so elaborate they distract from the concept being taught.
- Follow PEP 8: 4-space indents, `snake_case` for variables and functions, `PascalCase` for classes, blank lines between top-level definitions, no trailing whitespace, line lengths ~79–100 chars, imports at the top.
- Accurate technical claims. Simplifications are fine ("a variable is a box for data"); outright-wrong statements are not.
- When we teach a topic, teach it thoroughly: a worked example, an exercise, and at least one edge case or common mistake called out.

### Exercise stubs are intentional

Many lessons have exercise code where key lines or whole function bodies are missing, commented out, or replaced with `...` / `# Your code here`. The student is supposed to type those in. Do **not** flag these as bugs, syntax errors, or missing implementations. Common shapes:

- `def foo():` with just a `# Your code here` comment as the body
- A bare `x = ` with no value (student will fill in the expression)
- `... # Your code here` placeholders in the middle of otherwise-complete code
- `.py` files that contain only a docstring — the rest is for the student

Only flag these if something adjacent is actually wrong (e.g. the surrounding hint text is misleading, or the stub references a concept the student hasn't learned).

## Scope

Curriculum targets PCEP. Intentionally **out of scope**:

- List / dict / set comprehensions
- Generators and `yield`
- Decorators
- Context managers beyond `with open(...)`
- Metaclasses, descriptors, `__slots__`
- `async` / `await`
- Type hints beyond incidental use

Do not suggest adding these. Teach what we teach thoroughly rather than expanding the surface area.

## Review workflow

When asked to review one or more lessons:

1. Read the lesson(s) in full, plus enough surrounding lessons in the same category (and the lesson immediately before and after) to judge flow and prerequisites.
2. Produce a markdown review with one `## <relative file path>` heading per file, and findings as bulleted items underneath.
3. The user will delete findings they don't want applied and hand the edited review back.
4. Apply the remaining findings.

### Finding format

Each bullet must be **standalone and deletable** — removing it shouldn't break any other finding. Include: category tag, location, the problem, and a concrete suggestion.

Group findings under each file heading in this order: **Voice**, **Flow**, **Technical**, **Scope**. Order within a category follows the location in the file.

```
## lessons/10_Turtles/10_Welcome/10_Welcome.ipynb

- **Voice** (cell 0, opening line): "Hello future coders, programmers, and engineers!" — drop the greeting, open with "Welcome to your first Python lesson."
- **Voice** (cell 0, intro paragraph): "We're super excited to help you..." — rewrite as "This course will help you take your first steps into programming."
- **Flow** (cell 2, exercise): exercise uses `random.randint()` but `random` hasn't been introduced — either introduce it earlier or swap the exercise for one using only what's been taught.
- **Technical** (cell 4, code block): mixes `Turtle()` and `turtle.Turtle()` — standardize on one convention and use it throughout the lesson.
```

Keep findings specific enough that applying one doesn't require re-reading the whole lesson. If a single change touches multiple places in a lesson (e.g. "rename `x` to `count` everywhere"), that's one finding — say so in the bullet.

<!-- CURIK:START -->
# Curik Curriculum Project

This repository is a Curik-managed curriculum project for the League of Amazing Programmers.

## Before You Do Anything

1. Run `curik status` to determine where this project stands.
2. Run `curik phase get` to understand the current phase and what gates must be met to advance.
3. Follow the process guide's instructions for the current phase.

Do not write curriculum content, modify course structure, scaffold files, or make any substantive changes without first checking the current phase via the CLI.

## Hugo Theme

The Hugo theme lives at `themes/curriculum-hugo-theme/` in this repo. Curik
copies it there during scaffolding. Do not modify it — changes go upstream
in the curik package. Hugo finds it automatically via `theme = "curriculum-hugo-theme"`
in `hugo.toml`.

## Rules

- **Use the AskUserQuestion tool for all questions**: When you need input, a decision, or approval from the stakeholder, ALWAYS use the `AskUserQuestion` tool. Do NOT pose questions in plain text output — users working in IDEs often miss text-only questions. The AskUserQuestion tool renders a visible UI prompt that the user can respond to. This applies to design decisions, approval gates, clarifications, and any time you need the stakeholder to choose or confirm something.
- **CLI-first**: For any operation that Curik has a command for (creating issues, managing change plans, scaffolding, validation, syllabus operations), use `curik <command>` via Bash. Do not perform these operations by directly editing files.
- **Agent boundaries**: When you load an agent definition via `get_agent()`, respect its boundaries. The Curriculum Architect does not write lesson content. The Lesson Author does not modify course structure.
- **Skills are workflows**: When you load a skill via `get_skill()`, follow its steps in order. Do not skip steps.
- **Gates are gates**: When `curik phase advance` fails, do not work around it. Address the unmet conditions.
- **Designer approval**: Change plans, outlines, and phase transitions require designer approval. Do not self-approve.
- **Theme is read-only**: Do not edit files in `themes/`. The theme is managed by the curik package.
- **No TBDs in course.yml**: After scaffolding, fill in all `course.yml` fields using `curik config update`. Infer values from the spec and content, then present to the designer for review. Never leave TBD values — ask the designer if you cannot determine a field.

## Available Commands

### Status and Phase
- `curik status` — current project state (phase, open issues, active plans)
- `curik phase get` — current phase and gate conditions
- `curik phase advance <target>` — gated phase transition
- `curik phase advance-sub` — advance to next Phase 1 sub-phase

### Spec Management
- `curik spec get` — read the course specification
- `curik spec update <section>` — update a named spec section
- `curik spec record-concept` — record Phase 1a output
- `curik spec record-model` — record Phase 1b output
- `curik spec record-alignment` — record Phase 1d output

### Course Configuration
- `curik config update <json>` — update fields in course.yml

### Scaffolding
- `curik scaffold structure <json>` — create Hugo content/ directory tree and lesson stubs
- `curik scaffold lesson <module> <lesson> --tier <n>` — create a single lesson stub
- `curik scaffold outline <name>` — create an outline document
- `curik scaffold approve-outline <name>` — mark an outline as approved
- `curik scaffold get-outline <name>` — read an outline document
- `curik scaffold change-plan <title> <items-json>` — create a numbered change plan

### Issues and Change Plans
- `curik issue create <title>` — create a numbered issue
- `curik issue list` — list open issues
- `curik plan create <title> <issue-numbers-json>` — create a change plan
- `curik plan register <n>` — register an agent-written change plan
- `curik plan approve <n>` — approve a change plan
- `curik plan execute <n>` — mark a change plan as executed
- `curik plan review <n>` — review a change plan
- `curik plan close <n>` — close a change plan and move issues to done

### Validation
- `curik validate lesson <path>` — validate a single lesson file
- `curik validate module <path>` — validate a module directory
- `curik validate course` — validate the entire course
- `curik validate get-report` — read the last saved validation report

### Syllabus
- `curik syllabus write-url <uid> <url>` — update the URL for a lesson entry
- `curik syllabus validate` — check syllabus entries against Hugo content pages

### Hugo Site
- `curik hugo pages` — list all content pages
- `curik hugo create-page <path> <title>` — create a new content page
- `curik hugo update-frontmatter <path> <json>` — update page frontmatter
- `curik hugo setup` — generate hugo.toml and copy the curriculum theme
- `curik hugo bump-version` — bump the curriculum version in hugo.toml
- `curik hugo build` — build the Hugo site

### README Generation
- `curik readme generate` — generate README files from lesson shortcode guards

### Publishing
- `curik publish guide` — full publishing guide with pre/post checklists
- `curik publish check` — quick publish readiness check
<!-- CURIK:END -->
