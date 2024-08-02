"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY into your program.
     Using a loop and if-statements, you must figure out how to vary the text and the positioning 
     so that you can read all four separate lines.
"""

from tkinter import Canvas
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF")
canvas.grid()

"""
Text Rendering Example:
                    x   y                                                       
canvas.create_text(100, 50, text="text goes here", font=("Arial", 16))
"""
# Put your code here
banana_message = ""  # ;

for i in range(4):  # ;
    if i == 3:  # ;
        banana_message += "banana"  # ;
    else:  # ;
        banana_message += "ice cream\n"  # ;

canvas.create_text(100, 100, text=banana_message, font=("Arial", 16))  # ;


root.mainloop()  # ;
