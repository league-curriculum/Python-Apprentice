"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw() # Hide the window; we just want to see pop ups
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
num1 = simpledialog.askinteger("Number 1", "Gimme a number") 
# Ask the user for the second number
num2 = simpledialog.askinteger("Number 2", "Gimme another number") 
# Display the sum of the two numbers 
final = num1+num2

messagebox.showinfo('Sum', "The sum is: " + str(final))
# Keep the window open
window.mainloop() 
