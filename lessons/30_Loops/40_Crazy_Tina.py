"""
Create a program that will draw a crazy pattern using the turtle.

Create lists for the path that Tina will take, the angles 
she will turn, and the colors she will use. Then access those
lists to draw the pattern.

Review the ' Using Lists' section of the previous lesson if you need 
more help

hint: all of your lists should have the same number of elements.
uid: JBzJ2nx1
name: Crazy Tina
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Move at a moderate speed, not too fast.

forwards = [ ... ]
lefts = [ ... ]
colors = [  ... ]

for i in range(8):

    forward = ...
    left = ...
    color = ...

    tina.color(color)
    tina.forward(forward)
    tina.left(left)

turtle.exitonclick()  