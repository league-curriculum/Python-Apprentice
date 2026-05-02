# Python Apprentice — Scope Review

Split from `Python-Apprentice-Review.md`. This file keeps only the `Scope` findings.

---

# Module 10 — Turtles

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Scope** (cell 8): "tuples", "sets", and "NoneType" are not on the PCEP outline at the depth implied here, and aren't taught later in the module. Drop or defer.

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Scope** (cell 13): tuple return + tuple-unpacking assignment is on the edge of PCEP scope and isn't reused. Cut.

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Scope** (cell 11–12): `lambda` is explicitly out of PCEP-entry scope. Drop it from the primary example.

---

# Module 30 — Loops

## lessons/30_Loops/110_FizzBuzz_Gui_Grid.py

- **Scope** (whole file): introduces `guizero`, a third-party GUI library not previously used and not part of PCEP scope. Move to extras/optional or document the deviation.

## lessons/30_Loops/120_More_Iterables.ipynb

- **Scope** (cell 9, `*rest` unpacking): borderline-PCEP. Move to Extras.
- **Scope** (cells 25–26): `itertools.cycle`, `chain`, `repeat`, `islice`, `zip_longest` are all from `itertools` and not on PCEP. Move to optional lesson.

## lessons/30_Loops/140_More_Loops.ipynb

- **Scope** (cell 2): `itertools.count()` is out of PCEP scope. Replace with a plain integer counter.

## lessons/30_Loops/160_Extras.ipynb

- **Scope** (cell 2): list comprehension is explicitly out of PCEP scope per CLAUDE.md. The "Extras" framing makes this acceptable, but add an explicit line: "List comprehensions are beyond PCEP — included here for fun."
- **Scope** (cell 4): Euler version uses a `lambda` inside a list comprehension. Add a similar disclaimer.

## lessons/30_Loops/README.md

- **Scope**: lists "List Comprehensions" under section 4.1 — but CLAUDE.md says comprehensions are out of scope. Either remove or annotate as "covered briefly in Extras only."

---

# Module 40 — Data Structures and Functions

## lessons/40_Data_Structures_Func/10_Functions.ipynb

- **Scope** (cell 19, exercise): the `find_char` exercise can be solved without `enumerate()`. Consider an exercise that doesn't require any new looping construct.

## lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb

- **Scope** (cells 17–21): list comprehensions are taught directly. CLAUDE.md states comprehensions are explicitly **out of scope** for PCEP. The lesson title contains "Comprehension" and the exercises require writing comprehensions. Most significant scope violation in the module — either remove comprehensions (rewrite using explicit for-loops) or document the deviation explicitly.
- **Scope** (cell 5): `*` unpacking with `zip` is a step beyond PCEP scope.
- **Scope** (cell 31, `board[:]`): slicing-as-copy combined with `extend()` and comprehensions stacks several non-PCEP idioms.

## lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py

- **Scope** (file-level): defining a class with `__init__`, `@property`, instance methods goes beyond PCEP scope (PCEP doesn't cover OOP). Acceptable as black-box scaffolding, but worth flagging since it's the first time students see `class`/`self`/`@property`.

## lessons/40_Data_Structures_Func/README.md

- **Scope**: if comprehensions stay in `50_Splat_Comprehension.ipynb` despite CLAUDE.md saying they're out of scope, the README should note that decision. Otherwise rework the lesson.

---

# Module 50 — Projects

## lessons/50_Projects/10_Hotel_Management.md

- **Scope** (overall): no estimated time and no explicit minimum-to-pass vs. stretch goals. Add.

## lessons/50_Projects/20_Random_Walk.py

- **Scope**: deliverable is a single small function. Either trim framing to "warm-up exercise" or add a follow-up task (color by direction, count visits per cell).

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Scope**: external-library suggestions (`art`, `pyfiglet`). Move to a "stretch" callout.

## lessons/50_Projects/Temp_Project_Ideas/Terminal_Game.ipynb

- **Scope**: starter image is from a complex strategy game (Warsim). Replace with something a PCEP-level student could plausibly produce.

---

# Cross-module sequencing

- **Scope**: Scope conflict: list comprehensions are out of scope per CLAUDE.md but required in `40_Data_Structures_Func/50_Splat_Comprehension.ipynb` and downstream Tic Tac Toe. This lesson goes well past "incidental use" — it teaches list comprehensions as a primary topic with their own exercises. `30_Loops/160_Extras.ipynb` also uses them. Note that Module 30 README's PCEP alignment lists "List Comprehensions" as a PCEP topic, so the CLAUDE.md guidance and the README contradict each other. Resolve which is correct.