"""

Run this program to meet Tina the Turtle. Tina is a
hexagon with legs and a head.

You can run this program by:

1) clicking on ▶️ icon ar the top of the editor
window
2) Hit the F5 function key

You won't understand what this program is doing just
yet, but don't worry, that's what you will be
learning in the next few lessons.

"""

import turtle                           # Tell Python we want to work with the turtle
turtle.setup(600,600,0,0)               # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.speed('fastest')                   # Set the speed of the turtle to fastest

# Draw the hexagon
tina.penup()                            # Lift the pen up so we can move tina without drawing
tina.goto(-100, 175)                    # Move tina to the starting position
tina.pendown()
tina.begin_fill()

def head_pos(l=200):
    """ Position of tina's head, relative to the center of the screen"""
    from math import radians, tan
    return  (l/2) / tan(radians(30))

def draw_body(t, l = 200):
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

def draw_head():
    """Draw a brown head at the head position"""
    tina.penup()
    tina.goto(0, head_pos()-20)          # Move tina to the head position
    tina.pendown()
    tina.pencolor('brown')               # Set the pen color to brown
    tina.fillcolor('brown')              # Set the fill color to brown
    tina.begin_fill()
    tina.circle(50)                      # Draw a circle with radius 50
    tina.end_fill()

def say_hello():
    """Make tina say hello, with text to the right of her head"""
    tina.penup()
    tina.goto(75, head_pos()+75)         # Move tina to the position for the text
    tina.pendown()
    tina.write("Hello! I'm Tina!", font=("Arial", 20, "normal"))  # Write the text

draw_head() 

for lp in (30, -30, -150, 150):
    draw_leg(tina, lp)                   # Draw the legs at the specified angles

draw_leg(tina, -90, r=170, w=10, l=50)   # This one is actually a tail!

draw_body(tina)                          # Draw the body of the turtle

say_hello()                              # Make tina say hello

turtle.exitonclick()                     # Close the window when we click on it
