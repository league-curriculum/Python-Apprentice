"""
# 10_Flaming_Ninja_Star.py

This program already works; run it to see what it does.
Then change it to make it draw a different pattern.

uid: ejUIkGvk
name: Flaming Ninja Star
"""

import random
import turtle


# Returns a random color!
def get_random_color():
    return "#%06X" % (random.randint(0, 0xFFFFFF))


colors = ["red", "blue", "green", "yellow", "orange"]


def get_next_color(i):
    return colors[i % len(colors)]

turtle.setup(600, 600, 0, 0)            # Set the size of the window
window = turtle.Screen()

base_size = 200  # the size of the black part of the star
flame_size = 130  # the length of the flaming arms

t = turtle.Turtle()
t.shape("turtle")
t.width(2)
t.speed(0)

for i in range(25):
    t.pencolor(get_random_color())
    t.fillcolor(get_random_color())
    t.begin_fill()
    t.forward(64)
    t.left(40)
    t.forward(flame_size)
    t.right(170)
    t.forward(flame_size)
    t.right(62)
    t.forward(base_size)
    t.end_fill()

t.hideturtle()

turtle.done()
