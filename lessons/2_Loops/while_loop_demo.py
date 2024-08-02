"""
while loops and the break keyword Demo
"""
from tkinter import messagebox, simpledialog, Tk

# While loops are similar to for loops. Both repeat the code inside the loop.
# The for loop repeats code for a specified number of times.
# The while loop repeats code for as long as a condition is True.
# A while loop looks like this:
#
#   while <condition>:
#       # Code to repeat
#
# Where <condition> is a boolean variable or something that evaluates to a
# boolean (True or False). This is similar to an if or elif statement.
# Here is an example of a while loop:
#
#   name = ""
#   while name == "" or name is None:
#       name = simpledialog.askstring(None, prompt="What is your name?")
#
# The while loop above keeps showing a pop-up message box until the user types
# something in the text field. A while loop can potentially go on forever if
# the condition is always True. A 'break' statement is used to exit the while
# loop immediately. The code below does the same thing except uses a break
# statement instead:
#
#   while True:
#       name = simpledialog.askstring(None, prompt="What is your name?")
#       if name != "" and name is not None:
#           break
#


window = Tk()
window.withdraw()

name = ""
while name == "" or name is None:
    name = simpledialog.askstring(None, prompt="What is your name?")

# Code below only executes when the user types something in the text field
messagebox.showinfo(None, "Your name is " + name)

while True:
    name = simpledialog.askstring(None, prompt="What is your name again?")
    if name != "" and name is not None:
        break

messagebox.showinfo(None, "Your name again is " + name)
