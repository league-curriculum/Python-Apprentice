import random
from tkinter import Label, Button, Tk

from PIL import ImageTk


def onclick(args):
    if args == "button":
        # TODO 1) Make random_choice equal to a random number between 1 and 6
        random_choice = random.randint(1,6)

        # TODO 2) Fix the code below so that it displays the correct image
        if random_choice == 1:
            label.configure(image=dice1)
            label.photo_ref = dice1
        elif random_choice == 2:
            label.configure(image=dice2)
            label.image = dice2
        elif random_choice == 3:
            label.configure(image=dice3)
            label.image = dice3
        elif random_choice == 4:
            label.configure(image=dice4)
            label.image = dice4
        elif random_choice == 5:
            label.configure(image=dice5)
            label.image = dice5
        else:
            label.configure(image=dice6)
            label.image = dice6



window = Tk()
window.title("Roll the Dice!")

dice1 = ImageTk.PhotoImage(file="dice 1.png")
dice2 = ImageTk.PhotoImage(file="dice 2.png")
dice3 = ImageTk.PhotoImage(file="dice 3.png")
dice4 = ImageTk.PhotoImage(file="dice 4.png")
dice5 = ImageTk.PhotoImage(file="dice 5.png")
dice6 = ImageTk.PhotoImage(file="dice 6.png")

Button(window, text="CLICK HERE TO ROLL", command=lambda: onclick("button")).pack(side="left")

label = Label(window, image=dice1).pack(side="left")

# Start the GUI
window.mainloop()