# Write a Python program that asks the user for two numbers.
# Then display the sum of the two numbers
# Import the messagebox, simpledialog, and Tk classes from the tkinter module
from tkinter import messagebox, simpledialog, Tk  # ;

# Create a window object
window = Tk()  # ;
# Hide the window, hint: use the withdraw method
window.withdraw()  # ;

num1 = simpledialog.askfloat(None, "Enter a number")  # ;
num2 = simpledialog.askfloat(None, "Enter a second number")  # ;

messagebox.showinfo(  # ;
    None,
    "The sum of " + str(num1) + " and " + str(num2) + " = " + str(num1 + num2),  # ;
)

# Don't forget to call the mainloop method
window.mainloop()  # ;
