"""
# 40_Turtle_Spiral.py

This program already works. See if you can change it to make it draw a different pattern.

uid: rkftzcAi
name: Turtle Spiral
"""

import random
import turtle

# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))

window = turtle.Screen()
window.bgcolor("white")

# Make a new turtle
my_turtle = turtle.Turtle()

# This code sets our shape to a turtle
my_turtle.shape("turtle")

# Set your turtle's speed
my_turtle.speed(0)

# Set your turtle's color
my_turtle.color("green")

# Use a loop to repeat the code below 50 times
for i in range(50):

    # Set the turtle color to a random color
    my_turtle.pencolor(get_random_color())

    # Move the turtle (5*i) pixels. 'i' is the loop variable
    my_turtle.forward(9 * i)

    # Turn the turtle (360/7) degrees to the right
    my_turtle.right(360 / 7 + i*5)

    # Change the turtle width to 'i' (the loop variable)
    my_turtle.width(i)

    # Check the pattern against the picture in the recipe. If it matches, you are done.

turtle.done()

# Now check in your code.
