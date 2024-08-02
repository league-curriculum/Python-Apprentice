
# 1) Improve the code below to draw a square using a loop

import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

tina.forward(150)                       # Move tina forward by the forward distance
tina.left(90)                           # Turn tina left by the left turn

tina.forward(150)                       # Continuie the last two steps three more times
tina.left(90)                           # to draw a square

tina.forward(150)
tina.left(90)

tina.forward(150)
tina.left(90)

# 2) Move Tina away from the square and then use a loop to draw a pentagon

... # Your code here


# 3) Move Tina away from the pentagon and then use a loop to draw a hexagon

... # Your code here 

turtle.exitonclick()                    # Close the window when we click on it
