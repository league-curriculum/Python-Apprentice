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
