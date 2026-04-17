"""
# Squares_and_Circles.py

This Turtle program demonstrates basic drawing and text output in Python.
It draws a colored square, places a filled circle inside it, and writes a message on the screen.
Lines starting with # are single-line comments, used to describe what each part of the code does.
Text enclosed in triple quotes (like this) is a docstring, which provides a multi-line explanation at the top of the file.

Review each section to see how the turtle is moved, how shapes are drawn, and how text is displayed.
"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Move at a moderate speed, not too fast.

##
## Move Tina to the Starting Position
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 100)                    # Move tina to the starting position
tina.pendown()                          # Put the pen down so we can draw

##
## Draw a Square
## Repeat forward + right three more times to complete the square.
##

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(200)                       # Move tina forward by the forward distance
tina.right(90)                          # Turn tina right by 90 degrees

tina.pencolor('red')                    # Set the pen color to red
tina.forward(200)
tina.right(90)

tina.pencolor('green')                  # Set the pen color to green
tina.forward(200)
tina.right(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(200)
tina.right(90)

##
## Draw a Circle
##

tina.penup()
tina.goto(0, -75)
tina.pendown()

tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(75)
tina.end_fill()

##
## Write a Message
##

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-30, -130)                    # Move to where the text should appear
tina.write("Why, hello there!")         # Write the message "Why, hello there!"

turtle.exitonclick()                    # Close the window when we click on it

# Nice work. Save your progress in the next lesson, 40_Check_In_Your_Code.ipynb
