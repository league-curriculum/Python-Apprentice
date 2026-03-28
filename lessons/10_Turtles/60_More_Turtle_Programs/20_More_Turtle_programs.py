"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""

import turtle
def set_turtle_image(turtle, image_name):
    """set the turtles shape to a custom imagen."""
    from pathlib import Path 
    image_dir = Path(__file__).parent.parent /"images"
    image_path = str(image_dir / image_name)
    
    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

#set up the screen
screen = turtle.screen()
screen.setup(width=600, height=600)

# create a turtle and set its shape to the custom gif
t = turtle.turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()
t.speed(3)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)


turtle.exitonclick()   