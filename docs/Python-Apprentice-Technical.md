# Python Apprentice — Technical Review

Split from `Python-Apprentice-Review.md`. This file keeps only the `Technical` findings.

---

# Module 10 — Turtles

## lessons/10_Turtles/10_Welcome/10_Welcome.ipynb

- **Technical** (cell 0, embedded SVGs): every glossary term is followed by a 24x24 inline SVG info icon, repeated roughly seven times in this cell alone. The result is a wall of inline SVG markup that obscures the prose in any non-rendering view. Move the icon into a small CSS class or a single helper, and reuse it by class name.
- **Technical** (cell 0, "League Code Server" bullet): the line ends with `<!--If there is a link for this let me know -->` — an author-to-author HTML comment leaked into the lesson. Remove or replace with a real link.

## lessons/10_Turtles/10_Welcome/30_Run_Programs.ipynb

- **Technical** (cell 7, "Using the Lesson Browser"): the lesson refers to "the Lesson Browser" in the bottom-left as the recommended way to run `.py` files, but the rest of the course uses plain `python file.py`-style runs. Confirm the Lesson Browser actually exists in the student's environment, or move it below the play-button instructions.
- **Technical** (cell 8, warning): "if the program's code ends with `turtle.exitonclick()`, simply click anywhere inside the window to close it" — `exitonclick()` closes the *turtle* window, not the program; the Python process exits as a result. Reword as "click the turtle window to close it".

## lessons/10_Turtles/20_Introducing_Tina/10_Meet_Tina/Meet_Tina.py

- **Technical** (line 49, `def draw_leg(t, a, r=170, w=40, l=50)`): single-letter parameter `l` is one of the PEP 8-discouraged names (looks like `1` or `I`); also conflicts with `length`. Rename `l` to `length` and `a` to `angle` (and `r`/`w` similarly).
- **Technical** (line 91, `for lp in (30, -30, -150, 150):`): uses tuple iteration before lists, tuples, or iteration have been introduced. Either swap to a literal list or unroll the four `draw_leg` calls.
- **Technical** (line 94, `draw_leg(tina, -90, r=170, w=10, l=50)`): keyword arguments appear here for the first time in the course, with no introduction. The `r=170` is also the default, so it's redundant; pass `w=10` only.
- **Technical** (lines 89–96, call order): `draw_head(tina)`, then legs, then `draw_body(tina)`. The orphan `tina.begin_fill()`, `tina.penup()`, `tina.goto(-100, 175)`, `tina.pendown()` block on lines 23–26 doesn't do anything useful. Remove it.

## lessons/10_Turtles/20_Introducing_Tina/20_What_Can_Tina_Do.ipynb

- **Technical** (cell 1, embedded iframe): `<iframe src="https://docs.python.org/3/library/turtle.html" …>` — the Python docs send `X-Frame-Options: deny`, so this iframe will not render in most browsers. Replace with a plain link.

## lessons/10_Turtles/20_Introducing_Tina/30_Squares_and_Circles/Squares_and_Circles.py

- **Technical** (line 57, `tina.color('red')`): the rest of the file uses `pencolor()` and `fillcolor()` separately. `color()` sets both, which is fine here, but it's the only line in the file using the combined form. Mention in a comment that `color()` sets pen and fill at once, or split it for consistency.

## lessons/10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb

- **Technical** (cell 1, large stylized "Sync Changes" span): the inline-styled span renders as an oversized button-like graphic but it's pure HTML — students may try to click it. Replace with a screenshot or smaller styled span.
- **Technical** (cell 4, empty markdown cell): cell 4 is an empty markdown cell. Remove it.

## lessons/10_Turtles/30_Turtle_Tricks/10_Turtle_Tricks.py

- **Technical** (line 6, `tina.forward()` and `tina.left()`): the docstring lists these but the student has only seen `tina.right()` so far. Add a one-line note that `left` works the same as `right`, just the other direction.

## lessons/10_Turtles/40_Loops/10_Loops.ipynb

- **Technical** (cell 2, code comment): "Loop will run 4 times from 0 to 3" is stated again two lines down ("range(4) generates numbers 0, 1, 2, 3"). Pick one.
- **Technical** (cell 5): inconsistent indentation/spacing between `tina.goto(150, 0)` and the comment compared to surrounding lines. Tidy up.
- **Technical** (cell 8): comments mention coordinates without explaining what they mean. Add a one-line note that (0,0) is the center.
- **Technical** (cell 9, "Star repeats … 36 times"): the figure isn't a star — `range(36)` with `left(170)` produces a 36-pointed rosette, not the "star" most kids picture. Either say "star pattern" consistently or pick angles that produce a recognizable 5-point star.

## lessons/10_Turtles/40_Loops/20_Loop_with_Turtle.py

- **Technical** (line 23, comment): "Repeat forward + left three more times to finish the square." — same false-imperative issue as in Squares_and_Circles.py: the next eight lines already do this. Reword to describe what's already there, since the student is supposed to *replace* the repetition with a loop.

## lessons/10_Turtles/40_Loops/30_Loop_with_Turtle.py

- **Technical** (lines 12–13, docstring): same `uid:` / `name:` metadata leaking into the docstring as in `20_Loop_with_Turtle.py`.

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Technical** (cell 15, exercise): the lines `height_difference = `, `area = `, `doubled = ` are intentional stubs, but the surrounding text never shows the student a worked example. Add a short worked-example block right above the exercise.

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Technical** (cell 17, exercise): comment "use a loop to print numbers from start_number down to 1" implies counting down — `range(start_number, 0, -1)` requires the three-argument form, which has only been used as `range(n)` and `range(a, b)`. Mention the step argument or change the exercise to count up.

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Technical** (cell 7): the `for i in range(-200, 200):` loop runs 400 turtle moves with no `screen.exitonclick()` or `turtle.done()` at the end. The window will close as soon as the loop finishes. Add a closing call.
- **Technical** (cell 9): explanation of `done` vs `exitonclick` is correct, but earlier examples in the module used `exitonclick()` without explaining the difference. Add a callback to the earlier lessons.

## lessons/10_Turtles/70_Projects/10_LeagueBot.py

- **Technical** (line 6, instructions): "Change the turtle image to `'leaguebot_bot.gif'`" — the file in `images/` is named `leaguebot_bolt.gif` (with an "L"). The student's program will fail. Fix to `leaguebot_bolt.gif` (or rename the asset).

## lessons/10_Turtles/80_Introducing_Lists/10_Lists.ipynb

- **Technical** (cell 1): the cell ends with the bare expression `things_to_buy` to display the list. Notebook-only behavior; won't work in a `.py` file. Add a brief note or change to `print(things_to_buy)`.
- **Technical** (cell 3): same bare-expression display (`things_to_buy[1]`). Same fix.
- **Technical** (cell 12): the example uses `[90, 90, 90, 90]` — four identical 90s. The point of using a list of angles is to vary them. Use `[60, 120, 60, 120]` or something visibly varied.

## lessons/10_Turtles/90_Graphics_Projects/10_Flaming_Ninja_Star.py

- **Technical** (line 17, `"#%06X" % (random.randint(0, 0xFFFFFF))`): printf-style `%` formatting and hex literals appear here for the first time without explanation. A one-line comment ("returns a random hex color string like `#A1B2C3`") would help.
- **Technical** (line 23, `colors[i % len(colors)]`): `get_next_color` is defined but never called. Remove the unused function.
- **Technical** (lines 20–24, ordering): the global `colors` list and `get_next_color` are defined between `get_random_color` and the rest of the setup, splitting the function definitions. Move them together.

## lessons/10_Turtles/90_Graphics_Projects/20_Crazy_Spiral.py

- **Technical** (line 31): `t.right(360/num_shapes)` is fine if `num_shapes` is an int, but if it's a list (per the suggestion in the comment), it's a TypeError. Drop the "list of numbers" suggestion.

## lessons/10_Turtles/90_Graphics_Projects/30_Pentagon_Crazy.py

- **Technical** (line 16): `get_random_color` defined but never called. Remove.
- **Technical** (line 33): the loop uses `i == 100` and `i == 200` as triggers to change pen width. Magic numbers should be named.

## lessons/10_Turtles/Module_One_Quiz.ipynb

- **Technical** (cell 1, code): `display_quiz("../../lessons/.jtl/Quiz_Data/Module_One_Quiz.json")` — the relative path goes up two directories from `lessons/10_Turtles/`, which is wrong by one. Correct path is `../.jtl/Quiz_Data/Module_One_Quiz.json`.
- **Technical** (cell 2): empty code cell. Remove.

---

# Module 20 — Types and Logic

## lessons/20_Types_and_Logic/10_Operators_and_Types.ipynb

- **Technical** (cell 11, operator table): the `**` row uses `$2$ ** $3$` with `**` outside math mode while every other operator is wrapped in `$...$`. Make consistent.
- **Technical** (cell 18, final two prints): the "Verification" line prints `(2 * 4) + 3 = 11` and the next prints `Result: 11`. Two separate labels for the same verification is confusing — collapse into one.
- **Technical** (cell 20, `for` loop): first appearance of `for i in range(10)` with a bound variable used inside the body. Module 10 only used `for _ in range(N)`. Add a one-line note that `i` takes on each value `0..9`.

## lessons/20_Types_and_Logic/20_String_Operations.ipynb

- **Technical** (cell 0, note at end): "Strings are immutable, meaning once they are created, they cannot be changed, or used in mathematical operations without conversion." The "or used in mathematical operations" clause has nothing to do with immutability. Split into two sentences.
- **Technical** (cell 8): `s.replace('World', 'Python')` uses single quotes but the rest of the lesson uses double quotes. Pick one.
- **Technical** (cell 16, exercise stub): `greet = ... #` ends with a trailing `#` and an empty comment. Drop or add the actual hint.

## lessons/20_Types_and_Logic/30_Control_Flow.ipynb

- **Technical** (cell 10, lunch-time check): `if time > "11:30" and time < "12:30"` does lexicographic string comparison, not numeric. Works for "11:31" by accident but breaks for `"9:30"` vs `"11:00"` (since `"9" > "1"` lexicographically). Switch to integers (`hour, minute = 11, 31`) or call out that this only works because all the strings are zero-padded `HH:MM`.
- **Technical** (cell 18, `if maybe_its_true == True`): comparing booleans to `True`/`False` with `==` is a PEP 8 anti-pattern (E712). Teach the idiomatic form: `if maybe_its_true:`.
- **Technical** (cell 20, `else` comment): the comment reads `# do this if maybe_this == False and maybe_that == False` but `else` runs when neither preceding condition matched, not when the variables themselves are `False`. Rewrite as `# do this if neither of the conditions above was true`.
- **Technical** (cell 25, comparison threshold): `if ml <= teaspoon_ml` fires on any `ml <= 4.92892`, including `0` and negatives. Add a guard `if ml < 0: ...` or note the assumption that `ml > 0`.

## lessons/20_Types_and_Logic/40_Working_With_Numbers.ipynb

- **Technical** (cell 0, hex example): the literal is written `0x2f3` (lowercase `f`) but the place-value table writes `F (15)`. Pick a single case.
- **Technical** (cell 0, decimal place-value example): "decimal number $255$ can be broken down by its place values into $(2 \times 100) + (5 \times 10) + (5 \times 1)$" — spell out positions explicitly: "$255 = (2 \times 10^2) + (5 \times 10^1) + (5 \times 10^0)$".
- **Technical** (cell 5, scientific notation claim): note that `1e6` is a `float` in Python, not an `int` (`type(1e6)` returns `float`). This trips up students who type `1e6` expecting an integer.

## lessons/20_Types_and_Logic/50_My_Ages.py

- **Technical** (line 21, docstring snippet): docstring shows `simpledialog.askinteger(...)` example but the surrounding scaffold leaves `# Ask the user's age` as a stub. Make clear the docstring is a template: "Use this pattern to ask for the user's age:".
- **Technical** (line 47, TODO comment): `# TODO:` reads like leftover engineering scaffolding. Replace with `# Stretch goal:` or `# Bonus:`.

## lessons/20_Types_and_Logic/60_Simple_Adder.py

- **Technical** (line 20): the student needs to know `simpledialog.askinteger` returns an `int` (or `None` if cancelled), and `messagebox.showinfo` needs a string. Add a one-line hint about converting the sum to a string.

## lessons/20_Types_and_Logic/70_Infuriating_Calculator.py

- **Technical** (lines 30–32): division by an integer that doesn't divide evenly will surprise students unless they pick `askfloat()`. Recommend `askfloat()` for both numbers, or note that `int / int` returns a `float` in Python 3.

## lessons/20_Types_and_Logic/80_Code_Challenges.ipynb

- **Technical** (cell 1, challenge wording): "If $n$ is even and in the range 2 to 5 (inclusive), print `not weird`" — only `2` and `4` are even in `2..5`. Reword for clarity.

## lessons/20_Types_and_Logic/lib/03_badgers_tk.py

- **Technical** (line 31): `return 'mushroom' # Always show a snake` — comment says "snake" but code returns `'mushroom'`. Fix the comment.

## lessons/20_Types_and_Logic/lib/badgers.py

- **Technical** (line 18, bare `except`): catches `BaseException`, including `KeyboardInterrupt`. Use `except (ValueError, TypeError):` or at minimum `except Exception:`.
- **Technical** (line 7): docstring for `FizzBuzzer` is preceded by a blank line, so it's not picked up as the class docstring. Move it directly under `class FizzBuzzer:`.
- **Technical** (lines 14–19): `isnumber` is defined inside `update_display` and re-defined every call. Pull it out to module level.

---

# Module 30 — Loops

## lessons/30_Loops/10_Iteration.ipynb

- **Technical** (cell 0): typo "expads" → "expands."
- **Technical** (cell 1, comment): "This loop repeats 10 times" is fine, but cell 12 says "This loop repeats 12 times, printing each character in the string 'Hello World!'". "12 times" is over-specific and brittle.
- **Technical** (cell 5, code): `print( list("This is a string"))` has stray space after the opening paren — clean for PEP 8.
- **Technical** (cell 14, table): duplicate "Numbers" rows (one for `numbers` list, one for `range(10)`). Merge or relabel.

## lessons/30_Loops/20_Loops_with_Range.ipynb

- **Technical** (cell 5): the cell evaluates `list(range(101, 120, 2))` as a bare expression. Wrap in `print(...)` for consistency with the other "Run Me!" cells.
- **Technical** (cell 9, table): "🐍 snake!" has an exclamation point inconsistent with surrounding cells; drop the `!`.

## lessons/30_Loops/30_Looping_Through_Lists.ipynb

- **Technical** (cell 0e2837fd): uses bare `backpack` as the last expression to "display" — works in Jupyter but inconsistent with the explicit `print()` style. Use `print(backpack)`.
- **Technical** (cell b2a608ff): `# type: ignore[name-defined]` comments are noise to a beginner reader; hide or move explanation to a single comment block.
- **Technical** (cell 17a599ca): the cell only has a `# Try adding...` comment with no `my_list` declaration — students may run in isolation and get `NameError`. Re-declare `my_list` in the stub.

## lessons/30_Loops/40_Crazy_Tina.py

- **Technical** (line 22): `tina.speed(2)` with comment "Move at a moderate speed, not too fast" — speed 2 is quite slow. Use `tina.speed(6)` or change the comment.

## lessons/30_Loops/50_Tuples.ipynb

- **Technical** (cell 6): the code is intentionally a `TypeError` demonstration. Wrap with `try/except` to avoid stopping notebook execution, or note explicitly that the cell will error.

## lessons/30_Loops/60_Indexing_and_Slicing.ipynb

- **Technical** (cell 3, ASCII diagram): index labels under the boxes are misaligned visually. Verify alignment.
- **Technical** (cell 7): wording "to 8th... not including the 9th" is confusing — say "from the 3rd through the 8th item (stops before the 9th)."

## lessons/30_Loops/80_Strings.ipynb

- **Technical** (cell 1, code): `triple = """“Hope” is the thing with feathers...` uses curly Unicode quotes. Add a note that those are decorative inside the string, not Python syntax.
- **Technical** (cell 13): the alignment example produces left-aligned text by default. Clarify that the default alignment is left for strings and right for numbers.
- **Technical** (cell 17, challenge spec): be explicit that "The loop number, taking up 3 spaces" means right-aligned width using `{n:3}` and `{n:5}`.

## lessons/30_Loops/90_Fizz_Buzz_Badgers.py

- **Technical** (lines 25–32): the docstring rules list "evenly divisible by 15" third while the code correctly checks `% 15` first. Reorder the docstring rules to match the code (15, 5, 3).

## lessons/30_Loops/110_FizzBuzz_Gui_Grid.py

- **Technical** (line 34): `%` and `//` were introduced in module 20, but a brief reminder of `n % 10` (last digit) and `n // 10` (drop last digit) would help.
- **Technical** (line 40): `Box` is imported but never used. Remove from import.

## lessons/30_Loops/120_More_Iterables.ipynb

- **Technical** (cell 31, `repeat([], 5)`): produces five references to *the same* empty list — a classic gotcha. Add a warning or change the example.

## lessons/30_Loops/130_Iterable_Turtle.py

- **Technical** (line 19): variable name `something` is a placeholder. Add a comment hint like `# Replace 'something' with a tuple unpacking like (color, (angle, distance))`.

## lessons/30_Loops/140_More_Loops.ipynb

- **Technical** (cell 11): `else` clause attached to `while True:` is unreachable — worth a comment: `# Note: this else is unreachable because while True never becomes False.`

## lessons/30_Loops/150_Number_Guess.py

- **Technical** (line 19): the spec says "If the user's guess is divisible by 7, tell the user 'that is a very bad number, starting over' and pick another number" — but lines 4–6 say to pick another *random* number when *the random number itself* is divisible by 7. Reconcile: which is divisible by 7 — the guess, or the secret number?

## lessons/30_Loops/160_Extras.ipynb

- **Technical** (cell 2): `'fizz'*(i % 3 == 0) + 'buzz'*(i % 5 == 0) or str(i)` relies on the truthiness of the empty string. Add a brief comment explaining the trick.

---

# Module 40 — Data Structures and Functions

## lessons/40_Data_Structures_Func/10_Functions.ipynb

- **Technical** (cell 7): `greet_user(name = "Bob", greeting)` — `SyntaxError` is raised at parse time, so in Jupyter the *whole cell* fails before any prior context loads. Move the function definition into cell 7 itself.
- **Technical** (cell 17): redefines `greet_user` from cell 14, then cell 32 in Closures redefines it again. Use distinct names (`greet_user_broken`, `greet_user_global`) to keep the namespace clean.
- **Technical** (cell 30, exercise stub): comment block says "c) 2 + 2 != 3 + 3 = 6" — the `= 6` at the end is a leftover from line (b). Delete `= 6`.
- **Technical** (cell 33): says "This is called **accessing a global variable**" — accurate, but the prior heading still says "Closures." Pick one term.

## lessons/40_Data_Structures_Func/20_Exceptions.ipynb

- **Technical** (cell 17): both `try` blocks contain only `pass  # do something`, so no exception will ever be raised. Replace with a real triggering call (e.g. `int("not a number")`).
- **Technical** (cell 18): "use it to catch ones you are not aware of" — confusing. Suggested: "save the bare `except Exception` for cases where you genuinely don't know what could go wrong."
- **Technical** (cell 20, exercise stub): the TODO list never spells out where IndexError handling fits. Add `# TODO: handle IndexError when n is too large`.

## lessons/40_Data_Structures_Func/30_Dicts_Sets.ipynb

- **Technical** (cell 14): duplicate-key dict literal raises a SyntaxWarning in Python 3.12+. Mention or rewrite using sequential assignments.
- **Technical** (cell 22): `del my_dict['c']` shown without first showing dict's `.pop()`. Add `.pop()` alongside.
- **Technical** (cell 30, exercise): "return `'Funny'` and a list of the funny words found" — explicitly say "return a tuple of `('Funny', [list of words])`".

## lessons/40_Data_Structures_Func/40_Funny_Words_Db.py

- **Technical** (lines 124–127): wraps definitions in literal emoji `"😂 "` and `" 🤡"`. CLAUDE.md says "Do not use emojis as substitutes for words" — these are decorative but baked into student-facing output. Consider `"[funny] "` or making decoration optional.
- **Technical** (line 169): `app.when_key_pressed = handle_enter` — accesses `event.tk_event.keysym`, which varies by guizero version. Use the documented `event.key` instead.
- **Technical** (line 65, `is_funny` stub): until the student implements `is_funny`, the emoji-wrapping branch is dead code. Add a comment near the stub: "Until you implement this, definitions will never be marked funny."
- **Technical** (line 105, `update_listbox` stub): the stub returns a non-empty placeholder list. The instruction "(For your function, you should set this list to the empty list)" is buried mid-comment. Make it more prominent.
- **Technical** (line 142, GUI sizing): `width="10"` and `width="25"` passed as strings to guizero TextBoxes. Use integers.

## lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb

- **Technical** (cell 6, `pretty_print_2d`): helper defined inside a "Run Me!" cell, then re-referenced throughout. If a student runs cells out of order, later calls fail. Move the helper to its own setup cell.
- **Technical** (cell 31, `transpose`): defines `transpose()` but cell 6 already showed `list(zip(*board))` doing the same thing. Reuse or factor out.

## lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py

- **Technical** (lines 53, 56, 75): mixes `.value` and `.text` on a guizero Text widget. guizero `Text` uses `.value` only. Standardize.
- **Technical** (line 102): `ttt = TicTacToe(check_win)` runs at import time, opening a window. Wrap in `if __name__ == "__main__":`.

---

# Module 50 — Projects

## lessons/50_Projects/10_Hotel_Management.md

- **Technical** (Requirements): capitalization is inconsistent ("While Loop", "Multiple Night Check in"). Standardize on lowercase prose.
- **Technical** (Requirements): the rule "The functions should, mostly, return something" with the `my_age = add(10, 5)` example repeats Module 40 material. Trim to one sentence.

## lessons/50_Projects/20_Random_Walk.py

- **Technical** (function docstring): student is told to make the turtle move "a fixed number of steps" but no `STEP_SIZE` constant. Add `# step_size = 10  # tweak to taste`.
- **Technical** (hint block): "Read one of the past turtle programs to see how to use these methods." — be specific. Point to e.g. `lessons/10_Turtles/90_Graphics_Projects/40_Turtle_Spiral.py`.

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Technical** (boilerplate code cell): dict only contains the letters in "ASCII ART IS COOL" plus space. A student calling `print_ascii("HELLO")` sees nothing for `H`, `E`, `L`, `O`. Either include the full alphabet or add a comment.
- **Technical** (Exclusions, "No Hardcoding"): conflicts with the boilerplate, which hardcodes every character row. Reword.

## lessons/50_Projects/Temp_Project_Ideas/Spin_The_Wheel.ipynb

- **Technical** (Assignment Requirements): "Display the total prizes won at the end of the game" but earlier "Keep track of the prizes won by each player" (multiplayer). Pick one.

---

# Cross-module sequencing

- **Technical**: Filename casing inconsistent across modules. Module 10 uses `Tash_Me_Click`, `Tash_Me_Twirl`, `LeagueBot`. Module 30 uses `Iterable_Turtle`, `List_Story`, `Fizz_Buzz_Badgers`. PEP 8 prefers `snake_case` for filenames — pick e.g. `20_tash_me.py`, `10_league_bot.py`.