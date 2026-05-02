# Python Apprentice — Curriculum Review

Findings follow the format prescribed by `CLAUDE.md`: one heading per file, bulleted findings grouped Voice / Flow / Technical / Scope. Each bullet is standalone and deletable.

---

# Module 10 — Turtles

## lessons/10_Turtles/10_Welcome/10_Welcome.ipynb

- **Voice** (cell 0, "Course Symbols" alert): "Take a moment to look them over before you continue." plus the closing italic line "It's worth reading through each of these, since the lessons refer back to them." — these say the same thing twice and the second sounds slightly preachy. Drop the centered italic line and keep only the opening sentence.
- **Flow** (cell 0, third paragraph): "It's like having a small robot artist you can control with code." — the analogy is fine, but the surrounding paragraph already calls turtle programming "a virtual turtle [you give] commands [to]". Cut the robot-artist sentence to avoid repeating the same idea three times.
- **Technical** (cell 0, embedded SVGs): every glossary term is followed by a 24x24 inline SVG info icon, repeated roughly seven times in this cell alone. The result is a wall of inline SVG markup that obscures the prose in any non-rendering view. Move the icon into a small CSS class or a single helper, and reuse it by class name.
- **Technical** (cell 0, "League Code Server" bullet): the line ends with `<!--If there is a link for this let me know -->` — an author-to-author HTML comment leaked into the lesson. Remove or replace with a real link.

## lessons/10_Turtles/10_Welcome/20_Open_The_Screen.ipynb

- **Voice** (cell 0, second sentence): "Now, to see your turtle's drawings, you need to open a virtual screen." — fine, but combine with the next sentence ("Most of the time, this screen will open automatically.") which currently reads as a small contradiction. Suggest: "The virtual screen usually opens automatically. If it doesn't, look for the monitor icon …".
- **Flow** (cell 0, opening): the lesson assumes the reader is in a Codespace ("you probably clicked … Create codespace on master"), but lesson 10 listed three valid environments (VS Code, Codespaces, League Code Server). Either narrow the prerequisite earlier, or rewrite this opening to cover the non-Codespace cases.

## lessons/10_Turtles/10_Welcome/30_Run_Programs.ipynb

- **Voice** (cell 1, code): "Hello 👋 World 🌎! Today is" uses two decorative emojis in a single short string and the lesson hasn't introduced strings yet. Drop the emojis — the date demo doesn't need them.
- **Flow** (cell 1, code): the very first executable code in the course imports `datetime` and uses `datetime.date.today()` — modules, attribute access, and method calls all at once, before any of those concepts have been introduced. Replace with a plain `print("Hello, world!")` so the first run is "press play, see output appear", not "parse three new ideas".
- **Flow** (cell 5, "Your First Assignment"): step 1 says "Copy the Hello World code from above into the cell below, or type `print("Hello World!")`" — but the code above is the multi-line `datetime` example, not a Hello World. Either change the example in cell 1 to actual Hello World or rewrite the assignment to match what's there.
- **Technical** (cell 7, "Using the Lesson Browser"): the lesson refers to "the Lesson Browser" in the bottom-left as the recommended way to run `.py` files, but the rest of the course uses plain `python file.py`-style runs. Confirm the Lesson Browser actually exists in the student's environment, or move it below the play-button instructions.
- **Technical** (cell 8, warning): "if the program's code ends with `turtle.exitonclick()`, simply click anywhere inside the window to close it" — `exitonclick()` closes the *turtle* window, not the program; the Python process exits as a result. Reword as "click the turtle window to close it".

## lessons/10_Turtles/20_Introducing_Tina/10_Meet_Tina/Meet_Tina.py

- **Flow** (lines 28–98, function definitions): the file is intended as a "you don't need to understand all this yet" demo, but it defines five functions, uses default parameters (`l=200`, `r=170`, `w=40`, `l=50`), tuple unpacking in a `for` loop, `tan(radians(...))`, `setheading`, and a parameter named `l` that shadows the math letter. The comment promises "Later lessons will walk through it piece by piece," but no later lesson actually does. Flatten the structure or follow through.
- **Technical** (line 49, `def draw_leg(t, a, r=170, w=40, l=50)`): single-letter parameter `l` is one of the PEP 8-discouraged names (looks like `1` or `I`); also conflicts with `length`. Rename `l` to `length` and `a` to `angle` (and `r`/`w` similarly).
- **Technical** (line 91, `for lp in (30, -30, -150, 150):`): uses tuple iteration before lists, tuples, or iteration have been introduced. Either swap to a literal list or unroll the four `draw_leg` calls.
- **Technical** (line 94, `draw_leg(tina, -90, r=170, w=10, l=50)`): keyword arguments appear here for the first time in the course, with no introduction. The `r=170` is also the default, so it's redundant; pass `w=10` only.
- **Technical** (lines 89–96, call order): `draw_head(tina)`, then legs, then `draw_body(tina)`. The orphan `tina.begin_fill()`, `tina.penup()`, `tina.goto(-100, 175)`, `tina.pendown()` block on lines 23–26 doesn't do anything useful. Remove it.

## lessons/10_Turtles/20_Introducing_Tina/20_What_Can_Tina_Do.ipynb

- **Voice** (cell 0, second paragraph): "Your task will be to read the program, figure out what it does, and make some fun changes." — drop "fun"; "make some changes" is enough.
- **Flow** (cell 0, "How Tina Follows Commands"): the bullet says "The code *before* the `#` is a **command**" — but `tina = turtle.Turtle()` is an assignment, not a command in the imperative sense. Either narrow the claim ("each line that starts with `tina.`...") or use "statement" / "instruction" instead of "command".
- **Technical** (cell 1, embedded iframe): `<iframe src="https://docs.python.org/3/library/turtle.html" …>` — the Python docs send `X-Frame-Options: deny`, so this iframe will not render in most browsers. Replace with a plain link.

## lessons/10_Turtles/20_Introducing_Tina/30_Squares_and_Circles/Squares_and_Circles.py

- **Flow** (line 30, comment): "Repeat forward + right three more times to complete the square." — the next 12 lines *are* those repetitions. The comment reads as if the student is supposed to add them. Reword as "The square is drawn with four forward+right pairs, one per side."
- **Technical** (line 57, `tina.color('red')`): the rest of the file uses `pencolor()` and `fillcolor()` separately. `color()` sets both, which is fine here, but it's the only line in the file using the combined form. Mention in a comment that `color()` sets pen and fill at once, or split it for consistency.

## lessons/10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb

- **Voice** (cell 2, tip): "Stopping your Codespace helps save resources and ensures your work is safely paused. Just remember to save/commit any changes!" — has the only exclamation point in the lesson and isn't earned. Drop the `!`.
- **Flow** (cell 0, opening sentence): "Now that you've created a few programs…" — the student has run two programs and edited one; "created" overstates it. Reword: "Now that you've run a few programs and made a change…".
- **Technical** (cell 1, large stylized "Sync Changes" span): the inline-styled span renders as an oversized button-like graphic but it's pure HTML — students may try to click it. Replace with a screenshot or smaller styled span.
- **Technical** (cell 4, empty markdown cell): cell 4 is an empty markdown cell. Remove it.

## lessons/10_Turtles/30_Turtle_Tricks/10_Turtle_Tricks.py

- **Flow** (line 4, intro): the student is asked to draw an equilateral triangle with `tina.left()` — they need to know the exterior turn angle is 120°, not the interior 60°. The lesson hasn't covered this. Either give the angle or add an explanation.
- **Technical** (line 6, `tina.forward()` and `tina.left()`): the docstring lists these but the student has only seen `tina.right()` so far. Add a one-line note that `left` works the same as `right`, just the other direction.

## lessons/10_Turtles/30_Turtle_Tricks/20_Turtle_Tricks.py

- **Flow** (line 4, exercise): drawing a pentagon requires knowing the exterior angle is 72°. The course hasn't introduced the `360/sides` formula yet (that's in Lesson 50). Either give the angle in the docstring or push this exercise after Variables.

## lessons/10_Turtles/40_Loops/10_Loops.ipynb

- **Voice** (cell 1, second paragraph): "Instead of repeating the same instructions over and over again, a loop will let you tell Tina to do something multiple times by using a simple command." — wordy. Trim to "Instead of repeating the same instructions, a loop tells Tina to do something multiple times."
- **Voice** (cell 6, last sentence): "Imagine how confusing it would be if we wanted to move the turtle 36 times to draw a star — that's a lot of repetitive code." — kid-TV-host register. Reword: "Drawing the 36-step star without a loop would mean 72 lines of nearly identical code."
- **Voice** (cell 18, tip): just restates what the cell above explained. Cut it.
- **Flow** (cell 5, code): `%run .lib/auto_turtle.py` and `tina = turtle(myTS)` with `# type: ignore[name-defined]` — this is a notebook-only macro that doesn't appear in any earlier lesson, and it differs from the `import turtle; tina = turtle.Turtle()` pattern used in the .py files. Either explain `auto_turtle` the first time it appears, or use the same `import turtle` pattern as the .py exercises.
- **Flow** (cells 11–18, ASCII-emoji "drawings"): the lesson pivots from turtle drawing to printing emoji grids (orange squares, checkerboard, American flag), then returns to a turtle exercise. The emoji-grid section uses `if`/`elif`/`else`, modulo (`%`), nested loops, and the `end=''` keyword to `print()` — none of which have been introduced. Either move this to a later lesson where conditionals exist, or label it clearly as preview material with the syntax explained.
- **Flow** (cell 17, code): the American flag uses nested `if`/`else`, modulo, and `end=''`. Far past PCEP "first loop" territory. Same fix as above.
- **Technical** (cell 2, code comment): "Loop will run 4 times from 0 to 3" is stated again two lines down ("range(4) generates numbers 0, 1, 2, 3"). Pick one.
- **Technical** (cell 5): inconsistent indentation/spacing between `tina.goto(150, 0)` and the comment compared to surrounding lines. Tidy up.
- **Technical** (cell 8): comments mention coordinates without explaining what they mean. Add a one-line note that (0,0) is the center.
- **Technical** (cell 9, "Star repeats … 36 times"): the figure isn't a star — `range(36)` with `left(170)` produces a 36-pointed rosette, not the "star" most kids picture. Either say "star pattern" consistently or pick angles that produce a recognizable 5-point star.

## lessons/10_Turtles/40_Loops/20_Loop_with_Turtle.py

- **Flow** (lines 11–12, docstring): contains `uid: 85lNu5qj` / `name: Loop With Turtle` metadata that's not in any other student-facing .py file in the module. Move metadata to a comment outside the docstring or strip it.
- **Technical** (line 23, comment): "Repeat forward + left three more times to finish the square." — same false-imperative issue as in Squares_and_Circles.py: the next eight lines already do this. Reword to describe what's already there, since the student is supposed to *replace* the repetition with a loop.

## lessons/10_Turtles/40_Loops/30_Loop_with_Turtle.py

- **Flow** (line 4, instructions): the assignment says "use a loop to draw a regular pentagon" but the file is empty. Without the angle hint (72°) and with the previous file having had structure laid out, the jump to a blank file is abrupt. Add boilerplate (`import turtle`, `setup`, `tina = turtle.Turtle()`, `turtle.exitonclick()`) so the student fills in the loop body, not the whole program.
- **Technical** (lines 12–13, docstring): same `uid:` / `name:` metadata leaking into the docstring as in `20_Loop_with_Turtle.py`.

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Voice** (cell 8): "You don't need to memorize all these types right now—let's just look at some examples to see how they work!" — only exclamation point in the lesson, attached to filler. Replace with "These examples show how a few of them work."
- **Voice** (cell 1, "In case you got stuck on the previous lesson, here is one way you could have solved it"): implies the previous lesson had an exercise the student attempted. Either rephrase as "if you tried the pentagon exercise…" or move the solution next to the exercise.
- **Flow** (cell 8, "Different Types of Variables"): introduces eight types — int, float, str, bool, list, tuple, dict, set, NoneType — when only int, float, str, bool are demonstrated. Lists arrive in lesson 80; dicts/sets/tuples/None aren't taught in the module at all. Trim.
- **Flow** (cell 13, code): another `%run .lib/auto_turtle.py` / `turtle(myTS)` invocation — same convention drift as 40_Loops.
- **Technical** (cell 15, exercise): the lines `height_difference = `, `area = `, `doubled = ` are intentional stubs, but the surrounding text never shows the student a worked example. Add a short worked-example block right above the exercise.
- **Scope** (cell 8): "tuples", "sets", and "NoneType" are not on the PCEP outline at the depth implied here, and aren't taught later in the module. Drop or defer.

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Voice** (cell 0, opening paragraph): "By the end, you'll be able to write your own reusable code blocks to perform calculations, make decisions, and more." — corporate-training register. Reword: "By the end, you'll be writing your own reusable functions."
- **Flow** (cell 13, "Advanced Function Examples"): introduces `if`/`elif`/`else`, comparison operators, default parameter values, `from math import ceil`, **and** multiple-return-value tuple unpacking (`slices, pizzas = pizza_calculator(10)`) — all in one cell, none introduced yet, none reused later. Split or remove. At minimum drop the tuple-unpacking return.
- **Flow** (cell 15, code): another `auto_turtle` macro instead of the standard `import turtle` setup the .py exercises use.
- **Technical** (cell 17, exercise): comment "use a loop to print numbers from start_number down to 1" implies counting down — `range(start_number, 0, -1)` requires the three-argument form, which has only been used as `range(n)` and `range(a, b)`. Mention the step argument or change the exercise to count up.
- **Scope** (cell 13): tuple return + tuple-unpacking assignment is on the edge of PCEP scope and isn't reused. Cut.

## lessons/10_Turtles/50_Variables_and_Functions/20_Efficient_Turtle.py

- **Flow** (line 19, `def draw_polygon(sides):`): student is asked to define a function whose body uses both a loop and a calculation, with `forward` and `left` distance still unspecified. Either add a `size` parameter to the stub or hard-code a `size = 50` line above the function so the student isn't guessing.

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Voice** (cell 0, opening): "Check out this link, or take a look below!" — exclamation point on a transitional sentence. Drop the `!`.
- **Flow** (cell 2): `set_turtle_image()` uses `from pathlib import Path`, `Path(__file__).parent / "images"`, and `str(...)` — none introduced. The function is presented as a copy-this-and-reuse-it black box, which is reasonable, but it's the first `from … import …`. One sentence saying "you don't need to understand the `pathlib` part" would fix this.
- **Flow** (cell 5): `from PIL import Image` is required for `set_background_image()`. Pillow isn't a stdlib module. Flag the dependency at the top of the lesson or check the course environment ships with Pillow.
- **Flow** (cell 11): introduces `lambda` (`t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))`), with the explanation deferred to "we will go over how to use the lambda function later on". Lambdas aren't on the PCEP track and don't appear later. Use the named `make_handler(t)` form as the primary example.
- **Technical** (cell 7): the `for i in range(-200, 200):` loop runs 400 turtle moves with no `screen.exitonclick()` or `turtle.done()` at the end. The window will close as soon as the loop finishes. Add a closing call.
- **Technical** (cell 9): explanation of `done` vs `exitonclick` is correct, but earlier examples in the module used `exitonclick()` without explaining the difference. Add a callback to the earlier lessons.
- **Scope** (cell 11–12): `lambda` is explicitly out of PCEP-entry scope. Drop it from the primary example.

## lessons/10_Turtles/60_More_Turtle_Programs/20_More_Turtle_Programs.py

- **Flow**: file is two-line instructions inside a docstring, with no boilerplate. The student is asked to "copy the code from the previous lesson" — fine, but every other exercise file in the module includes at least `import turtle` and `turtle.exitonclick()`. Add minimal boilerplate.

## lessons/10_Turtles/60_More_Turtle_Programs/30_More_Turtle_Programs.py

- **Flow** (lines 1–7): same as above — file consists of instructions in a docstring with no boilerplate. Add an `import turtle` skeleton.

## lessons/10_Turtles/60_More_Turtle_Programs/40_More_Turtle_Programs.py

- **Flow** (lines 8–12, hint): the `random.randint(-300, 300)` snippet is the first appearance of `random` in this file, but `random` was already used in `90_Graphics_Projects` files. Add a one-line "you'll need `import random` at the top".

## lessons/10_Turtles/70_Projects/10_LeagueBot.py

- **Technical** (line 6, instructions): "Change the turtle image to `'leaguebot_bot.gif'`" — the file in `images/` is named `leaguebot_bolt.gif` (with an "L"). The student's program will fail. Fix to `leaguebot_bolt.gif` (or rename the asset).
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
- **Technical** (cell 1): the cell ends with the bare expression `things_to_buy` to display the list. Notebook-only behavior; won't work in a `.py` file. Add a brief note or change to `print(things_to_buy)`.
- **Technical** (cell 3): same bare-expression display (`things_to_buy[1]`). Same fix.
- **Technical** (cell 12): the example uses `[90, 90, 90, 90]` — four identical 90s. The point of using a list of angles is to vary them. Use `[60, 120, 60, 120]` or something visibly varied.

## lessons/10_Turtles/80_Introducing_Lists/20_Color_Lines.py

- **Flow** (line 20): "Make another square, but put the colors in reverse order, using a negative index" — negative indexing wasn't covered in `10_Lists.ipynb`. Either add it to the lesson or change the instruction.

## lessons/10_Turtles/90_Graphics_Projects/10_Flaming_Ninja_Star.py

- **Technical** (line 17, `"#%06X" % (random.randint(0, 0xFFFFFF))`): printf-style `%` formatting and hex literals appear here for the first time without explanation. A one-line comment ("returns a random hex color string like `#A1B2C3`") would help.
- **Technical** (line 23, `colors[i % len(colors)]`): `get_next_color` is defined but never called. Remove the unused function.
- **Technical** (lines 20–24, ordering): the global `colors` list and `get_next_color` are defined between `get_random_color` and the rest of the setup, splitting the function definitions. Move them together.

## lessons/10_Turtles/90_Graphics_Projects/20_Crazy_Spiral.py

- **Flow** (lines 26–27, instructions): "The second `...` in the for loop should be the number of shapes you want to make, for example 100, or a list of numbers." — confusing because the template above has `num_shapes = ...` on line 28. Clarify which `...` the comment refers to.
- **Technical** (line 31): `t.right(360/num_shapes)` is fine if `num_shapes` is an int, but if it's a list (per the suggestion in the comment), it's a TypeError. Drop the "list of numbers" suggestion.

## lessons/10_Turtles/90_Graphics_Projects/30_Pentagon_Crazy.py

- **Technical** (line 16): `get_random_color` defined but never called. Remove.
- **Technical** (line 33): the loop uses `i == 100` and `i == 200` as triggers to change pen width. Magic numbers should be named.

## lessons/10_Turtles/90_Graphics_Projects/40_Turtle_Spiral.py

- **Voice** (line 47, comment): "Check the pattern against the picture in the recipe. If it matches, you are done." — what "recipe" and "picture"? There's no image referenced in the file or its README. Either link the picture or drop the line.

## lessons/10_Turtles/Module_One_Quiz.ipynb

- **Technical** (cell 1, code): `display_quiz("../../lessons/.jtl/Quiz_Data/Module_One_Quiz.json")` — the relative path goes up two directories from `lessons/10_Turtles/`, which is wrong by one. Correct path is `../.jtl/Quiz_Data/Module_One_Quiz.json`.
- **Technical** (cell 2): empty code cell. Remove.
- **Flow**: notebook is named "Module One Quiz" but Module 10 is the first module of the *Turtles* unit. Rename to "Module 10 Quiz" or "Turtles Quiz" for consistency with the directory name.

---

# Module 20 — Types and Logic

## lessons/20_Types_and_Logic/README.md

- **Flow** (PCEP Alignment list, section 2.1): lists "Bitwise Operators: `~` `&` `^` `|` `<<` `>>`" as covered, but no lesson teaches bitwise operators. Either remove the bullet or add a short bitwise lesson.
- **Flow** (PCEP Alignment list, section 2.2): lists "The `sep=` and `end=` Keyword Parameters" as covered, but neither parameter appears in any lesson. Remove the bullet or add coverage.
- **Flow** (PCEP Alignment list, section 1.3): lists "Naming Conventions" as covered, but no lesson explicitly teaches `snake_case` / `PascalCase` / valid identifier rules. Remove or add a short "Naming variables" subsection.

## lessons/20_Types_and_Logic/10_Operators_and_Types.ipynb

- **Voice** (cell 1, "When you're ready to begin, run the code block below."): mild kid-TV phrasing; cut to "Run the cell below to create a few variables of different types." or just delete it.
- **Flow** (cell 5, common types list): lists Integers, Floats, Strings, and Lists as the four most common types, treating `bool` and `dict` as afterthoughts. PCEP treats `bool` as one of the core literal types. Promote `bool` into the main list, or add a one-line `bool` example in the same code cell.
- **Flow** (cell 5, "Lists" bullet): this is the first time `mutable`/`immutable` appear. Briefly note "we'll come back to mutability later" rather than putting the load-bearing definition in a hover tooltip.
- **Technical** (cell 11, operator table): the `**` row uses `$2$ ** $3$` with `**` outside math mode while every other operator is wrapped in `$...$`. Make consistent.
- **Technical** (cell 18, final two prints): the "Verification" line prints `(2 * 4) + 3 = 11` and the next prints `Result: 11`. Two separate labels for the same verification is confusing — collapse into one.
- **Technical** (cell 20, `for` loop): first appearance of `for i in range(10)` with a bound variable used inside the body. Module 10 only used `for _ in range(N)`. Add a one-line note that `i` takes on each value `0..9`.
- **Flow** (cell 22, exercise): `kids = ...` and `candy_bars = ...` left as `Ellipsis` mean if a student runs the cell before filling in, they get a confusing `TypeError` involving `'ellipsis'`. Use bare `kids =` (cleaner syntax error) or add a hint comment.

## lessons/20_Types_and_Logic/20_String_Operations.ipynb

- **Technical** (cell 0, note at end): "Strings are immutable, meaning once they are created, they cannot be changed, or used in mathematical operations without conversion." The "or used in mathematical operations" clause has nothing to do with immutability. Split into two sentences.
- **Flow** (cell 7, intro to string methods): lists `.upper()`, `.lower()`, `.replace()`, `.split()` as the methods the lesson will cover, but cell 8 also demonstrates `.title()`, `.startswith()`, `.endswith()`, and `.strip()` without introducing them. Either expand the introductory list or trim cell 8.
- **Technical** (cell 8): `s.replace('World', 'Python')` uses single quotes but the rest of the lesson uses double quotes. Pick one.
- **Voice** (cell 15, "Test Yourself"): cell 16 names variables `hello`, `name`, `greet`, `hello3`, `s`, `titled` — `hello3` is not a great name. Rename to `hello_repeated` or `greeting_x3`.
- **Technical** (cell 16, exercise stub): `greet = ... #` ends with a trailing `#` and an empty comment. Drop or add the actual hint.

## lessons/20_Types_and_Logic/30_Control_Flow.ipynb

- **Technical** (cell 10, lunch-time check): `if time > "11:30" and time < "12:30"` does lexicographic string comparison, not numeric. Works for "11:31" by accident but breaks for `"9:30"` vs `"11:00"` (since `"9" > "1"` lexicographically). Switch to integers (`hour, minute = 11, 31`) or call out that this only works because all the strings are zero-padded `HH:MM`.
- **Technical** (cell 18, `if maybe_its_true == True`): comparing booleans to `True`/`False` with `==` is a PEP 8 anti-pattern (E712). Teach the idiomatic form: `if maybe_its_true:`.
- **Technical** (cell 20, `else` comment): the comment reads `# do this if maybe_this == False and maybe_that == False` but `else` runs when neither preceding condition matched, not when the variables themselves are `False`. Rewrite as `# do this if neither of the conditions above was true`.
- **Flow** (cell 21, forward reference to `try`/`except`): the tip says `if-elif-else` blocks "are useful when paired with `try` and `except` blocks to handle errors" — but `try`/`except` is its own control structure, not a partner of `if`. Remove the tip or rephrase as "We'll cover `try`/`except` for handling errors in a later module."
- **Flow** (cell 25, `convert_ml_to_imperial`): first appearance of `def` with a parameter, `input()`, and `float()` casting together — too much new mechanics inside one example whose actual point is `if`/`elif`. Split into two cells.
- **Technical** (cell 25, comparison threshold): `if ml <= teaspoon_ml` fires on any `ml <= 4.92892`, including `0` and negatives. Add a guard `if ml < 0: ...` or note the assumption that `ml > 0`.
- **Voice** (cell 10, code comment): `print("Hooray!")` — kid-TV exclamation. Replace with something matter-of-fact like `print("Both checks passed.")`.

## lessons/20_Types_and_Logic/40_Working_With_Numbers.ipynb

- **Technical** (cell 0, hex example): the literal is written `0x2f3` (lowercase `f`) but the place-value table writes `F (15)`. Pick a single case.
- **Technical** (cell 0, decimal place-value example): "decimal number $255$ can be broken down by its place values into $(2 \times 100) + (5 \times 10) + (5 \times 1)$" — spell out positions explicitly: "$255 = (2 \times 10^2) + (5 \times 10^1) + (5 \times 10^0)$".
- **Flow** (cell 0): the three `<details>` sections include a deeper dive than PCEP requires. Add one sentence above the block: "Open these only if you want a deeper walkthrough — you don't need them to use the `bin()`/`oct()`/`hex()` functions below."
- **Technical** (cell 5, scientific notation claim): note that `1e6` is a `float` in Python, not an `int` (`type(1e6)` returns `float`). This trips up students who type `1e6` expecting an integer.
- **Flow** (cell 7, exercise): asks to print age "in decimal", "in hexadecimal", "in octal", "in binary", and finally "modulo 3". The modulo-3 line wasn't motivated by anything in this lesson. Drop it or tie it back explicitly.

## lessons/20_Types_and_Logic/50_My_Ages.py

- **Voice** (line 16, docstring): `print "You are pretty awesome!"` — "awesome" used as an intensifier. Replace with `print("You're the same age as me.")`.
- **Flow** (line 33, tkinter import): first appearance of `from tkinter import messagebox, simpledialog, Tk` in the curriculum. No preceding lesson introduces the Tk pattern. Add a paragraph explaining `Tk`, `withdraw`, and `mainloop`, or add a tiny "Hello, tkinter" lesson before this one.
- **Technical** (line 21, docstring snippet): docstring shows `simpledialog.askinteger(...)` example but the surrounding scaffold leaves `# Ask the user's age` as a stub. Make clear the docstring is a template: "Use this pattern to ask for the user's age:".
- **Technical** (line 47, TODO comment): `# TODO:` reads like leftover engineering scaffolding. Replace with `# Stretch goal:` or `# Bonus:`.

## lessons/20_Types_and_Logic/60_Simple_Adder.py

- **Flow** (lines 10–22): all six steps require knowing the tkinter pattern from `50_My_Ages.py`, but `50_My_Ages.py` only sketched the pattern in a docstring. Add a "Reference example" pointer at the top: `# See 50_My_Ages.py for the import and Tk()/withdraw() pattern.`
- **Technical** (line 20): the student needs to know `simpledialog.askinteger` returns an `int` (or `None` if cancelled), and `messagebox.showinfo` needs a string. Add a one-line hint about converting the sum to a string.

## lessons/20_Types_and_Logic/70_Infuriating_Calculator.py

- **Voice** (lines 1–5): "Let's write a calculator that's really hard to use, not because we want it to be hard, but just because we haven't learned how to make it easy yet." — chatty meta-aside. Tighten to: "Write a calculator that asks for inputs one at a time. Later lessons will show how to make this friendlier."
- **Technical** (lines 30–32): division by an integer that doesn't divide evenly will surprise students unless they pick `askfloat()`. Recommend `askfloat()` for both numbers, or note that `int / int` returns a `float` in Python 3.

## lessons/20_Types_and_Logic/80_Code_Challenges.ipynb

- **Flow** (cell 2): first time the curriculum iterates a `for` loop over an explicit list of values (`for n in [2, 3, 4, ...]`). Module 10 covered `for _ in range(N)` only; Module 20's lesson 10 used `for i in range(10)`. Add a one-line note ("`for n in [...]` runs the body once for each value in the list").
- **Voice** (cell 0, "Code Wars" paragraph): "...Code Wars has a more competitive and gamified experience—think of it like Rocket League for coding." — surrounding pitch reads like marketing copy. Trim.
- **Technical** (cell 1, challenge wording): "If $n$ is even and in the range 2 to 5 (inclusive), print `not weird`" — only `2` and `4` are even in `2..5`. Reword for clarity.

## lessons/20_Types_and_Logic/lib/03_badgers_tk.py

- **Technical** (line 31): `return 'mushroom' # Always show a snake` — comment says "snake" but code returns `'mushroom'`. Fix the comment.
- **Flow** (whole file): file is in `lib/` but isn't referenced by any of the notebooks or `.py` files in this module. If it's the intended FizzBuzz UI for `30_Control_Flow.ipynb`, link it from cell 22; otherwise move it.

## lessons/20_Types_and_Logic/lib/badgers.py

- **Technical** (line 18, bare `except`): catches `BaseException`, including `KeyboardInterrupt`. Use `except (ValueError, TypeError):` or at minimum `except Exception:`.
- **Technical** (line 7): docstring for `FizzBuzzer` is preceded by a blank line, so it's not picked up as the class docstring. Move it directly under `class FizzBuzzer:`.
- **Technical** (lines 14–19): `isnumber` is defined inside `update_display` and re-defined every call. Pull it out to module level.

---

# Module 30 — Loops

## lessons/30_Loops/10_Iteration.ipynb

- **Voice** (cell 0, opening paragraph): "loops are actually a lot more interesting" and "expads it to make it even more useful" — mildly cheerleader-ish and contains a typo ("expads"). Rewrite: "In this module we'll go further with iteration: looping over collections, generating sequences with `range()`, and working with lists, tuples, and strings."
- **Flow** (cell 4, "What is an Iterable?" table): mentions Tuple before tuples have been introduced (lesson 50). Either flag with "we'll cover tuples later" or remove the row.
- **Flow** (cell 4): introduces `list()` as "one of the ways to iterate over an iterable" — but `list()` consumes an iterable into a list. Rewrite: "One way to peek at an iterable's contents is to pass it to `list()`, which collects every item into a list."
- **Flow** (cell 13): mentions `enumerate()` before lesson 120 introduces it; references `.replace()`/`.lower()`/`.upper()` before lesson 80. Drop or add forward references.
- **Flow** (cell 14, name-choice table): rows for `for x, y, z in coordinates:` and `for red, green, blue in colors:` use tuple unpacking, which the student hasn't seen. Remove or add a callout.
- **Technical** (cell 0): typo "expads" → "expands."
- **Technical** (cell 1, comment): "This loop repeats 10 times" is fine, but cell 12 says "This loop repeats 12 times, printing each character in the string 'Hello World!'". "12 times" is over-specific and brittle.
- **Technical** (cell 5, code): `print( list("This is a string"))` has stray space after the opening paren — clean for PEP 8.
- **Technical** (cell 14, table): duplicate "Numbers" rows (one for `numbers` list, one for `range(10)`). Merge or relabel.

## lessons/30_Loops/20_Loops_with_Range.ipynb

- **Voice** (cell 9): "These [Badgers]..., but instead, they have their own rules" reads slightly stilted. Tighten to: "These badgers play their own version of FizzBuzz."
- **Flow** (cell 7, Challenge): the exercise stub in cell 8 is just `...` with no scaffolding. Add a hint comment like `# Use range(start, stop, step) with the right step value`.
- **Flow** (cell 9, Badger FizzBuzz challenge): introduces conditional / divisibility logic that requires nested `if/elif/else`. Add a one-line callback ("Use `if`/`elif`/`else` and the `%` operator from module 20").
- **Technical** (cell 5): the cell evaluates `list(range(101, 120, 2))` as a bare expression. Wrap in `print(...)` for consistency with the other "Run Me!" cells.
- **Technical** (cell 9, table): "🐍 snake!" has an exclamation point inconsistent with surrounding cells; drop the `!`.

## lessons/30_Loops/30_Looping_Through_Lists.ipynb

- **Flow** (cell 9280847b, indexing intro): introduces `backpack[0]` indexing here, but the dedicated indexing/slicing lesson is 60. Trim the explanation to "as we saw before."
- **Flow** (cell 9e90bab0): converting `range()` to a list was already shown in lessons 10 and 20; this re-introduction is redundant. Cut or label as recap.
- **Flow** (cell d63d5efe): comment `my_list.append(c) # Adding to a list, more on this later` — the very next "Adding To Lists" section *is* "later." Replace with `# Adds c to the end of the list`.
- **Flow** (cell 7bd259e4): sorting is introduced here without warning, then never used in the challenge. The challenge does use `.sort()`, so make that callback explicit.
- **Flow** (cell c8f4a193, Challenge): requires `input()`, which has not been formally introduced. Add a one-line note.
- **Technical** (cell 0e2837fd): uses bare `backpack` as the last expression to "display" — works in Jupyter but inconsistent with the explicit `print()` style. Use `print(backpack)`.
- **Technical** (cell b2a608ff): `# type: ignore[name-defined]` comments are noise to a beginner reader; hide or move explanation to a single comment block.
- **Technical** (cell 17a599ca): the cell only has a `# Try adding...` comment with no `my_list` declaration — students may run in isolation and get `NameError`. Re-declare `my_list` in the stub.

## lessons/30_Loops/40_Crazy_Tina.py

- **Technical** (line 22): `tina.speed(2)` with comment "Move at a moderate speed, not too fast" — speed 2 is quite slow. Use `tina.speed(6)` or change the comment.

## lessons/30_Loops/50_Tuples.ipynb

- **Flow** (cell 10, Tuple Unpacking): introduces tuple unpacking here, but lesson 120 also introduces it more thoroughly with `enumerate()`. Add a forward-reference: "We'll see more uses for unpacking in the iteration-functions lesson."
- **Flow** (cell 12, Use Cases): mentions "They can also be used as keys in a dictionary, whereas lists cannot." Dictionaries have not been introduced. Drop the dictionary mention or add "(dictionaries come up in the next module)."
- **Technical** (cell 6): the code is intentionally a `TypeError` demonstration. Wrap with `try/except` to avoid stopping notebook execution, or note explicitly that the cell will error.

## lessons/30_Loops/60_Indexing_and_Slicing.ipynb

- **Flow** (cell 0): says "Lists and strings are sequences of items" — but tuples were just covered in lesson 50 and they also support indexing/slicing. Add tuples.
- **Flow** (cell 13, IndexError demo): the cell will crash on execution. Wrap in `try/except IndexError as e: print(e)` or add a markdown note.
- **Technical** (cell 3, ASCII diagram): index labels under the boxes are misaligned visually. Verify alignment.
- **Technical** (cell 7): wording "to 8th... not including the 9th" is confusing — say "from the 3rd through the 8th item (stops before the 9th)."

## lessons/30_Loops/70_List_Story.py

- **Flow** (line 19): the student is told to use indexing and append, then the final line uses `' '.join(story)` — `.join()` is introduced in 80_Strings, but 80 comes *after* 70. Either move this exercise after 80 or scaffold `.join()` in a comment.
- **Voice** (lines 11–12): word list mixes emoji and text tokens. `'⚽.'` glues a punctuation mark to the emoji. Split into `'⚽'` and `'.'` so students have flexibility.

## lessons/30_Loops/80_Strings.ipynb

- **Voice** (cell 26, comment): `# Doesn't that look weird?` — kid-TV-host moment. Replace with `# Note: the separator string comes first, then .join()`.
- **Voice** (cell 9, header): "Fancy Formatting (f-strings)" — use "String Formatting with f-strings."
- **Flow** (cell 0, scope): teaches f-strings, escape sequences, `.split()`, `.join()`, slicing within strings, and a "rebuild a sentence" challenge. At least four distinct concepts. Existing structure stands per CLAUDE.md, so flag only.
- **Flow** (cell 3, escaping intro): introduces "kernel" with a tooltip but never explains what a kernel is in beginner-friendly terms. Use "Python interpreter" instead.
- **Flow** (cell 33): example uses heavy slicing/indexing combinations. Add a simpler intermediate example before the dense one.
- **Technical** (cell 1, code): `triple = """“Hope” is the thing with feathers...` uses curly Unicode quotes. Add a note that those are decorative inside the string, not Python syntax.
- **Technical** (cell 13): the alignment example produces left-aligned text by default. Clarify that the default alignment is left for strings and right for numbers.
- **Technical** (cell 17, challenge spec): be explicit that "The loop number, taking up 3 spaces" means right-aligned width using `{n:3}` and `{n:5}`.

## lessons/30_Loops/90_Fizz_Buzz_Badgers.py

- **Technical** (lines 25–32): the docstring rules list "evenly divisible by 15" third while the code correctly checks `% 15` first. Reorder the docstring rules to match the code (15, 5, 3).
- **Voice** (line 13): the file's task is essentially "change the start/step of `range()`" — make this explicit so students don't hunt.

## lessons/30_Loops/100_For_Loop_Gauntlet.ipynb

- **Voice** (cell 539e9340): trim "Carefully read and complete each challenge below" to "Complete each challenge."
- **Flow** (cell beb062f6): example uses an f-string `f"({i},{j})"` and `print(..., end=' ')`. The `end=` parameter could use a one-liner explanation since it's the first explicit use in this module.
- **Flow** (cell dee7d3d2): the multiplication-table bonus expects fixed column widths. Direct students to f-string padding `{n:3}` from lesson 80, or accept `\t` tab separation.

## lessons/30_Loops/110_FizzBuzz_Gui_Grid.py

- **Scope** (whole file): introduces `guizero`, a third-party GUI library not previously used and not part of PCEP scope. Move to extras/optional or document the deviation.
- **Flow** (line 13): same FizzBuzz logic was just covered in 90_Fizz_Buzz_Badgers.py. Add a one-line callback.
- **Technical** (line 34): `%` and `//` were introduced in module 20, but a brief reminder of `n % 10` (last digit) and `n // 10` (drop last digit) would help.
- **Technical** (line 40): `Box` is imported but never used. Remove from import.

## lessons/30_Loops/120_More_Iterables.ipynb

- **Voice** (cell 12, comment): `# <- Ok, look, unpacking!` — kid-TV-host. Replace with `# Note: each iteration unpacks the pair into list1, list2`.
- **Voice** (cell 22, comment): `# Important, but you knew that!` — drop. Just `# islice() comes from itertools`.
- **Voice** (cell 23, header): "A Slice of Infinite Possibilities" — re-explains `islice()` after it was just introduced. Remove duplicate or rename to "More on `islice()`."
- **Voice** (cell 32): "The real power comes from combining these functions together!" — drop. Use "These functions compose well — here are some practical combinations."
- **Voice** (cell 0): "Python has some very important iteration functions" — drop "very."
- **Flow** (whole file): covers `enumerate`, `zip`, `zip_longest`, `islice`, `cycle`, `chain`, `repeat`, plus tuple unpacking with `*rest`, plus building dictionaries from `zip()`. Serious one-concept-per-lesson violation. Flag only per CLAUDE.md.
- **Flow** (cell 8, "Nested Unpacking"): the example `for color, (item1, item2) in zip(colors, pairs):` is dense. Move to "Extras" or simplify.
- **Flow** (cell 20, dictionaries): builds a dictionary with `zip()`, but dictionaries are not part of this module. Drop or flag as preview.
- **Flow** (cell 33): uses ternary expression in a checkerboard example. Use a plain `if/else` block.
- **Scope** (cell 9, `*rest` unpacking): borderline-PCEP. Move to Extras.
- **Scope** (cells 25–26): `itertools.cycle`, `chain`, `repeat`, `islice`, `zip_longest` are all from `itertools` and not on PCEP. Move to optional lesson.
- **Technical** (cell 31, `repeat([], 5)`): produces five references to *the same* empty list — a classic gotcha. Add a warning or change the example.

## lessons/30_Loops/130_Iterable_Turtle.py

- **Flow** (line 4): docstring mentions `cycle` and `slice` (`islice`) from lesson 120. If 120 moves to extras, this exercise loses prerequisites. Coordinate.
- **Technical** (line 19): variable name `something` is a placeholder. Add a comment hint like `# Replace 'something' with a tuple unpacking like (color, (angle, distance))`.

## lessons/30_Loops/140_More_Loops.ipynb

- **Flow** (lesson placement): `while` loops are introduced in lesson 140 — quite late. PCEP treats `while` and `for` as peers. Consider whether `while` should appear earlier. Flag only.
- **Flow** (cell 0): the body of the while-loop example increments but never prints. Add a `print(s)` so the example is observable.
- **Flow** (cell 2, `count()` from itertools): use a simpler example — a plain `for i in range(100):` with `break`.
- **Flow** (cell 8): nested loops with `break` and `for/else` together is a heavy lift for the first encounter. Add walkthrough or simplify to a flat example first.
- **Technical** (cell 11): `else` clause attached to `while True:` is unreachable — worth a comment: `# Note: this else is unreachable because while True never becomes False.`
- **Scope** (cell 2): `itertools.count()` is out of PCEP scope. Replace with a plain integer counter.

## lessons/30_Loops/150_Number_Guess.py

- **Flow** (line 26): `ask_integer` is defined in this file (line 39) but uses `try/except`, which has not been introduced. Either explain `try/except` briefly in a comment, or pre-define `ask_integer` in a helper file.
- **Flow** (lines 41–45): student reading the file will encounter `try` and `except` for the first time. Add a one-line comment.
- **Technical** (line 19): the spec says "If the user's guess is divisible by 7, tell the user 'that is a very bad number, starting over' and pick another number" — but lines 4–6 say to pick another *random* number when *the random number itself* is divisible by 7. Reconcile: which is divisible by 7 — the guess, or the secret number?

## lessons/30_Loops/160_Extras.ipynb

- **Scope** (cell 2): list comprehension is explicitly out of PCEP scope per CLAUDE.md. The "Extras" framing makes this acceptable, but add an explicit line: "List comprehensions are beyond PCEP — included here for fun."
- **Scope** (cell 4): Euler version uses a `lambda` inside a list comprehension. Add a similar disclaimer.
- **Technical** (cell 2): `'fizz'*(i % 3 == 0) + 'buzz'*(i % 5 == 0) or str(i)` relies on the truthiness of the empty string. Add a brief comment explaining the trick.

## lessons/30_Loops/README.md

- **Scope**: lists "List Comprehensions" under section 4.1 — but CLAUDE.md says comprehensions are out of scope. Either remove or annotate as "covered briefly in Extras only."
- **Flow**: mentions "Lists in Lists: Matrices and Cubes" but no lesson covers nested lists explicitly. Remove or add coverage.
- **Flow**: mentions "The `del` Instruction" but no lesson teaches `del`. Remove or add coverage.
- **Flow**: mentions "Lists Inside Tuples and Tuples Inside Lists" — `50_Tuples.ipynb` does not cover this. Remove or add coverage.

---

# Module 40 — Data Structures and Functions

## lessons/40_Data_Structures_Func/10_Functions.ipynb

- **Voice** (cell 0, title): "**Functions and Data Structures**" but this lesson is exclusively about functions. Rename to "**Functions**" so the title matches the contents.
- **Flow** (cell 0, opening): add a one-line roadmap (e.g. "This lesson covers parameters, defaults, scope, composition, and globals.").
- **Flow** (cells 7, 9, 11): three cells in a row deliberately fail with `# Run Me!` comments — students will think their environment is broken. Label as `# This will fail!` instead.
- **Flow** (cell 19, exercise hint): "Use `enumerate()`" — `enumerate()` was introduced in Module 30. Optional: a one-line callback.
- **Flow** (cells 31–33, "Closures"): the section is titled "Closures" but the content is about reading a global variable from inside a function — that's not a closure. Rename to "Global Variables" / "Variable Scope" or rewrite to show an actual closure.
- **Technical** (cell 7): `greet_user(name = "Bob", greeting)` — `SyntaxError` is raised at parse time, so in Jupyter the *whole cell* fails before any prior context loads. Move the function definition into cell 7 itself.
- **Technical** (cell 17): redefines `greet_user` from cell 14, then cell 32 in Closures redefines it again. Use distinct names (`greet_user_broken`, `greet_user_global`) to keep the namespace clean.
- **Technical** (cell 30, exercise stub): comment block says "c) 2 + 2 != 3 + 3 = 6" — the `= 6` at the end is a leftover from line (b). Delete `= 6`.
- **Technical** (cell 33): says "This is called **accessing a global variable**" — accurate, but the prior heading still says "Closures." Pick one term.
- **Scope** (cell 19, exercise): the `find_char` exercise can be solved without `enumerate()`. Consider an exercise that doesn't require any new looping construct.

## lessons/40_Data_Structures_Func/20_Exceptions.ipynb

- **Voice** (cell 4): "led to a crash" is slightly dramatic; consider "stopped the program before the loop could finish."
- **Flow** (cell 0, header): opens with `## **Exceptions**` (h2) while every other lesson in this module starts with `# **<title>**` (h1). Promote.
- **Flow** (cells 8, 10, 12, 14): four cells in a row deliberately raise exceptions with `# Run Me!` comments. Use `# This will raise an exception` instead.
- **Flow** (cell 19, exercise): "tell the user what the n-th number *in the list* is" but the example output uses `7` as the index into a 4-element list. The wording "the 7th number in the list" misleads. Rewrite to use a number small enough to succeed (e.g. `3rd` returning `45`) and a separate one that fails.
- **Technical** (cell 17): both `try` blocks contain only `pass  # do something`, so no exception will ever be raised. Replace with a real triggering call (e.g. `int("not a number")`).
- **Technical** (cell 18): "use it to catch ones you are not aware of" — confusing. Suggested: "save the bare `except Exception` for cases where you genuinely don't know what could go wrong."
- **Technical** (cell 20, exercise stub): the TODO list never spells out where IndexError handling fits. Add `# TODO: handle IndexError when n is too large`.

## lessons/40_Data_Structures_Func/30_Dicts_Sets.ipynb

- **Voice** (cell 10): "You know what a real dictionary is, right?" — kid-TV-host. Rewrite: "A real-world dictionary is a book that maps words to definitions. Python dictionaries do the same thing with key-value pairs."
- **Voice** (cell 11, comment): "a collection of superior words and their definitions" — "superior" is odd. Suggest "uncommon words" or "fancy words."
- **Flow** (cell 0): roadmap doesn't mention dicts even though dicts are half the lesson title. Add.
- **Flow** (cell 0, set syntax bullet): "note that empty `{}` creates a dict, so an empty set must be created with `set()`" — references dicts before they're introduced. Move or add a parenthetical.
- **Flow** (cell 19, "Unpacking Key-Value Pairs"): tuple unpacking introduced as if it's been seen before. Make the introduction explicit, or move to its own subsection.
- **Flow** (cell 20): `enumerate(my_dict.items())` is correct but visually busy. Show simpler `for key, value in d.items()` first, then enumerated.
- **Flow** (cell 30, exercise loop): `for my_set in funny_sentences:` — variable name `my_set` to iterate over a list of *strings* is misleading. Rename to `sentence`.
- **Technical** (cell 14): duplicate-key dict literal raises a SyntaxWarning in Python 3.12+. Mention or rewrite using sequential assignments.
- **Technical** (cell 22): `del my_dict['c']` shown without first showing dict's `.pop()`. Add `.pop()` alongside.
- **Technical** (cell 30, exercise): "return `'Funny'` and a list of the funny words found" — explicitly say "return a tuple of `('Funny', [list of words])`".

## lessons/40_Data_Structures_Func/40_Funny_Words_Db.py

- **Flow** (file-level): no README or notebook callout explaining how to run it (it needs `guizero`). Add a one-line note in the module README.
- **Technical** (lines 124–127): wraps definitions in literal emoji `"😂 "` and `" 🤡"`. CLAUDE.md says "Do not use emojis as substitutes for words" — these are decorative but baked into student-facing output. Consider `"[funny] "` or making decoration optional.
- **Technical** (line 169): `app.when_key_pressed = handle_enter` — accesses `event.tk_event.keysym`, which varies by guizero version. Use the documented `event.key` instead.
- **Technical** (line 65, `is_funny` stub): until the student implements `is_funny`, the emoji-wrapping branch is dead code. Add a comment near the stub: "Until you implement this, definitions will never be marked funny."
- **Technical** (line 105, `update_listbox` stub): the stub returns a non-empty placeholder list. The instruction "(For your function, you should set this list to the empty list)" is buried mid-comment. Make it more prominent.
- **Technical** (line 142, GUI sizing): `width="10"` and `width="25"` passed as strings to guizero TextBoxes. Use integers.

## lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb

- **Voice** (cell 6, code comment): "<--- HERE IS THE MAGIC" — kid-TV-ish. Replace with "# transpose the board".
- **Voice** (cell 7): "First, let's understand how `zip()` performs this magic trick." — drop "magic trick".
- **Voice** (cell 9): "Imagine the `*` as saying 'take apart this container...'" — tighten to: "The `*` unpacks the list so each row is passed as a separate argument."
- **Voice** (cell 30, header): "## **Challenge: Make It Better!**" — replace with "## **Challenge: Combine the Checks**".
- **Flow** (cell 0, title): "Splat, Zip, and Comprehensions" — file is named `50_Splat_Comprehension.ipynb` (singular). Pick one.
- **Flow** (cell 5, "Who Won?" header): the section is actually a transposition lesson. Rename to "## **Getting Columns from a Grid**" and let "Who Won?" come later.
- **Flow** (cells 22–24, diagonals exercise): student is asked to write a comprehension immediately after one introductory example. Add a worked example using an *index* before asking.
- **Flow** (cell 27, hint): "logic value" is non-standard. Use "truth value".
- **Flow** (cell 34, callback): verify path `../10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb` is correct relative to the current notebook.
- **Technical** (cell 6, `pretty_print_2d`): helper defined inside a "Run Me!" cell, then re-referenced throughout. If a student runs cells out of order, later calls fail. Move the helper to its own setup cell.
- **Technical** (cell 31, `transpose`): defines `transpose()` but cell 6 already showed `list(zip(*board))` doing the same thing. Reuse or factor out.
- **Scope** (cells 17–21): list comprehensions are taught directly. CLAUDE.md states comprehensions are explicitly **out of scope** for PCEP. The lesson title contains "Comprehension" and the exercises require writing comprehensions. Most significant scope violation in the module — either remove comprehensions (rewrite using explicit for-loops) or document the deviation explicitly.
- **Scope** (cell 5): `*` unpacking with `zip` is a step beyond PCEP scope.
- **Scope** (cell 31, `board[:]`): slicing-as-copy combined with `extend()` and comprehensions stacks several non-PCEP idioms.

## lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py

- **Flow** (line 5): docstring header `# 60_Tic_Tac_Toe.py` — drop the `#` since it's a docstring, not Markdown.
- **Flow** (lines 13–14): "use the constants X_MARK and O_MARK instead of the strings 'x' and 'o'" — but the previous notebook used lowercase `'x'`/`'o'` while this file defines `X_MARK = "X"` (uppercase). Students copying from the notebook will silently fail. Call this out at the top of the file.
- **Technical** (lines 53, 56, 75): mixes `.value` and `.text` on a guizero Text widget. guizero `Text` uses `.value` only. Standardize.
- **Technical** (line 102): `ttt = TicTacToe(check_win)` runs at import time, opening a window. Wrap in `if __name__ == "__main__":`.
- **Scope** (file-level): defining a class with `__init__`, `@property`, instance methods goes beyond PCEP scope (PCEP doesn't cover OOP). Acceptable as black-box scaffolding, but worth flagging since it's the first time students see `class`/`self`/`@property`.

## lessons/40_Data_Structures_Func/README.md

- **Flow**: lists only PCEP-30-02 4.3 (dictionaries) under "PCEP Alignment," but this module also covers functions, exceptions, and sets. Functions are PCEP 3.x and exceptions are PCEP 4.x. Expand.
- **Flow**: no mention of the project files (40_Funny_Words_Db.py, 60_Tic_Tac_Toe.py) or the splat/zip/comprehension lesson. Add a short outline.
- **Scope**: if comprehensions stay in `50_Splat_Comprehension.ipynb` despite CLAUDE.md saying they're out of scope, the README should note that decision. Otherwise rework the lesson.

---

# Module 50 — Projects

## lessons/50_Projects/README.md

- **Flow**: single paragraph with no list of lessons. Either drop PCEP Alignment from earlier modules' READMEs for consistency, or add a short "Projects in this module" list here.

## lessons/50_Projects/10_Hotel_Management.md

- **Voice** (Getting Started): "Code away, make sure to keep it organized so you know where things are and what they do." — slightly throwaway. Replace with "Then start coding. Keep things organized so you can find them again later."
- **Voice** (closing line): "Have fun." as a bare one-liner reads like filler. Drop or fold into a real summary.
- **Voice** (Getting Started, third bullet): "Write down your thoughts as a list or instructions to yourself inside the docstring" — unusual advice. Move to a separate plan/`README` file or teach a "comments at the top" convention.
- **Flow** (Getting Started): "Add your imports (tkinter or whatever you need)" — curriculum doesn't teach Tkinter directly. Module 20 uses `tkinter.simpledialog`/`messagebox` and Module 30/40 use `guizero`. Replace "tkinter" with "guizero (or `tkinter.simpledialog`)".
- **Flow** (Functionality Requirements): "Must be interactive, either in the command line with print() and input() or with Tkinter" — `input()` has not been formally introduced. Either swap for the dialog functions students have used, or add an "Using `input()`" intro.
- **Technical** (Requirements): capitalization is inconsistent ("While Loop", "Multiple Night Check in"). Standardize on lowercase prose.
- **Technical** (Requirements): the rule "The functions should, mostly, return something" with the `my_age = add(10, 5)` example repeats Module 40 material. Trim to one sentence.
- **Scope** (overall): no estimated time and no explicit minimum-to-pass vs. stretch goals. Add.

## lessons/50_Projects/20_Random_Walk.py

- **Voice** (docstring opening): "A simple turtle program that moves the turtle randomly in the grid" then "This program will perform a 'random walk' by moving the turtle randomly in the grid." — same sentence twice. Cut to one line.
- **Flow**: this is a turtle program in the Projects module, sitting after Hotel Management. Consider whether it should live with `10_Turtles/90_Graphics_Projects/`. If kept here, add a one-line note that it intentionally revisits Module 10 turtle skills.
- **Technical** (function docstring): student is told to make the turtle move "a fixed number of steps" but no `STEP_SIZE` constant. Add `# step_size = 10  # tweak to taste`.
- **Technical** (hint block): "Read one of the past turtle programs to see how to use these methods." — be specific. Point to e.g. `lessons/10_Turtles/90_Graphics_Projects/40_Turtle_Spiral.py`.
- **Scope**: deliverable is a single small function. Either trim framing to "warm-up exercise" or add a follow-up task (color by direction, count visits per cell).

## lessons/50_Projects/Temp_Project_Ideas/

- **Flow**: directory name `Temp_Project_Ideas` suggests draft material, but it sits in the published `lessons/` tree. Either rename the directory to `30_More_Projects/` and number the files, or move it to a top-level `drafts/` until ready.
- **Flow**: files inside are inconsistently named — `30_ASCII_Art.ipynb` has a numeric prefix but `Spin_The_Wheel.ipynb` and `Terminal_Game.ipynb` do not. Pick one.

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Voice** (cell 0, title): "**So you want to be an ASCII Artist?**" — borderline kid-TV-host. Prefer a flat title like "ASCII Art".
- **Voice** (cell 0): "There's more where that came from." — drop colloquial filler.
- **Voice** (cell 0): "Now you might be thinking, man, that looks complicated." — rewrite without the imagined-student-monologue framing.
- **Voice** (cell 0, "Note"): "the only requirement here is having fun" — contradicts the explicit Requirements cell. Drop or rephrase.
- **Voice** (Before You Begin): trim the emoji column.
- **Flow** (boilerplate code cell): worked example uses nested loops over a dict. If lesson placement is post-Module-40, that's fine; warn if lesson order is uncertain.
- **Technical** (boilerplate code cell): dict only contains the letters in "ASCII ART IS COOL" plus space. A student calling `print_ascii("HELLO")` sees nothing for `H`, `E`, `L`, `O`. Either include the full alphabet or add a comment.
- **Technical** (Exclusions, "No Hardcoding"): conflicts with the boilerplate, which hardcodes every character row. Reword.
- **Scope**: external-library suggestions (`art`, `pyfiglet`). Move to a "stretch" callout.

## lessons/50_Projects/Temp_Project_Ideas/Spin_The_Wheel.ipynb

- **Voice** (cell 0): "Do you know someone who likes to watch game shows on TV? Have you ever wanted to create your own?" — back-to-back rhetorical questions. Cut.
- **Voice** (cell 0): "This is your chance to get creative and have fun." — drop.
- **Voice** (cell 0): "Software development is all about problem-solving and creativity. So, think about how you can make your game engaging and enjoyable for players." — generic motivational filler. Cut.
- **Flow**: lesson is two short markdown cells with no example code, no scaffold, no exercise stub. Add a starter file or call out that the student writes from scratch.
- **Technical** (Assignment Requirements): "Display the total prizes won at the end of the game" but earlier "Keep track of the prizes won by each player" (multiplayer). Pick one.

## lessons/50_Projects/Temp_Project_Ideas/Terminal_Game.ipynb

- **Voice** (cell 0): "Have you ever wanted to create your own text-based adventure game that runs in the terminal?" — opening rhetorical question. Replace with "In this project you'll build a small text-based adventure game that runs in the terminal."
- **Flow**: two-and-a-half markdown cells with no starter code, no example play session, no concrete scope. The Warsim screenshot sets a target way out of reach. Either add a 2-room "find the key" walkthrough or pick a lower-key visual.
- **Flow** (Assignment Requirements): "Use control flow to manage game progression" duplicates "Implement user input to allow players to make choices". Tighten.
- **Scope**: starter image is from a complex strategy game (Warsim). Replace with something a PCEP-level student could plausibly produce.

---

# Cross-module sequencing

- **Functions taught twice — Module 10 informally, Module 40 formally — handled gracefully but framing misrepresents Module 10**: `40_Data_Structures_Func/10_Functions.ipynb` opens with "We've seen functions a few times, but haven't explained how they work in detail" — but Module 10's `50_Variables_and_Functions/20_Functions.ipynb` already covers `def`, parameters, return values, and looped calls. Module 40's intro should state more concretely *what's new*: keyword vs. positional args, default args, scope/globals, `pass` — none of which are in Module 10.

- **Lists taught twice — Module 10 (`80_Introducing_Lists`) and Module 30 (`30_Looping_Through_Lists`) — handled gracefully but Module 30 is mostly review**: by the end of Module 10, students already have indexing, iteration with `for`, and `append`/`insert`/`remove`/`len`/slicing. Decide whether `30_Loops/30_Looping_Through_Lists.ipynb` does meaningful new work or is mostly review.

- **`90_Graphics_Projects/10_Flaming_Ninja_Star.py` uses concepts not formally taught in Module 10**: uses `random.randint`, hex string formatting (`"#%06X" % ...`), modulo, and indexing. If lessons run in numeric order (`70_Projects` → `80_Introducing_Lists` → `90_Graphics_Projects`), then `90_*` is after lists and is fine. The bigger hole is `%`-formatting and `random.randint` — neither is taught in Module 10. Either add a one-cell "the `random` module" callout or move `90_Graphics_Projects/` to after Module 20.

- **Hole: `input()` is never properly introduced before it's required in `50_Projects/10_Hotel_Management.md`**: Module 20 uses `tkinter.simpledialog`/`messagebox`. Module 30's `150_Number_Guess.py` uses a custom `ask_integer` helper. By Module 50 the student is told they can use `print()` and `input()` — but `input()` has zero prior exposure. Add a short "Using `input()` and `print()`" subsection.

- **Hole: `guizero` is used in three projects (`30_Loops/110_FizzBuzz_Gui_Grid.py`, `40_Data_Structures_Func/40_Funny_Words_Db.py`, `40_Data_Structures_Func/60_Tic_Tac_Toe.py`) but never formally introduced**: `110_FizzBuzz_Gui_Grid.py` says "Don't worry about how it works — copy the examples", okay for one project but not three. Add a short `guizero` primer in Module 30 (before `110_*`) covering `App`, `Text`, `Box`, `PushButton`, `grid=`.

- **Scope conflict: list comprehensions are out of scope per CLAUDE.md but required in `40_Data_Structures_Func/50_Splat_Comprehension.ipynb` and downstream Tic Tac Toe**: this lesson goes well past "incidental use" — it teaches list comprehensions as a primary topic with their own exercises. `30_Loops/160_Extras.ipynb` also uses them. Note that Module 30 README's PCEP alignment lists "List Comprehensions" as a PCEP topic, so the CLAUDE.md guidance and the README contradict each other. Resolve which is correct.

- **`30_Loops/40_Crazy_Tina.py` references a section that doesn't exist**: docstring says "Review the 'Using Lists' section of the previous lesson" — there is no section titled "Using Lists" in `30_Looping_Through_Lists.ipynb`. Update the cross-reference or rename the section.

- **Module 30 has 16 lesson files; Module 40 has 6 — heavy pacing skew**: Module 30 covers `for`, `while`, range, lists, indexing/slicing, tuples, strings, plus a FizzBuzz GUI project — much overlapping Module 10's lists/loops intro. Consider moving basic-list material entirely to Module 30 (and trimming Module 10's `80_Introducing_Lists/`), or splitting Module 30 into "Loops" and "Sequences".

- **Filename casing inconsistent across modules**: Module 10 uses `Tash_Me_Click`, `Tash_Me_Twirl`, `LeagueBot`. Module 30 uses `Iterable_Turtle`, `List_Story`, `Fizz_Buzz_Badgers`. PEP 8 prefers `snake_case` for filenames — pick e.g. `20_tash_me.py`, `10_league_bot.py`.

- **Turtle naming drift**: Module 10 uses `tina` consistently. Module 30 uses `tina` and `t`. Module 50's `20_Random_Walk.py` calls the turtle `walker`. Fine variety, but `20_Random_Walk.py`'s docstring should add "you've used turtles before; this one is named `walker`" so the rename isn't jarring.

- **Module 10 README is shorter and missing PCEP alignment**: lists four bullet topics ("Variables, Loops, Functions, Lists") with PCEP Alignment only sections 1.1 and 1.2. Module 10 actually teaches enough to at least partially cover 1.3, 3.2, and 4.1. Either trim Module 10's content or expand the README's PCEP block.

- **Module 50 README says "complete projects" but `20_Random_Walk.py` is a single-function fill-in**: reframe README to "small to medium projects", or upgrade Random Walk.
