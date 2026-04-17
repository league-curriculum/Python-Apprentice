# Review: remainder of 10_Turtles

Delete any bullet you don't want applied, then hand the file back and I'll apply the rest.

---

## lessons/10_Turtles/30_Turtle_Tricks/10_Turtle_Tricks.py

- **Technical** (line 14): `turtle.setup(600,600,0,0)` — add spaces after commas:
  `turtle.setup(600, 600, 0, 0)`.

---

## lessons/10_Turtles/30_Turtle_Tricks/20_Turtle_Tricks.py

- **Technical** (line 14): `turtle.setup(600,600,0,0)` — add spaces after commas.

---

## lessons/10_Turtles/30_Turtle_Tricks/30_Turtle_Tricks.py

- **Technical** (line 16): `turtle.setup(600,600,0,0)` — add spaces after commas.
- **Voice** (line 9, docstring bullet): "Challenge yourself to experiment with different colors and positions!" —
  drop exclamation: "Try different colors and positions."
- **Voice** (line 26): `# Dont forget to check in your code!` — fix "Dont" → "Don't", drop exclamation, or
  rewrite as `# Save your progress by checking in your code.`

---

## lessons/10_Turtles/40_Loops/10_Loops.ipynb

- **Voice** (cell 0, opening): "Welcome to the world of loops!" plus the rest of the paragraph oversells.
  Rewrite the whole opening as: "Loops let you run the same code many times without repeating yourself. In this
  lesson you'll see how `for` loops work and how they make turtle programs shorter and easier to change."
- **Voice** (cell 0, Tip): "mastering them will greatly enhance your coding skills" — drop the tip or soften to
  "Loops show up in every programming language, so it's worth taking time to get comfortable with them."
- **Voice** (cell 1, paragraph 1): "A loop will let you tell Tina to do something multiple times by using a simple
  command!" — drop exclamation.
- **Voice** (cell 1, bullet intro): "Loops are super useful because they help us:" — drop "super".
- **Voice** (cell 6): "That's a lot of repetitive code!" — drop exclamation.
- **Voice** (cell 6): "Maybe we can even add more shapes without making the code super long!" — drop "super" and
  the exclamation: "We can even add more shapes without making the code much longer."
- **Voice** (cell 9, paragraph 1): "Using loops can make your code much cleaner and easier to understand!" — drop
  exclamation.
- **Voice** (cell 9, Tip): "Take your time to practice and experiment with them—understanding loops will help you
  solve problems more efficiently and write better code!" — drop the tip; the same point is made in cell 0.
- **Voice** (cell 10): "Try running these examples to see how loops can be used in different ways!" — drop
  exclamation.
- **Voice** (cell 12, Note): "Try changing the value of size to see how the output changes!" — drop exclamation.
- **Voice** (cell 15, Tip): "Nested loops are great for creating patterns like checkerboards." — fine, keep. No
  change needed.
- **Voice** (cell 19, closing line): "open the file `20_Loop_with_Turtle.py`, and try running it!" — drop the
  exclamation.
- **Technical** (cell 8, code): `tina.speed('fastest')` has extra whitespace before the aligned comment. Tighten.

---

## lessons/10_Turtles/40_Loops/20_Loop_with_Turtle.py

- **Technical** (line 16): `turtle.setup(600,600,0,0)` — add spaces after commas.
- **Technical** (line 21): `tina.speed(2)  # Make the turtle move as fast, but not too fast. ` — the comment is
  awkwardly worded and has a trailing space. Rewrite: `# Move at a moderate speed, not too fast.`
- **Technical** (line 26): `tina.forward(150)  # Continue the last two steps three more times` — same bug as
  Squares_and_Circles.py: comment sits in the second iteration, so "three more times" is wrong. Move the
  explanatory comment above the whole block or rewrite as `# Repeat forward + left three more times to finish
  the square.`

---

## lessons/10_Turtles/40_Loops/30_Loop_with_Turtle.py

- No findings.

---

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Voice** (cell 4, closing line): "Try changing sides to different numbers and watch how angle changes! 🎯" —
  drop the exclamation and the 🎯 emoji.
- **Voice** (cell 5, opening): "You may not have noticed, but you have been working with variables all along!" —
  drop the exclamation.
- **Voice** (cell 7, paragraph 1): "This shows the power of variables—they let you write code that adapts
  automatically!" — drop the exclamation.
- **Voice** (cell 7, closing): "This makes your code flexible and easy to experiment with!" — drop the exclamation.
- **Voice** (cell 9, final comment): "Try changing the numbers, text, or boolean values and see what happens!" —
  drop the exclamation.
- **Voice** (cell 11, final comment): "Try changing the number of pizzas, slices_per_pizza, or people, and see
  what happens!" — drop the exclamation.
- **Technical** (cell 15, exercises): each blank line like `height_difference = ` is a SyntaxError if run. Put
  `...` or `0  # TODO` after each bare `=` so the cell at least parses before students fill it in. Example:
  `height_difference = ...  # Complete this calculation using variables`.
- **Scope** (cell 8): lists dictionaries, sets, and NoneType. PCEP covers dicts and sets at a basic level, so fine
  as a name-drop. No change needed — noting only because the rubric asks to flag scope.

---

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Voice** (cell 0, closing line): "By the end, you'll be able to write your own reusable code blocks to perform
  calculations, make decisions, and more!" — drop the exclamation.
- **Voice** (cell 3, final comment): "Try changing the parameters to see how the angle changes or create new
  shapes!" — drop the exclamation.
- **Voice** (cell 11, final comment): "Try changing the numbers to see different results!" — drop the exclamation.
- **Voice** (cell 13, `pizza_calculator`): `# Return both values at once!` — drop the exclamation.
- **Voice** (cell 13, final comment): "Try changing the inputs to see different results!" — drop the exclamation.
- **Voice** (cell 14, opening): "Now let's put our function knowledge to work with Tina!" — drop the exclamation.
- **Voice** (cell 15, closing): "See how functions make our code cleaner and easier to reuse? Try calling the
  functions with different parameters!" — drop the exclamation.
- **Voice** (cell 16, opening): "Now it's your turn!" — drop the line; the "Function Challenges" heading already
  signals this.
- **Flow** (cell 13): `print(f"For 10 people: need {slices} slices and {pizzas} pizzas")` uses an f-string, which
  hasn't been introduced. Swap for comma-separated `print`: `print("For 10 people: need", slices, "slices and",
  pizzas, "pizzas")`.

- **Technical** (cell 13, `pizza_calculator`): `pizzas_needed = -(-total_slices_needed // 8)` is a cryptic ceiling-
  division trick. Replace with `from math import ceil` at the top and `pizzas_needed = ceil(total_slices_needed /
  8)`, which is readable.

---

## lessons/10_Turtles/50_Variables_and_Functions/30_Efficient_Turtle.py

- **Technical** (line 12): `turtle.setup(600,600,0,0)` — add spaces after commas.
- **Technical** (line 17): `tina.speed(2)  # Make the turtle move as fast, but not too fast.` — same awkward
  wording. Rewrite as `# Move at a moderate speed, not too fast.`

---

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Voice** (cell 0, heading): "Turtle Tricks and Tips" — the folder and file name are "More_Turtle_Programs";
  either rename the heading to match ("More Turtle Programs") or accept the mismatch. I'd align the heading.
- **Technical** (cell 0): `https://docs.python.org/3.14/library/turtle.html` — Python 3.14 docs may not exist yet
  and the iframe below points to `/3/`. Change the link to `/3/library/turtle.html` to match.
- **Technical** (cell 2, example code): the demo loop `for i in range(4): t.goto(200, 200); t.goto(-200, -200)`
  just bounces the turtle back and forth across a diagonal, which doesn't show off a custom-image turtle doing
  anything interesting. Consider changing to a square pattern (goto each of 4 corners in sequence) so the demo
  matches what the follow-up `.py` asks the student to write.
- **Technical** (cells 7, 9, 11): `import turtle as turtle` is a redundant alias. Change to plain `import turtle`.
- **Voice** (cell 13, Tip): "If you haven't checked in your code now would be a great time to do so!" — drop the
  exclamation: "If you haven't checked in your code, now's a good time."

---

## lessons/10_Turtles/60_More_Turtle_Programs/20_More_Turtle_programs.py

- **Technical** (filename): lowercased `programs` is inconsistent with every other file and the folder
  (`More_Turtle_Programs`). Rename the file to `20_More_Turtle_Programs.py`.
- **Technical** (line 2, docstring): references `10_More_Turtle_programs.ipynb` (lowercase p) but the actual file
  is `10_More_Turtle_Programs.ipynb`. Fix the casing.

---

## lessons/10_Turtles/60_More_Turtle_Programs/30_More_Turtle_Programs.py

- **Technical** (line 2, docstring): references `10_More_Turtle_programs.ipynb` (lowercase p) — fix casing.
- **Flow** (docstring lines 5–6): the instructions tell the student to "move to the corners of the screen in a
  square pattern", but this lesson is for the **background image** section, not the turtle-image section.
  "Moves to the corners in a square pattern" is leftover copy-paste from `20_`. Rewrite to describe what the
  background-image exercise actually asks for — e.g., "Set the background image, then draw a shape on top of it
  with your turtle."

---

## lessons/10_Turtles/60_More_Turtle_Programs/40_More_Turtle_Programs.py

- **Technical** (line 2, docstring): references `10_More_Turtle_programs.ipynb` (lowercase p) — fix casing.

---

## lessons/10_Turtles/70_Projects/10_LeagueBot.py

- No findings.

---

## lessons/10_Turtles/70_Projects/20_Tash_Me.py

- **Technical** (line 9, Hint): the hint is cut off mid-sentence: "See the `10_More_Turtle_Programs` section
  labeled 'Change the Background Image' and" — the sentence ends on "and". Drop the trailing "and" or finish the
  thought.
- **Technical** (line 9, Hint): the notebook section is actually titled "Set a Background Picture", not "Change
  the Background Image". Update the reference.

---

## lessons/10_Turtles/70_Projects/30_Tash_Me_Click.py

- No findings.

---

## lessons/10_Turtles/70_Projects/40_Tash_Me_Twirl.py

- **Technical** (line 6, Hint): references "section 'Respond to Screen Clicks'", but this exercise is about
  clicking the *turtle*, not the screen. Change the reference to "Clicking The Turtle Directly".

---

## lessons/10_Turtles/80_Introducting_Lists/10_Lists.ipynb

- **Technical** (folder name): `80_Introducting_Lists` is misspelled — should be `80_Introducing_Lists`. Flagging
  separately since renaming a folder is a bigger change than an in-file edit; let me know if you want this.
- **Technical** (cell 13, heading): "Excercises (Optional)" — typo, should be "Exercises (Optional)".
- **Scope** (cell 8): mentions "comprehensions" as something lists can do. PCEP scope says comprehensions are out,
  and we're mentioning them only as a "you can also do this" aside, which is fine, but for consistency consider
  dropping "comprehensions" from the list so students don't try to look them up mid-lesson.
- **Technical** (cell 12, code): `for left in [90, 90, 90, 90]:` shadows the outer `left = 90` variable (OK here,
  but noting it since the lesson is new to most students). Consider renaming the loop variable to `angle`.

---

## lessons/10_Turtles/80_Introducting_Lists/20_Color_Lines.py

- **Technical** (line 8): `turtle.setup(600,600,0,0)` — add spaces after commas.
- **Technical** (line 13): trailing whitespace after `too fast.` — remove.
- **Technical** (line 13): "Make the turtle move as fast, but not too fast." — same awkward "as fast" wording.
  Rewrite as `# Move at a moderate speed, not too fast.`

---

## lessons/10_Turtles/90_Graphics_Projects/10_Flaming_Ninja_Star.py

- **Technical** (naming): `getRandomColor`, `getNextColor`, `baseSize`, `flameSize` are camelCase. PEP 8: use
  snake_case for functions and variables. Rename to `get_random_color`, `get_next_color`, `base_size`,
  `flame_size` (and update call sites).
- **Technical** (line 26): `turtle.setup(600,600,0,0)` — add spaces after commas.
- **Technical** (line 32): `t = turtle.Turtle()` has a trailing space — remove.
- **Technical** (lines 40–61): each statement inside the `for` loop is separated by a blank line, which is
  unusual. Tighten by removing the blank lines between related calls so the loop body reads as one block.

---

## lessons/10_Turtles/90_Graphics_Projects/20_Crazy_Spiral.py

- **Scope** (line 26, instructions): "or it could use islice(), cycle(), or a list of numbers." — `islice()` and
  `cycle()` are out of scope (from `itertools`). Drop those two: "for example 100, or a list of numbers."

---

## lessons/10_Turtles/90_Graphics_Projects/30_Pentagon_Crazy.py

- **Technical** (naming): `getRandomColor`, `getNextColor`, `myTurtle` are camelCase. Rename to
  `get_random_color`, `get_next_color`, `my_turtle` (PEP 8).
- **Technical** (lines 13–17): `getNextColor` references the global `colors` at call time, but `colors` is
  defined below the function (line 23). It works because Python looks up globals lazily, but it's confusing for a
  student reading top-to-bottom. Move the `colors = (...)` tuple above the function definitions.

---

## lessons/10_Turtles/90_Graphics_Projects/40_Turtle_Spiral.py

- **Technical** (naming): `getRandomColor`, `myTurtle` are camelCase. Rename to `get_random_color`, `my_turtle`
  (PEP 8).
- **Voice** (line 47): `# Check the pattern against the picture in the recipe. If it matches, you are done!` —
  drop the exclamation.
- **Voice** (line 51): `# Now check in your code!` — drop the exclamation.

---

## lessons/10_Turtles/Module_One_Quiz.ipynb

- No findings.

---

## lessons/10_Turtles/README.md

- No findings.
