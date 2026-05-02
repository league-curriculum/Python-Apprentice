# Python Apprentice — Review Highlights

Distilled from the full review in `Python-Apprentice-Review.md`. Items are grouped by what they cost you if left alone.

## Bugs that will actually break student work

- **`lessons/10_Turtles/70_Projects/10_LeagueBot.py`** — instructions tell students to load `'leaguebot_bot.gif'`; the asset is named `leaguebot_bolt.gif`. The student's program will fail immediately.
- **`lessons/10_Turtles/Module_One_Quiz.ipynb`** (cell 1) — `display_quiz("../../lessons/.jtl/Quiz_Data/Module_One_Quiz.json")` is wrong by one directory level. From `lessons/10_Turtles/` the correct path is `../.jtl/Quiz_Data/Module_One_Quiz.json`.
- **`lessons/20_Types_and_Logic/lib/03_badgers_tk.py`** (line 31) — `return 'mushroom' # Always show a snake`. Comment says snake, code returns mushroom.
- **`lessons/30_Loops/40_Crazy_Tina.py`** — docstring says "Review the 'Using Lists' section of the previous lesson," but no section by that name exists in `30_Looping_Through_Lists.ipynb`.
- **`lessons/30_Loops/150_Number_Guess.py`** — spec contradicts itself: lines 4–6 say to reroll when the *secret number* is divisible by 7, line 19 says to reroll when the *user's guess* is divisible by 7. Pick one.
- **`lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py`** — defines `X_MARK = "X"` (uppercase) and `O_MARK = "O"`, but the preceding `50_Splat_Comprehension.ipynb` trained students on lowercase `'x'`/`'o'`. Code copied from the notebook will silently fail to detect wins.

## Real sequencing holes

- **`input()` is never taught before Module 50 demands it.** Module 20 uses `tkinter.simpledialog`/`messagebox`. Module 30's `150_Number_Guess.py` uses a custom `ask_integer` helper. By `50_Projects/10_Hotel_Management.md` the student is told to use `print()` and `input()`, but `input()` has zero prior exposure.
- **`guizero` is used in three projects without a primer.** `30_Loops/110_FizzBuzz_Gui_Grid.py`, `40_Data_Structures_Func/40_Funny_Words_Db.py`, and `40_Data_Structures_Func/60_Tic_Tac_Toe.py` all assume guizero. The first one says "Don't worry about how it works — copy the examples," which works for one project, not three.
- **`random` shows up in `10_Turtles/90_Graphics_Projects/` before Module 20 introduces it.** `random.randint` and `"#%06X" % ...` string formatting both appear with no explanation.
- **Module 40's "Functions" lesson misrepresents what came before.** `40_Data_Structures_Func/10_Functions.ipynb` opens with "We've seen functions a few times, but haven't explained how they work in detail." Module 10's `50_Variables_and_Functions/20_Functions.ipynb` already covered `def`, parameters, return values, and looped calls. Reframe Module 40's intro around what's actually new (keyword vs. positional args, defaults, scope, `pass`).

## The biggest scope question to resolve

- **List comprehensions are inconsistent across the curriculum.**
  - `CLAUDE.md` lists comprehensions as out of scope.
  - `lessons/30_Loops/README.md`'s PCEP alignment block lists "List Comprehensions" as covered.
  - `lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb` teaches them as a primary topic with required exercises.
  - `lessons/40_Data_Structures_Func/60_Tic_Tac_Toe.py` depends on student-written comprehensions.

  Pick a position and align all four. Either remove comprehension teaching (rewrite Splat_Comprehension and Tic Tac Toe with explicit `for` loops) or update CLAUDE.md to match.

## Recurring voice and convention patterns

- **`# Run Me!` labels on cells that are deliberately supposed to crash.** `40_Data_Structures_Func/10_Functions.ipynb` cells 7/9/11 and `20_Exceptions.ipynb` cells 8/10/12/14 do this. Students will think their environment is broken. Relabel as `# This will fail` or `# This will raise an exception`.
- **The `auto_turtle` notebook macro is never introduced.** `%run .lib/auto_turtle.py` and `tina = turtle(myTS)` appear in `10_Turtles/40_Loops/10_Loops.ipynb`, `50_Variables_and_Functions/10_Variables.ipynb`, and `50_Variables_and_Functions/20_Functions.ipynb`, conflicting with the `import turtle; tina = turtle.Turtle()` pattern used in every `.py` exercise. Either explain it once on first use, or replace it with the standard `import turtle` pattern.
