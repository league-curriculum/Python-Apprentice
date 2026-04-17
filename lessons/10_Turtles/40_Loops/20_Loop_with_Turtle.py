"""
# 20_Loop_with_Turtle.py

This program currently uses four pairs of lines to move and turn the turtle,
drawing each side of a square individually.

In this exercise, you will modify the program to use a loop to draw the square instead.

- Replace the repeated movement and turning lines with a for loop that runs four times.

uid: 85lNu5qj
name: Loop With Turtle
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Move at a moderate speed, not too fast.

# Repeat forward + left three more times to finish the square.
tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by 90 degrees

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)

turtle.exitonclick()                    # Close the window when we click on it
