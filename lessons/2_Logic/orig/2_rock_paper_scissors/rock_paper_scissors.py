import random
from tkinter import Tk, Label, Button, messagebox

from PIL import ImageTk


def onclick(args):
    # TODO 1) Run the program and play many rounds of Rock Paper Scissors. Does the computer always choose the same thing?

    # TODO 2) Change the value of opponent_selection to be a random number between 1 and 3
    opponent_selection = 1
    opponent_selection = random.randint(1,3)
    # TODO 3) Run the program again. Is the result different?

    selection = 1

    if args == "PAPER":
        selection = 2
    elif args == "SCISSORS":
        selection = 3

    messagebox.showinfo(None, "You chose: " + str(args) + ".\n"
                        + "The computer chose: " + opp_select(opponent_selection) + ".\n")

    if selection == opponent_selection:
        messagebox.showinfo(None, "No Winner. Play Again.")
    elif (selection == 1 and opponent_selection == 3) or (selection == 2 and opponent_selection == 1) or (
            selection == 3 and opponent_selection == 2):
        messagebox.showinfo(None, "You Win!")
    else:
        messagebox.showinfo(None, "You Lose!")


def opp_select(s):
    if s == 1:
        return "ROCK"
    if s == 2:
        return "PAPER"
    if s == 3:
        return "SCISSORS"



window = Tk()
window.title("Rock Paper Scissors")
window.geometry("1075x250")
window.configure(background="grey")

Label(window, text="Choose Your Weapon!", bg="grey").pack(side="left")

img_rock = ImageTk.PhotoImage(file="rock.png")
img_paper = ImageTk.PhotoImage(file="paper.jpeg")
img_scissors = ImageTk.PhotoImage(file="scissors.jpeg")

Button(window, image=img_rock, command=lambda: onclick("ROCK")).pack(side="left")
Button(window, image=img_paper, command=lambda: onclick("PAPER")).pack(side="left")
Button(window, image=img_scissors, command=lambda: onclick("SCISSORS")).pack(side="left")

# Start the GUI
window.mainloop()
