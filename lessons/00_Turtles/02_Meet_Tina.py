"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast.

tina.pencolor('blue')                   # Set the pen color to blue
tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.pencolor('red')                    # Set the pen color to red
tina.forward(150)                       # Continuie the last two steps three more times
tina.left(90)                           # to draw a square

tina.pencolor('green')                  # Set the pen color to green
tina.forward(150)
tina.left(90)

tina.pencolor('purple')                 # Set the pen color to purple
tina.forward(150)
tina.left(90)

tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.forward(20)                        # Move tina forward by 20
tina.left(90)                           # Turn tina left by 90 degrees
tina.forward(20)                        # Move tina forward by 20
tina.write("Why, hello there!")         # Write the message "Why, hello there!"
tina.backward(20)                       # Move tina backward by 20

tina.goto(-50,0)
tina.pendown()
tina.color('red')                       # Set the color of tina to red
tina.begin_fill()
tina.circle(101, steps=50)
tina.end_fill()

turtle.exitonclick()                    # Close the window when we click on it

# Now you can try writing your own programs. Open
# the next file 03_Turtle_Tricks.py

