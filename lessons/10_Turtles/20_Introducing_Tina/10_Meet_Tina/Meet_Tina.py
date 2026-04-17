"""
# Meet_Tina.py

This program draws Tina: a turtle with a hexagon-shaped green shell, four brown legs, a head, and a tail.

There are two ways to run this program:
1. Click the 'Run' (▶) button at the top of your editor window OR in the bottom left corner.
2. Press the F5 key (in editors like VS Code, Thonny, or GitHub Codespaces).

You don't need to understand all of this yet. Later lessons will walk through it piece by piece.
"""

import turtle                           # Tell Python we want to work with the turtle
from math import radians, tan

turtle.setup(600, 600, 0, 0)            # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.speed('fastest')                   # Set the speed of the turtle to fastest

# Draw the hexagon
tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 175)                    # Move tina to the starting position
tina.pendown()
tina.begin_fill()

def head_pos(l=200):
    """ Position of tina's head, relative to the center of the screen"""
    return (l/2) / tan(radians(30))

def draw_body(t, l=200):
    """Draw the body of the turtle"""
    t.pencolor('green')                  # Set the pen color to green
    t.fillcolor('green')                 # Set the fill color to green
    t.penup()
    t.goto(0,0)                          # Move tina to the center of the screen
    t.setheading(-90)                    # Set the heading of tina to -90 degrees
    t.forward(head_pos(l))               # Move tina forward by the head position
    t.right(90)                          # Turn tina right by 90 degrees
    t.backward( l/2 )                    # Move tina backward by half the length
    t.pendown()
    t.begin_fill()
    for _ in range(6):
        t.forward(l)                     # Move tina forward by the length
        t.right(60)                      # Turn tina right by 60 degrees
    t.end_fill()

def draw_leg(t, a, r=170, w=40, l=50):
    """Draw A Leg"""
    t.penup()
    t.goto(0, 0)                         # Move tina to the center of the screen
    t.setheading(a)                      # Set the heading of tina to the angle
    t.forward(r)                         # Move tina forward by the radius
    t.pendown()
    t.pencolor('brown')                  # Set the pen color to brown
    t.fillcolor('brown')                 # Set the fill color to brown
    t.begin_fill()
    t.left(90)                           # Turn tina left by 90 degrees
    t.forward(w/2)                       # Move tina forward by half the width
    t.right(90)                          # Turn tina right by 90 degrees
    t.forward(l)                         # Move tina forward by the length
    t.right(90)                          # Turn tina right by 90 degrees
    t.forward(w)                         # Move tina forward by the width
    t.right(90)                          # Turn tina right by 90 degrees
    t.forward(l)                         # Move tina forward by the length
    t.right(90)                          # Turn tina right by 90 degrees
    t.forward(w/2)                       # Move tina forward by half the width
    t.end_fill()

def draw_head(t):
    """Draw a brown head at the head position"""
    t.penup()
    t.goto(0, head_pos()-20)             # Move tina to the head position
    t.pendown()
    t.pencolor('brown')                  # Set the pen color to brown
    t.fillcolor('brown')                 # Set the fill color to brown
    t.begin_fill()
    t.circle(50)                         # Draw a circle with radius 50
    t.end_fill()

def say_hello(t):
    """Make tina say hello, with text to the right of her head"""
    t.penup()
    t.goto(75, head_pos()+75)            # Move tina to the position for the text
    t.pendown()
    t.write("Hello! I'm Tina!", font=("Arial", 20, "normal"))  # Write the text

draw_head(tina)

for lp in (30, -30, -150, 150):
    draw_leg(tina, lp)                   # Draw the legs at the specified angles

draw_leg(tina, -90, r=170, w=10, l=50)   # This one is actually a tail!

draw_body(tina)                          # Draw the body of the turtle

say_hello(tina)                          # Make tina say hello

turtle.exitonclick()                     # Close the window when we click on it
