""" A simple turtle program that moves the turtle randomly in the grid 

This program will perform a "random walk" by moving the turtle randomly in the grid.

Implement the random_walk function that will move the turtle randomly in the grid.

"""

import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")

# Set up the turtle
walker = turtle.Turtle()
walker.shape("turtle")
walker.penup()
walker.speed(0)  # Set to the maximum speed
walker.goto(0, 0)  # Start in the middle of the grid
walker.pendown()

# Function to move the turtle randomly in the grid
def random_walk(walker, steps):
    """ Implement a random walk for the turtle

    The turtle will move on a grid, taking a random step in one of the four directions

    For each of the steps, the turtle will move in a random direction (N, E, S, W) 
    a fixed number of steps. Fur instance, the turtle should move 10 pixels each time, but
    in a random, direction. 

    Args:
    walker (turtle.Turtle): The turtle object
    steps (int): The number of steps to take

    """

    # You can make the turle move randomly in either of two ways: randomly choosing a direction
    # or randomly choosing a angle to turn. You can use random.choice() to select a random element
    # from a list, like this: 
    # direction = random.choice(["N", "E", "S", "W"])
    # or
    # angle = random.choice([0, 90, 180, 270])
    #
    # Or you can use random.randint() to generate a random integer between two values, like this:
    # angle_index = random.randint(0, 4)
    # directions = ["N", "E", "S", "W"] # or directions = [0, 90, 180, 270]
    # direction = directions[angle_index]
    #
    # To set the turtle's heading, you can use the setheading() method, like this:
    # walker.setheading(angle)  # North
    #
    # you can use the right() or left() methods to turn the turtle, like this:
    # walker.right(angle)  # Go straight
    #
    #
    # Read one of the past turtle programs to see how to use these methods.

    # Your code here



# Start the random walk
random_walk(walker, 200)

# Close the turtle window on click
screen.exitonclick()
