import random
import sys
from tkinter import simpledialog, messagebox, Tk


# TODO 1) Make a new window variable, window = Tk()
window = Tk()
# TODO 2) Hide the window using the window's .withdraw() method
window.withdraw()

# TODO 5) Change this line to give you a random number between 1 - 100
rand_num = random.randint(1,100)

# TODO 4) Print out the random variable above
print(rand_num)
# TODO 12) Repeat steps 1 to 10 ten times
for i in range(10):
    # TODO 3) Ask the user for a guess using a pop-up window, and save their response
    guess = simpledialog.askstring(title="Question", prompt="Guess a number between 1 and 100")
    # TODO 6) if the guess is correct
    if guess == str(rand_num):
        # TODO 7) Win
        messagebox.showinfo(message="You Win!!!")
        # TODO 12) Use "sys.exit(0)" to quit the game if the user guessed the right answer
        sys.exit(0)
    # TODO 8) if the guess is high
    if guess > str(rand_num):
        # TODO 9) Tell them it's too high
        messagebox.showinfo(message="Your guess was too high")
    # TODO 10) if the guess is low
    if guess < str(rand_num):
        # TODO 11) Tell them it's too low
        messagebox.showinfo(message="Your guess was too low")
# TODO 13) Tell them they lose
messagebox.showinfo(message="You Lose :(")