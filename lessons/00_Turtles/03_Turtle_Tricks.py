# For this program, you will tell Tina the Turtle to 
# draw  shapes. 

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
tina = turtle.Turtle()                  # Create a turtle named tina


# 1 Use .forward() and .left() to draw a triangle
# Make each side of the triangle a different color

... # your code here 

# 2 Use .goto() to go to a different part of the screen, 
# and use .penup() and .pendown() so there is no line
# when the turtle moves. Then .forward() and .right() 
# to draw a pentagon, and write a message in the middle
# of the pentagon using .goto() and .write()

... # your code here

# 3 Use .goto() to go to a different part of the screen,
# and use the code below, along with .color() 
# to draw a red circle()

... # your code here

tina.begin_fill() 
tina.circle(100, steps=50)
tina.end_fill() 

# 4 continue with the file 04_Loops.ipynb

... # your code here


turtle.exitonclick()                    # Close the window when we click on it
