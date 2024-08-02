import random
from tkinter import messagebox, Tk, simpledialog



window = Tk()
window.withdraw()

# TODO 1) Get the user to enter a question for the 8 ball to answer
name = simpledialog.askstring(None, "Ask a question")

# TODO 2) Make a variable and initialize it to a random number.
#         You will need to make a random object!
#         Limit the random numbers to be between 0 and 3
randNum = random.randint(0, 3)

# TODO 3) If the random number is 0
if randNum == 0:
    # TODO --tell the user "Yes"
    messagebox.showinfo(None, "Yes")

# TODO 4) If the random number is 1
elif randNum == 1:
    # TODO --tell the user "No"
    messagebox.showinfo(None, "No")

# TODO 5) If the random number is 2
elif randNum == 2:
    # TODO --tell the user "Maybe you should ask Google?"
    messagebox.showinfo(None, "Maybe you should ask Google?")

# TODO 6) If the random number is 3
else:
    # TODO --write your own answer
    messagebox.showinfo(None, "Ask again later")