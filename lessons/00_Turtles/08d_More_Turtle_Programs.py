"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.

Use this code to get a random x and y location


    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

"""

# Double click on this cell to copy the code

import turtle as turtle
import random
turtle.setup(width=600, height=600)

t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def turtle_clicked(t, x, y):
    """Function that gets called when the user clicks on the turtle

    This function will make the turtle tilt 20 degrees 18 times, making a full
    circle. It is called by the turtle when the user clicks on it.

    Args:
        t (Turtle): The turtle object that was clicked
        x (int): The x coordinate of the click
        y (int): The y coordinate of the click
    """
    t.penup()
    print('turtle clicked!')
    t.goto(x,y)
    t.pendown()
    t.circle(30)

# Connect the turtle to the turtle_clicked function
screen.onclick(lambda x, y, t=t: turtle_clicked(t,  x,y))


turtle.done() # Important! Use `done` not `exitonclick` to keep the window open


