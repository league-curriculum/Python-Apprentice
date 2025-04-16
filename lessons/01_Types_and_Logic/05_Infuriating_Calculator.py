"""
Infuriating Calculator

Let's write a calculator that's really hard to use, not because we want it to be
hard, but just because we haven't learned how to make it easy yet.

Ask the user for three things: 

1. A number
2. A second number
3. A math operation (add, subtract, multiply, divide)
4. Use if-elif-else statements to provide the desired math operation on the
   numbers and display the result.

If the user enters an unknown operation, display an error message. ( use
messagebox.showerror() 

For the number, you can ask for a float or an integer with
simpledialog.askfloat() or simpledialog.askinteger(), and for the math operation
you can ask for a string with simpledialog.askstring().

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


# Ask the user for the math operation
oper = simpledialog.askstring("Operation", "Gimme a operation in STRINGY TERMS") 
# Use if-elif-else statements to provide the desired math operation on the numbers and display the result.
if oper == 'add':
    final = num1+num2
if oper == 'subtract':
    final = num1-num2
if oper == 'multiply':
    final = num1*num2
if oper == 'divide':
    final = num1/num2        
else:
    messagebox.showerror        
# If the user enters an unknown operation, display an error message. ( use messagebox.showerror()
messagebox.showinfo('Final Answer', "Your answer is: " + str(final))


window.mainloop()
# Keep the window open
