# Review: 50_Projects

Delete any bullet you don't want applied, then hand the file back and I'll apply the rest.

---

## lessons/50_Projects/README.md

- No findings. (The file just has the uid and the heading "Projects".)

---

## lessons/50_Projects/10_Hotel_Management.md

- **Voice** (line 5): "This is going to be your 1st program you write all by yourself" — informal "1st". Rewrite as
  "This is the first program you'll write on your own."
- **Technical** (line 10): `(it's the triple quotes """  stuff goes inside """)` — the quotes in the file are
  curly smart quotes (`“””`), not straight quotes (`"""`). Python doesn't accept smart quotes, so a student who
  copies this verbatim will get a SyntaxError. Replace with straight triple-quote characters.
- **Voice** (line 46): "Have Fun!!!" — three stacked exclamation points. Rewrite as "Have fun." or drop.

---

## lessons/50_Projects/20_Random_Walk.py

- **Technical** (line 35, docstring): "Fur instance" — typo, should be "For instance".
- **Technical** (line 44, comment): "You can make the turle move randomly" — typo, should be "turtle".
- **Technical** (line 52, example code in comment): `angle_index = random.randint(0, 4)` — off-by-one bug. A
  student who copies this literally will get an `IndexError` when `angle_index == 4`, because `directions` has
  only four elements (indices 0–3). `random.randint(0, 4)` is inclusive of both ends. Fix to
  `random.randint(0, 3)`.

---

## lessons/50_Projects/Temp_Project_Ideas/

- **Flow** (folder name): `Temp_Project_Ideas` — the prefix "Temp" suggests these are drafts. None of the three
  files are referenced in `lessons/.jtl/syllabus.yaml`, so they don't appear in the student flow. Flagging for a
  decision: keep and wire them into the syllabus, rename the folder to something less provisional (e.g.
  `More_Project_Ideas`), or delete if abandoned. I'll only touch voice/technical issues in the files below
  — not the folder itself — without your call.

---

## lessons/50_Projects/Temp_Project_Ideas/30_ASCII_Art.ipynb

- **Voice** (cell a8e43baa, opening): "Perfect!" — drop the line or drop the exclamation.
- **Voice** (cell a8e43baa, mid-paragraph): "Pretty cool, right? Oh there's more?!" — stacked `?!` and the
  "Pretty cool" phrasing. Rewrite as "There's more where that came from." or similar.
- **Voice** (cell 2553aff8): "Of course, feel free to explore and find other characters that you like!" — drop
  the exclamation.
- **Voice** (cell 2553aff8): "And no, it's not cheating to look at ASCII art generators online, there are plenty
  of free ones that can create some really cool designs!" — drop "really cool", drop the exclamation. Rewrite as
  "It's not cheating to use an ASCII-art generator online — there are plenty of free ones that can create good
  designs."
- **Voice** (cell e63a0b03, requirements): "- **Have Fun:** Build something you enjoy!" — drop the exclamation.
- **Voice** (cell e63a0b03, additional info): "prioritize effective usage while being creative!" — drop the
  exclamation.

---

## lessons/50_Projects/Temp_Project_Ideas/Spin_The_Wheel.ipynb

- **Voice** (cell ad97bb84): "Well, instead of physical, let's create a digital game that you can play on your
  computer!" — drop the exclamation. Also the phrasing "instead of physical" reads as a sentence fragment.
  Rewrite: "Instead of a physical wheel, let's build a digital version you can play on your computer."
- **Voice** (cell ad97bb84): "However, feel free to add your own twist to the game! This is your chance to get
  creative and have fun." — drop the exclamation.
- **Technical** (cell ad97bb84): "Software Development is all about problem-solving and creativity." — "Software
  Development" shouldn't be capitalized here (it isn't a proper noun). Lowercase it: "Software development is all
  about problem-solving and creativity."

---

## lessons/50_Projects/Temp_Project_Ideas/Terminal_Game.ipynb

- No findings.
