# Python Apprentice — Flow Review

Split from `Python-Apprentice-Review.md`. This file keeps only the `Flow` findings.

---

# Module 10 — Turtles

## lessons/10_Turtles/10_Welcome/10_Welcome.ipynb

- **Flow** (cell 0, third paragraph): "It's like having a small robot artist you can control with code." — the analogy is fine, but the surrounding paragraph already calls turtle programming "a virtual turtle [you give] commands [to]". Cut the robot-artist sentence to avoid repeating the same idea three times.

## lessons/10_Turtles/10_Welcome/20_Open_The_Screen.ipynb

- **Flow** (cell 0, opening): the lesson assumes the reader is in a Codespace ("you probably clicked … Create codespace on master"), but lesson 10 listed three valid environments (VS Code, Codespaces, League Code Server). Either narrow the prerequisite earlier, or rewrite this opening to cover the non-Codespace cases.

## lessons/10_Turtles/10_Welcome/30_Run_Programs.ipynb

- **Flow** (cell 1, code): the very first executable code in the course imports `datetime` and uses `datetime.date.today()` — modules, attribute access, and method calls all at once, before any of those concepts have been introduced. Replace with a plain `print("Hello, world!")` so the first run is "press play, see output appear", not "parse three new ideas".
- **Flow** (cell 5, "Your First Assignment"): step 1 says "Copy the Hello World code from above into the cell below, or type `print("Hello World!")`" — but the code above is the multi-line `datetime` example, not a Hello World. Either change the example in cell 1 to actual Hello World or rewrite the assignment to match what's there.

## lessons/10_Turtles/20_Introducing_Tina/10_Meet_Tina/Meet_Tina.py

- **Flow** (lines 28–98, function definitions): the file is intended as a "you don't need to understand all this yet" demo, but it defines five functions, uses default parameters (`l=200`, `r=170`, `w=40`, `l=50`), tuple unpacking in a `for` loop, `tan(radians(...))`, `setheading`, and a parameter named `l` that shadows the math letter. The comment promises "Later lessons will walk through it piece by piece," but no later lesson actually does. Flatten the structure or follow through.

## lessons/10_Turtles/20_Introducing_Tina/20_What_Can_Tina_Do.ipynb

- **Flow** (cell 0, "How Tina Follows Commands"): the bullet says "The code *before* the `#` is a **command**" — but `tina = turtle.Turtle()` is an assignment, not a command in the imperative sense. Either narrow the claim ("each line that starts with `tina.`...") or use "statement" / "instruction" instead of "command".

## lessons/10_Turtles/20_Introducing_Tina/30_Squares_and_Circles/Squares_and_Circles.py

- **Flow** (line 30, comment): "Repeat forward + right three more times to complete the square." — the next 12 lines *are* those repetitions. The comment reads as if the student is supposed to add them. Reword as "The square is drawn with four forward+right pairs, one per side."

## lessons/10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb

- **Flow** (cell 0, opening sentence): "Now that you've created a few programs…" — the student has run two programs and edited one; "created" overstates it. Reword: "Now that you've run a few programs and made a change…".

## lessons/10_Turtles/30_Turtle_Tricks/10_Turtle_Tricks.py

- **Flow** (line 4, intro): the student is asked to draw an equilateral triangle with `tina.left()` — they need to know the exterior turn angle is 120°, not the interior 60°. The lesson hasn't covered this. Either give the angle or add an explanation.

## lessons/10_Turtles/30_Turtle_Tricks/20_Turtle_Tricks.py

- **Flow** (line 4, exercise): drawing a pentagon requires knowing the exterior angle is 72°. The course hasn't introduced the `360/sides` formula yet (that's in Lesson 50). Either give the angle in the docstring or push this exercise after Variables.

## lessons/10_Turtles/40_Loops/10_Loops.ipynb

- **Flow** (cell 5, code): `%run .lib/auto_turtle.py` and `tina = turtle(myTS)` with `# type: ignore[name-defined]` — this is a notebook-only macro that doesn't appear in any earlier lesson, and it differs from the `import turtle; tina = turtle.Turtle()` pattern used in the .py files. Either explain `auto_turtle` the first time it appears, or use the same `import turtle` pattern as the .py exercises.
- **Flow** (cells 11–18, ASCII-emoji "drawings"): the lesson pivots from turtle drawing to printing emoji grids (orange squares, checkerboard, American flag), then returns to a turtle exercise. The emoji-grid section uses `if`/`elif`/`else`, modulo (`%`), nested loops, and the `end=''` keyword to `print()` — none of which have been introduced. Either move this to a later lesson where conditionals exist, or label it clearly as preview material with the syntax explained.
- **Flow** (cell 17, code): the American flag uses nested `if`/`else`, modulo, and `end=''`. Far past PCEP "first loop" territory. Same fix as above.

## lessons/10_Turtles/40_Loops/20_Loop_with_Turtle.py

- **Flow** (lines 11–12, docstring): contains `uid: 85lNu5qj` / `name: Loop With Turtle` metadata that's not in any other student-facing .py file in the module. Move metadata to a comment outside the docstring or strip it.

## lessons/10_Turtles/40_Loops/30_Loop_with_Turtle.py

- **Flow** (line 4, instructions): the assignment says "use a loop to draw a regular pentagon" but the file is empty. Without the angle hint (72°) and with the previous file having had structure laid out, the jump to a blank file is abrupt. Add boilerplate (`import turtle`, `setup`, `tina = turtle.Turtle()`, `turtle.exitonclick()`) so the student fills in the loop body, not the whole program.

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Flow** (cell 8, "Different Types of Variables"): introduces eight types — int, float, str, bool, list, tuple, dict, set, NoneType — when only int, float, str, bool are demonstrated. Lists arrive in lesson 80; dicts/sets/tuples/None aren't taught in the module at all. Trim.
- **Flow** (cell 13, code): another `%run .lib/auto_turtle.py` / `turtle(myTS)` invocation — same convention drift as 40_Loops.

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Flow** (cell 13, "Advanced Function Examples"): introduces `if`/`elif`/`else`, comparison operators, default parameter values, `from math import ceil`, **and** multiple-return-value tuple unpacking (`slices, pizzas = pizza_calculator(10)`) — all in one cell, none introduced yet, none reused later. Split or remove. At minimum drop the tuple-unpacking return.
- **Flow** (cell 15, code): another `auto_turtle` macro instead of the standard `import turtle` setup the .py exercises use.

## lessons/10_Turtles/50_Variables_and_Functions/20_Efficient_Turtle.py

- **Flow** (line 19, `def draw_polygon(sides):`): student is asked to define a function whose body uses both a loop and a calculation, with `forward` and `left` distance still unspecified. Either add a `size` parameter to the stub or hard-code a `size = 50` line above the function so the student isn't guessing.

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Flow** (cell 2): `set_turtle_image()` uses `from pathlib import Path`, `Path(__file__).parent / "images"`, and `str(...)` — none introduced. The function is presented as a copy-this-and-reuse-it black box, which is reasonable, but it's the first `from … import …`. One sentence saying "you don't need to understand the `pathlib` part" would fix this.
- **Flow** (cell 5): `from PIL import Image` is required for `set_background_image()`. Pillow isn't a stdlib module. Flag the dependency at the top of the lesson or check the course environment ships with Pillow.
- **Flow** (cell 11): introduces `lambda` (`t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))`), with the explanation deferred to "we will go over how to use the lambda function later on". Lambdas aren't on the PCEP track and don't appear later. Use the named `make_handler(t)` form as the primary example.

## lessons/10_Turtles/60_More_Turtle_Programs/20_More_Turtle_Programs.py

- **Flow**: file is two-line instructions inside a docstring, with no boilerplate. The student is asked to "copy the code from the previous lesson" — fine, but every other exercise file in the module includes at least `import turtle` and `turtle.exitonclick()`. Add minimal boilerplate.

## lessons/10_Turtles/60_More_Turtle_Programs/30_More_Turtle_Programs.py

- **Flow** (lines 1–7): same as above — file consists of instructions in a docstring with no boilerplate. Add an `import turtle` skeleton.

## lessons/10_Turtles/60_More_Turtle_Programs/40_More_Turtle_Programs.py

- **Flow** (lines 8–12, hint): the `random.randint(-300, 300)` snippet is the first appearance of `random` in this file, but `random` was already used in `90_Graphics_Projects` files. Add a one-line "you'll need `import random` at the top".

## lessons/10_Turtles/70_Projects/10_LeagueBot.py

- **Flow** (line 19): the boilerplate stops at `t = turtle.Turtle()` and the student has to recall the `set_turtle_image()` helper from lesson 60. The hint should reference that section by name.

## lessons/10_Turtles/70_Projects/20_Tash_Me.py

- **Flow** (line 11): no `import turtle`, no setup, just an instruction docstring and `... # Your code here`. Inconsistent with the rest of the module's exercise files. Add minimal boilerplate.

## lessons/10_Turtles/70_Projects/30_Tash_Me_Click.py

- **Flow**: instruction-only file. Add boilerplate.

## lessons/10_Turtles/70_Projects/40_Tash_Me_Twirl.py

- **Flow**: instruction-only file. Add boilerplate.

## lessons/10_Turtles/80_Introducing_Lists/10_Lists.ipynb

- **Flow** (cell 6, "Helpful list operations" table): lists `list[start:stop]` (slicing) — slicing hasn't been introduced and isn't covered in any later lesson in the module. Either add a quick example or drop the row.
- **Flow** (cell 12): uses `auto_turtle` macro, same convention drift.

## lessons/10_Turtles/80_Introducing_Lists/20_Color_Lines.py

- **Flow** (line 20): "Make another square, but put the colors in reverse order, using a negative index" — negative indexing wasn't covered in `10_Lists.ipynb`. Either add it to the lesson or change the instruction.

## lessons/10_Turtles/90_Graphics_Projects/20_Crazy_Spiral.py

- **Flow** (lines 26–27, instructions): "The second `...` in the for loop should be the number of shapes you want to make, for example 100, or a list of numbers." — confusing because the template above has `num_shapes = ...` on line 28. Clarify which `...` the comment refers to.

## lessons/10_Turtles/Module_One_Quiz.ipynb

- **Flow**: notebook is named "Module One Quiz" but Module 10 is the first module of the *Turtles* unit. Rename to "Module 10 Quiz" or "Turtles Quiz" for consistency with the directory name.

---

# Module 20 — Types and Logic

## lessons/20_Types_and_Logic/README.md

- **Flow** (PCEP Alignment list, section 2.1): lists "Bitwise Operators: `~` `&` `^` `|` `<<` `>>`" as covered, but no lesson teaches bitwise operators. Either remove the bullet or add a short bitwise lesson.
- **Flow** (PCEP Alignment list, section 2.2): lists "The `sep=` and `end=` Keyword Parameters" as covered, but neither parameter appears in any lesson. Remove the bullet or add coverage.
- **Flow** (PCEP Alignment list, section 1.3): lists "Naming Conventions" as covered, but no lesson explicitly teaches `snake_case` / `PascalCase` / valid identifier rules. Remove or add a short "Naming variables" subsection.

## lessons/20_Types_and_Logic/10_Operators_and_Types.ipynb

- **Flow** (cell 5, common types list): lists Integers, Floats, Strings, and Lists as the four most common types, treating `bool` and `dict` as afterthoughts. PCEP treats `bool` as one of the core literal types. Promote `bool` into the main list, or add a one-line `bool` example in the same code cell.
- **Flow** (cell 5, "Lists" bullet): this is the first time `mutable`/`immutable` appear. Briefly note "we'll come back to mutability later" rather than putting the load-bearing definition in a hover tooltip.
- **Flow** (cell 22, exercise): `kids = ...` and `candy_bars = ...` left as `Ellipsis` mean if a student runs the cell before filling in, they get a confusing `TypeError` involving `'ellipsis'`. Use bare `kids =` (cleaner syntax error) or add a hint comment.

## lessons/20_Types_and_Logic/20_String_Operations.ipynb

- **Flow** (cell 7, intro to string methods): lists `.upper()`, `.lower()`, `.replace()`, `.split()` as the methods the lesson will cover, but cell 8 also demonstrates `.title()`, `.startswith()`, `.endswith()`, and `.strip()` without introducing them. Either expand the introductory list or trim cell 8.

## lessons/20_Types_and_Logic/30_Control_Flow.ipynb

- **Flow** (cell 21, forward reference to `try`/`except`): the tip says `if-elif-else` blocks "are useful when paired with `try` and `except` blocks to handle errors" — but `try`/`except` is its own control structure, not a partner of `if`. Remove the tip or rephrase as "We'll cover `try`/`except` for handling errors in a later module."
- **Flow** (cell 25, `convert_ml_to_imperial`): first appearance of `def` with a parameter, `input()`, and `float()` casting together — too much new mechanics inside one example whose actual point is `if`/`elif`. Split into two cells.

## lessons/20_Types_and_Logic/40_Working_With_Numbers.ipynb

- **Flow** (cell 0): the three `<details>` sections include a deeper dive than PCEP requires. Add one sentence above the block: "Open these only if you want a deeper walkthrough — you don't need them to use the `bin()`/`oct()`/`hex()` functions below."
- **Flow** (cell 7, exercise): asks to print age "in decimal", "in hexadecimal", "in octal", "in binary", and finally "modulo 3". The modulo-3 line wasn't motivated by anything in this lesson. Drop it or tie it back explicitly.

## lessons/20_Types_and_Logic/50_My_Ages.py

- **Flow** (line 33, tkinter import): first appearance of `from tkinter import messagebox, simpledialog, Tk` in the curriculum. No preceding lesson introduces the Tk pattern. Add a paragraph explaining `Tk`, `withdraw`, and `mainloop`, or add a tiny "Hello, tkinter" lesson before this one.

## lessons/20_Types_and_Logic/60_Simple_Adder.py

- **Flow** (lines 10–22): all six steps require knowing the tkinter pattern from `50_My_Ages.py`, but `50_My_Ages.py` only sketched the pattern in a docstring. Add a "Reference example" pointer at the top: `# See 50_My_Ages.py for the import and Tk()/withdraw() pattern.`

## lessons/20_Types_and_Logic/80_Code_Challenges.ipynb

- **Flow** (cell 2): first time the curriculum iterates a `for` loop over an explicit list of values (`for n in [2, 3, 4, ...]`). Module 10 covered `for _ in range(N)` only; Module 20's lesson 10 used `for i in range(10)`. Add a one-line note ("`for n in [...]` runs the body once for each value in the list").

## lessons/20_Types_and_Logic/lib/03_badgers_tk.py

- **Flow** (whole file): file is in `lib/` but isn't referenced by any of the notebooks or `.py` files in this module. If it's the intended FizzBuzz UI for `30_Control_Flow.ipynb`, link it from cell 22; otherwise move it.

---

# Module 30 — Loops

## lessons/30_Loops/10_Iteration.ipynb

- **Flow** (cell 4, "What is an Iterable?" table): mentions Tuple before tuples have been introduced (lesson 50). Either flag with "we'll cover tuples later" or remove the row.
- **Flow** (cell 4): introduces `list()` as "one of the ways to iterate over an iterable" — but `list()` consumes an iterable into a list. Rewrite: "One way to peek at an iterable's contents is to pass it to `list()`, which collects every item into a list."
- **Flow** (cell 13): mentions `enumerate()` before lesson 120 introduces it; references `.replace()`/`.lower()`/`.upper()` before lesson 80. Drop or add forward references.
- **Flow** (cell 14, name-choice table): rows for `for x, y, z in coordinates:` and `for red, green, blue in colors:` use tuple unpacking, which the student hasn't seen. Remove or add a callout.

## lessons/30_Loops/20_Loops_with_Range.ipynb

- **Flow** (cell 7, Challenge): the exercise stub in cell 8 is just `...` with no scaffolding. Add a hint comment like `# Use range(start, stop, step) with the right step value`.
- **Flow** (cell 9, Badger FizzBuzz challenge): introduces conditional / divisibility logic that requires nested `if/elif/else`. Add a one-line callback ("Use `if`/`elif`/`else` and the `%` operator from module 20").

## lessons/30_Loops/30_Looping_Through_Lists.ipynb

- **Flow** (cell 9280847b, indexing intro): introduces `backpack[0]` indexing here, but the dedicated indexing/slicing lesson is 60. Trim the explanation to "as we saw before."
- **Flow** (cell 9e90bab0): converting `range()` to a list was already shown in lessons 10 and 20; this re-introduction is redundant. Cut or label as recap.
- **Flow** (cell d63d5efe): comment `my_list.append(c) # Adding to a list, more on this later` — the very next "Adding To Lists" section *is* "later." Replace with `# Adds c to the end of the list`.
- **Flow** (cell 7bd259e4): sorting is introduced here without warning, then never used in the challenge. The challenge does use `.sort()`, so make that callback explicit.
- **Flow** (cell c8f4a193, Challenge): requires `input()`, which has not been formally introduced. Add a one-line note.

## lessons/30_Loops/50_Tuples.ipynb

- **Flow** (cell 10, Tuple Unpacking): introduces tuple unpacking here, but lesson 120 also introduces it more thoroughly with `enumerate()`. Add a forward-reference: "We'll see more uses for unpacking in the iteration-functions lesson."
- **Flow** (cell 12, Use Cases): mentions "They can also be used as keys in a dictionary, whereas lists cannot." Dictionaries have not been introduced. Drop the dictionary mention or add "(dictionaries come up in the next module)."

## lessons/30_Loops/60_Indexing_and_Slicing.ipynb

- **Flow** (cell 0): says "Lists and strings are sequences of items" — but tuples were just covered in lesson 50 and they also support indexing/slicing. Add tuples.
- **Flow** (cell 13, IndexError demo): the cell will crash on execution. Wrap in `try/except IndexError as e: print(e)` or add a markdown note.

## lessons/30_Loops/70_List_Story.py

- **Flow** (line 19): the student is told to use indexing and append, then the final line uses `' '.join(story)` — `.join()` is introduced in 80_Strings, but 80 comes *after* 70. Either move this exercise after 80 or scaffold `.join()` in a comment.

## lessons/30_Loops/80_Strings.ipynb

- **Flow** (cell 0, scope): teaches f-strings, escape sequences, `.split()`, `.join()`, slicing within strings, and a "rebuild a sentence" challenge. At least four distinct concepts. Existing structure stands per CLAUDE.md, so flag only.
- **Flow** (cell 3, escaping intro): introduces "kernel" with a tooltip but never explains what a kernel is in beginner-friendly terms. Use "Python interpreter" instead.
- **Flow** (cell 33): example uses heavy slicing/indexing combinations. Add a simpler intermediate example before the dense one.

## lessons/30_Loops/100_For_Loop_Gauntlet.ipynb

- **Flow** (cell beb062f6): example uses an f-string `f"({i},{j})"` and `print(..., end=' ')`. The `end=` parameter could use a one-liner explanation since it's the first explicit use in this module.
- **Flow** (cell dee7d3d2): the multiplication-table bonus expects fixed column widths. Direct students to f-string padding `{n:3}` from lesson 80, or accept `\t` tab separation.

## lessons/30_Loops/110_FizzBuzz_Gui_Grid.py

- **Flow** (line 13): same FizzBuzz logic was just covered in 90_Fizz_Buzz_Badgers.py. Add a one-line callback.

## lessons/30_Loops/120_More_Iterables.ipynb

- **Flow** (whole file): covers `enumerate`, `zip`, `zip_longest`, `islice`, `cycle`, `chain`, `repeat`, plus tuple unpacking with `*rest`, plus building dictionaries from `zip()`. Serious one-concept-per-lesson violation. Flag only per CLAUDE.md.
- **Flow** (cell 8, "Nested Unpacking"): the example `for color, (item1, item2) in zip(colors, pairs):` is dense. Move to "Extras" or simplify.
- **Flow** (cell 20, dictionaries): builds a dictionary with `zip()`, but dictionaries are not part of this module. Drop or flag as preview.
- **Flow** (cell 33): uses ternary expression in a checkerboard example. Use a plain `if/else` block.

## lessons/30_Loops/130_Iterable_Turtle.py

- **Flow** (line 4): docstring mentions `cycle` and `slice` (`islice`) from lesson 120. If 120 moves to extras, this exercise loses prerequisites. Coordinate.

## lessons/30_Loops/140_More_Loops.ipynb

- **Flow** (lesson placement): `while` loops are introduced in lesson 140 — quite late. PCEP treats `while` and `for` as peers. Consider whether `while` should appear earlier. Flag only.
- **Flow** (cell 0): the body of the while-loop example increments but never prints. Add a `print(s)` so the example is observable.
- **Flow** (cell 2, `count()` from itertools): use a simpler example — a plain `for i in range(100):` with `break`.
- **Flow** (cell 8): nested loops with `break` and `for/else` together is a heavy lift for the first encounter. Add walkthrough or simplify to a flat example first.

## lessons/30_Loops/150_Number_Guess.py

- **Flow** (line 26): `ask_integer` is defined in this file (line 39) but uses `try/except`, which has not been introduced. Either explain `try/except` briefly in a comment, or pre-define `ask_integer` in a helper file.
- **Flow** (lines 41–45): student reading the file will encounter `try` and `except` for the first time. Add a one-line comment.

## lessons/30_Loops/README.md

- **Flow**: mentions "Lists in Lists: Matrices and Cubes" but no lesson covers nested lists explicitly. Remove or add coverage.
- **Flow**: mentions "The `del` Instruction" but no lesson teaches `del`. Remove or add coverage.
- **Flow**: mentions "Lists Inside Tuples and Tuples Inside Lists" — `50_Tuples.ipynb` does not cover this. Remove or add coverage.

---

# Module 40 — Data Structures and Functions

## lessons/40_Data_Structures_Func/10_Functions.ipynb

- **Flow** (cell 0, opening): add a one-line roadmap (e.g. "This lesson covers parameters, defaults, scope, composition, and globals.").
- **Flow** (cells 7, 9, 11): three cells in a row deliberately fail with `# Run Me!` comments — students will think their environment is broken. Label as `# This will fail!` instead.
- **Flow** (cell 19, exercise hint): "Use `enumerate()`" — `enumerate()` was introduced in Module 30. Optional: a one-line callback.
- **Flow** (cells 31–33, "Closures"): the section is titled "Closures" but the content is about reading a global variable from inside a function — that's not a closure. Rename to "Global Variables" / "Variable Scope" or rewrite to show an actual closure.

## lessons/40_Data_Structures_Func/20_Exceptions.ipynb

- **Flow** (cell 0, header): opens with `## **Exceptions**` (h2) while every other lesson in this module starts with `# **<title>**` (h1). Promote.
- **Flow** (cells 8, 10, 12, 14): four cells in a row deliberately raise exceptions with `# Run Me!` comments. Use `# This will raise an exception` instead.
- **Flow** (cell 19, exercise): "tell the user what the n-th number *in the list* is" but the example output uses `7` as the index into a 4-element list. The wording "the 7th number in the list" misleads. Rewrite to use a number small enough to succeed (e.g. `3rd` returning `45`) and a separate one that fails.

## lessons/40_Data_Structures_Func/30_Dicts_Sets.ipynb

- **Flow** (cell 0): roadmap doesn't mention dicts even though dicts are half the lesson title. Add.
- **Flow** (cell 0, set syntax bullet): "note that empty `{}` creates a dict, so an empty set must be created with `set()`" — references dicts before they're introduced. Move or add a parenthetical.
- **Flow** (cell 19, "Unpacking Key-Value Pairs"): tuple unpacking introduced as if it's been seen before. Make the introduction explicit, or move to its own subsection.
- **Flow** (cell 20): `enumerate(my_dict.items())` is correct but visually busy. Show simpler `for key, value in d.items()` first, then enumerated.
- **Flow** (cell 30, exercise loop): `for my_set in funny_sentences:` — variable name `my_set` to iterate over a list of *strings* is misleading. Rename to `sentence`.

## lessons/40_Data_Structures_Func/40_Funny_Words_Db.py

- **Flow** (file-level): no README or notebook callout explaining how to run it (it needs `guizero`). Add a one-line note in the module README.

## lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb

- **Flow** (cell 0, title): "Splat, Zip, and Comprehensions" — file is named `50_Splat_Comprehension.ipynb` (singular). Pick one.
- **Flow** (cell 5, "Who Won?" header): the section is actually a transposition lesson. Rename to "## **Getting Columns from a Grid**" and let "Who Won?" come later.
- **Flow** (cells 22–24, diagonals exercise): student is asked to write a comprehension immediately after one introductory example. Add a worked example using an *index* before asking.
- **Flow** (cell 27, hint): "logic value" is non-standard. Use "truth value".
- **Flow** (cell 34, callback): verify path `../10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb` is correct relative to the current notebook.

## lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py

- **Flow** (line 5): docstring header `# 60_Tic_Tac_Toe.py` — drop the `#` since it's a docstring, not Markdown.
- **Flow** (lines 13–14): "use the constants X_MARK and O_MARK instead of the strings 'x' and 'o'" — but the previous notebook used lowercase `'x'`/`'o'` while this file defines `X_MARK = "X"` (uppercase). Students copying from the notebook will silently fail. Call this out at the top of the file.

## lessons/40_Data_Structures_Func/README.md

- **Flow**: lists only PCEP-30-02 4.3 (dictionaries) under "PCEP Alignment," but this module also covers functions, exceptions, and sets. Functions are PCEP 3.x and exceptions are PCEP 4.x. Expand.
- **Flow**: no mention of the project files (40_Funny_Words_Db.py, 60_Tic_Tac_Toe.py) or the splat/zip/comprehension lesson. Add a short outline.

---

# Module 50 — Projects

## lessons/50_Projects/README.md

- **Flow**: single paragraph with no list of lessons. Either drop PCEP Alignment from earlier modules' READMEs for consistency, or add a short "Projects in this module" list here.

## lessons/50_Projects/10_Hotel_Management.md

- **Flow** (Getting Started): "Add your imports (tkinter or whatever you need)" — curriculum doesn't teach Tkinter directly. Module 20 uses `tkinter.simpledialog`/`messagebox` and Module 30/40 use `guizero`. Replace "tkinter" with "guizero (or `tkinter.simpledialog`)".
- **Flow** (Functionality Requirements): "Must be interactive, either in the command line with print() and input() or with Tkinter" — `input()` has not been formally introduced. Either swap for the dialog functions students have used, or add an "Using `input()`" intro.

## lessons/50_Projects/20_Random_Walk.py

- **Flow**: this is a turtle program in the Projects module, sitting after Hotel Management. Consider whether it should live with `10_Turtles/90_Graphics_Projects/`. If kept here, add a one-line note that it intentionally revisits Module 10 turtle skills.

## lessons/50_Projects/Temp_Project_Ideas/

- **Flow**: directory name `Temp_Project_Ideas` suggests draft material, but it sits in the published `lessons/` tree. Either rename the directory to `30_More_Projects/` and number the files, or move it to a top-level `drafts/` until ready.
- **Flow**: files inside are inconsistently named — `30_ASCII_Art.ipynb` has a numeric prefix but `Spin_The_Wheel.ipynb` and `Terminal_Game.ipynb` do not. Pick one.

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Flow** (boilerplate code cell): worked example uses nested loops over a dict. If lesson placement is post-Module-40, that's fine; warn if lesson order is uncertain.

## lessons/50_Projects/Temp_Project_Ideas/Spin_The_Wheel.ipynb

- **Flow**: lesson is two short markdown cells with no example code, no scaffold, no exercise stub. Add a starter file or call out that the student writes from scratch.

## lessons/50_Projects/Temp_Project_Ideas/Terminal_Game.ipynb

- **Flow**: two-and-a-half markdown cells with no starter code, no example play session, no concrete scope. The Warsim screenshot sets a target way out of reach. Either add a 2-room "find the key" walkthrough or pick a lower-key visual.
- **Flow** (Assignment Requirements): "Use control flow to manage game progression" duplicates "Implement user input to allow players to make choices". Tighten.

---

# Cross-module sequencing

- **Flow**: Functions taught twice — Module 10 informally, Module 40 formally — handled gracefully but framing misrepresents Module 10. `40_Data_Structures_Func/10_Functions.ipynb` opens with "We've seen functions a few times, but haven't explained how they work in detail" — but Module 10's `50_Variables_and_Functions/20_Functions.ipynb` already covers `def`, parameters, return values, and looped calls. Module 40's intro should state more concretely *what's new*: keyword vs. positional args, default args, scope/globals, `pass` — none of which are in Module 10.
- **Flow**: Lists taught twice — Module 10 (`80_Introducing_Lists`) and Module 30 (`30_Looping_Through_Lists`) — handled gracefully but Module 30 is mostly review. By the end of Module 10, students already have indexing, iteration with `for`, and `append`/`insert`/`remove`/`len`/slicing. Decide whether `30_Loops/30_Looping_Through_Lists.ipynb` does meaningful new work or is mostly review.
- **Flow**: `90_Graphics_Projects/10_Flaming_Ninja_Star.py` uses concepts not formally taught in Module 10. It uses `random.randint`, hex string formatting (`"#%06X" % ...`), modulo, and indexing. If lessons run in numeric order (`70_Projects` → `80_Introducing_Lists` → `90_Graphics_Projects`), then `90_*` is after lists and is fine. The bigger hole is `%` formatting and `random.randint` — neither is taught in Module 10. Either add a one-cell "the `random` module" callout or move `90_Graphics_Projects/` to after Module 20.
- **Flow**: Hole: `input()` is never properly introduced before it's required in `50_Projects/10_Hotel_Management.md`. Module 20 uses `tkinter.simpledialog`/`messagebox`. Module 30's `150_Number_Guess.py` uses a custom `ask_integer` helper. By Module 50 the student is told they can use `print()` and `input()` — but `input()` has zero prior exposure. Add a short "Using `input()` and `print()`" subsection.
- **Flow**: Hole: `guizero` is used in three projects (`30_Loops/110_FizzBuzz_Gui_Grid.py`, `40_Data_Structures_Func/40_Funny_Words_Db.py`, `40_Data_Structures_Func/60_Tic_Tac_Toe.py`) but never formally introduced. `110_FizzBuzz_Gui_Grid.py` says "Don't worry about how it works — copy the examples", okay for one project but not three. Add a short `guizero` primer in Module 30 (before `110_*`) covering `App`, `Text`, `Box`, `PushButton`, `grid=`.
- **Flow**: `30_Loops/40_Crazy_Tina.py` references a section that doesn't exist. Its docstring says "Review the 'Using Lists' section of the previous lesson" — there is no section titled "Using Lists" in `30_Looping_Through_Lists.ipynb`. Update the cross-reference or rename the section.
- **Flow**: Module 30 has 16 lesson files; Module 40 has 6 — heavy pacing skew. Module 30 covers `for`, `while`, range, lists, indexing/slicing, tuples, strings, plus a FizzBuzz GUI project — much overlapping Module 10's lists/loops intro. Consider moving basic-list material entirely to Module 30 (and trimming Module 10's `80_Introducing_Lists/`), or splitting Module 30 into "Loops" and "Sequences".
- **Flow**: Turtle naming drift. Module 10 uses `tina` consistently. Module 30 uses `tina` and `t`. Module 50's `20_Random_Walk.py` calls the turtle `walker`. Fine variety, but `20_Random_Walk.py`'s docstring should add "you've used turtles before; this one is named `walker`" so the rename isn't jarring.
- **Flow**: Module 10 README is shorter and missing PCEP alignment. It lists four bullet topics ("Variables, Loops, Functions, Lists") with PCEP Alignment only sections 1.1 and 1.2. Module 10 actually teaches enough to at least partially cover 1.3, 3.2, and 4.1. Either trim Module 10's content or expand the README's PCEP block.
- **Flow**: Module 50 README says "complete projects" but `20_Random_Walk.py` is a single-function fill-in. Reframe README to "small to medium projects", or upgrade Random Walk.