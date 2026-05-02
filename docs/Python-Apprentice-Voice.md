# Python Apprentice — Voice Review

Split from `Python-Apprentice-Review.md`. This file keeps only the `Voice` findings.

---

# Module 10 — Turtles

## lessons/10_Turtles/10_Welcome/10_Welcome.ipynb

- **Voice** (cell 0, "Course Symbols" alert): "Take a moment to look them over before you continue." plus the closing italic line "It's worth reading through each of these, since the lessons refer back to them." — these say the same thing twice and the second sounds slightly preachy. Drop the centered italic line and keep only the opening sentence.

## lessons/10_Turtles/10_Welcome/20_Open_The_Screen.ipynb

- **Voice** (cell 0, second sentence): "Now, to see your turtle's drawings, you need to open a virtual screen." — fine, but combine with the next sentence ("Most of the time, this screen will open automatically.") which currently reads as a small contradiction. Suggest: "The virtual screen usually opens automatically. If it doesn't, look for the monitor icon …".

## lessons/10_Turtles/10_Welcome/30_Run_Programs.ipynb

- **Voice** (cell 1, code): "Hello 👋 World 🌎! Today is" uses two decorative emojis in a single short string and the lesson hasn't introduced strings yet. Drop the emojis — the date demo doesn't need them.

## lessons/10_Turtles/20_Introducing_Tina/20_What_Can_Tina_Do.ipynb

- **Voice** (cell 0, second paragraph): "Your task will be to read the program, figure out what it does, and make some fun changes." — drop "fun"; "make some changes" is enough.

## lessons/10_Turtles/20_Introducing_Tina/40_Check_In_Your_Code.ipynb

- **Voice** (cell 2, tip): "Stopping your Codespace helps save resources and ensures your work is safely paused. Just remember to save/commit any changes!" — has the only exclamation point in the lesson and isn't earned. Drop the `!`.

## lessons/10_Turtles/40_Loops/10_Loops.ipynb

- **Voice** (cell 1, second paragraph): "Instead of repeating the same instructions over and over again, a loop will let you tell Tina to do something multiple times by using a simple command." — wordy. Trim to "Instead of repeating the same instructions, a loop tells Tina to do something multiple times."
- **Voice** (cell 6, last sentence): "Imagine how confusing it would be if we wanted to move the turtle 36 times to draw a star — that's a lot of repetitive code." — kid-TV-host register. Reword: "Drawing the 36-step star without a loop would mean 72 lines of nearly identical code."
- **Voice** (cell 18, tip): just restates what the cell above explained. Cut it.

## lessons/10_Turtles/50_Variables_and_Functions/10_Variables.ipynb

- **Voice** (cell 8): "You don't need to memorize all these types right now—let's just look at some examples to see how they work!" — only exclamation point in the lesson, attached to filler. Replace with "These examples show how a few of them work."
- **Voice** (cell 1, "In case you got stuck on the previous lesson, here is one way you could have solved it"): implies the previous lesson had an exercise the student attempted. Either rephrase as "if you tried the pentagon exercise…" or move the solution next to the exercise.

## lessons/10_Turtles/50_Variables_and_Functions/20_Functions.ipynb

- **Voice** (cell 0, opening paragraph): "By the end, you'll be able to write your own reusable code blocks to perform calculations, make decisions, and more." — corporate-training register. Reword: "By the end, you'll be writing your own reusable functions."

## lessons/10_Turtles/60_More_Turtle_Programs/10_More_Turtle_Programs.ipynb

- **Voice** (cell 0, opening): "Check out this link, or take a look below!" — exclamation point on a transitional sentence. Drop the `!`.

## lessons/10_Turtles/90_Graphics_Projects/40_Turtle_Spiral.py

- **Voice** (line 47, comment): "Check the pattern against the picture in the recipe. If it matches, you are done." — what "recipe" and "picture"? There's no image referenced in the file or its README. Either link the picture or drop the line.

---

# Module 20 — Types and Logic

## lessons/20_Types_and_Logic/10_Operators_and_Types.ipynb

- **Voice** (cell 1, "When you're ready to begin, run the code block below."): mild kid-TV phrasing; cut to "Run the cell below to create a few variables of different types." or just delete it.

## lessons/20_Types_and_Logic/20_String_Operations.ipynb

- **Voice** (cell 15, "Test Yourself"): cell 16 names variables `hello`, `name`, `greet`, `hello3`, `s`, `titled` — `hello3` is not a great name. Rename to `hello_repeated` or `greeting_x3`.

## lessons/20_Types_and_Logic/30_Control_Flow.ipynb

- **Voice** (cell 10, code comment): `print("Hooray!")` — kid-TV exclamation. Replace with something matter-of-fact like `print("Both checks passed.")`.

## lessons/20_Types_and_Logic/50_My_Ages.py

- **Voice** (line 16, docstring): `print "You are pretty awesome!"` — "awesome" used as an intensifier. Replace with `print("You're the same age as me.")`.

## lessons/20_Types_and_Logic/70_Infuriating_Calculator.py

- **Voice** (lines 1–5): "Let's write a calculator that's really hard to use, not because we want it to be hard, but just because we haven't learned how to make it easy yet." — chatty meta-aside. Tighten to: "Write a calculator that asks for inputs one at a time. Later lessons will show how to make this friendlier."

## lessons/20_Types_and_Logic/80_Code_Challenges.ipynb

- **Voice** (cell 0, "Code Wars" paragraph): "...Code Wars has a more competitive and gamified experience—think of it like Rocket League for coding." — surrounding pitch reads like marketing copy. Trim.

---

# Module 30 — Loops

## lessons/30_Loops/10_Iteration.ipynb

- **Voice** (cell 0, opening paragraph): "loops are actually a lot more interesting" and "expads it to make it even more useful" — mildly cheerleader-ish and contains a typo ("expads"). Rewrite: "In this module we'll go further with iteration: looping over collections, generating sequences with `range()`, and working with lists, tuples, and strings."

## lessons/30_Loops/20_Loops_with_Range.ipynb

- **Voice** (cell 9): "These [Badgers]..., but instead, they have their own rules" reads slightly stilted. Tighten to: "These badgers play their own version of FizzBuzz."

## lessons/30_Loops/70_List_Story.py

- **Voice** (lines 11–12): word list mixes emoji and text tokens. `'⚽.'` glues a punctuation mark to the emoji. Split into `'⚽'` and `'.'` so students have flexibility.

## lessons/30_Loops/80_Strings.ipynb

- **Voice** (cell 26, comment): `# Doesn't that look weird?` — kid-TV-host moment. Replace with `# Note: the separator string comes first, then .join()`.
- **Voice** (cell 9, header): "Fancy Formatting (f-strings)" — use "String Formatting with f-strings."

## lessons/30_Loops/90_Fizz_Buzz_Badgers.py

- **Voice** (line 13): the file's task is essentially "change the start/step of `range()`" — make this explicit so students don't hunt.

## lessons/30_Loops/100_For_Loop_Gauntlet.ipynb

- **Voice** (cell 539e9340): trim "Carefully read and complete each challenge below" to "Complete each challenge."

## lessons/30_Loops/120_More_Iterables.ipynb

- **Voice** (cell 12, comment): `# <- Ok, look, unpacking!` — kid-TV-host. Replace with `# Note: each iteration unpacks the pair into list1, list2`.
- **Voice** (cell 22, comment): `# Important, but you knew that!` — drop. Just `# islice() comes from itertools`.
- **Voice** (cell 23, header): "A Slice of Infinite Possibilities" — re-explains `islice()` after it was just introduced. Remove duplicate or rename to "More on `islice()`."
- **Voice** (cell 32): "The real power comes from combining these functions together!" — drop. Use "These functions compose well — here are some practical combinations."
- **Voice** (cell 0): "Python has some very important iteration functions" — drop "very."

---

# Module 40 — Data Structures and Functions

## lessons/40_Data_Structures_Func/10_Functions.ipynb

- **Voice** (cell 0, title): "**Functions and Data Structures**" but this lesson is exclusively about functions. Rename to "**Functions**" so the title matches the contents.

## lessons/40_Data_Structures_Func/20_Exceptions.ipynb

- **Voice** (cell 4): "led to a crash" is slightly dramatic; consider "stopped the program before the loop could finish."

## lessons/40_Data_Structures_Func/30_Dicts_Sets.ipynb

- **Voice** (cell 10): "You know what a real dictionary is, right?" — kid-TV-host. Rewrite: "A real-world dictionary is a book that maps words to definitions. Python dictionaries do the same thing with key-value pairs."
- **Voice** (cell 11, comment): "a collection of superior words and their definitions" — "superior" is odd. Suggest "uncommon words" or "fancy words."

## lessons/40_Data_Structures_Func/50_Splat_Comprehension.ipynb

- **Voice** (cell 6, code comment): "<--- HERE IS THE MAGIC" — kid-TV-ish. Replace with "# transpose the board".
- **Voice** (cell 7): "First, let's understand how `zip()` performs this magic trick." — drop "magic trick".
- **Voice** (cell 9): "Imagine the `*` as saying 'take apart this container...'" — tighten to: "The `*` unpacks the list so each row is passed as a separate argument."
- **Voice** (cell 30, header): "## **Challenge: Make It Better!**" — replace with "## **Challenge: Combine the Checks**".

---

# Module 50 — Projects

## lessons/50_Projects/10_Hotel_Management.md

- **Voice** (Getting Started): "Code away, make sure to keep it organized so you know where things are and what they do." — slightly throwaway. Replace with "Then start coding. Keep things organized so you can find them again later."
- **Voice** (closing line): "Have fun." as a bare one-liner reads like filler. Drop or fold into a real summary.
- **Voice** (Getting Started, third bullet): "Write down your thoughts as a list or instructions to yourself inside the docstring" — unusual advice. Move to a separate plan/`README` file or teach a "comments at the top" convention.

## lessons/50_Projects/20_Random_Walk.py

- **Voice** (docstring opening): "A simple turtle program that moves the turtle randomly in the grid" then "This program will perform a 'random walk' by moving the turtle randomly in the grid." — same sentence twice. Cut to one line.

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Voice** (cell 0, title): "**So you want to be an ASCII Artist?**" — borderline kid-TV-host. Prefer a flat title like "ASCII Art".
- **Voice** (cell 0): "There's more where that came from." — drop colloquial filler.
- **Voice** (cell 0): "Now you might be thinking, man, that looks complicated." — rewrite without the imagined-student-monologue framing.
- **Voice** (cell 0, "Note"): "the only requirement here is having fun" — contradicts the explicit Requirements cell. Drop or rephrase.
- **Voice** (Before You Begin): trim the emoji column.

## lessons/50_Projects/Temp_Project_Ideas/Spin_The_Wheel.ipynb

- **Voice** (cell 0): "Do you know someone who likes to watch game shows on TV? Have you ever wanted to create your own?" — back-to-back rhetorical questions. Cut.
- **Voice** (cell 0): "This is your chance to get creative and have fun." — drop.
- **Voice** (cell 0): "Software development is all about problem-solving and creativity. So, think about how you can make your game engaging and enjoyable for players." — generic motivational filler. Cut.

## lessons/50_Projects/Temp_Project_Ideas/Terminal_Game.ipynb

- **Voice** (cell 0): "Have you ever wanted to create your own text-based adventure game that runs in the terminal?" — opening rhetorical question. Replace with "In this project you'll build a small text-based adventure game that runs in the terminal."