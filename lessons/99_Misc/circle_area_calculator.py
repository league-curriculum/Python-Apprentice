import turtle
from tkinter import messagebox, simpledialog, Tk
import math

window = Tk()
window.withdraw()

# Ask the user for the radius in pixels and store it in a variable
# simpledialog.askinteger()
radius = simpledialog.askinteger(None, "enter a radius")  # ;

# Make a new turtle
my_turtle = turtle.Turtle()  # ;

# Have your turtle draw a circle with the correct radius
# my_turtle.circle()
my_turtle.circle(radius=radius, extent=360, steps=50)  # ;

# Call the turtle .penup() method
my_turtle.penup()  # ;

# Move your turtle to a new x,y position using .goto()
my_turtle.goto(0, 0)  # ;

# Calculate the area of your circle and store it in a variable, you can use math.pi
area = math.pi * radius * radius  # ;

# Write the area of your circle using the turtle .write() method
# my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
my_turtle.write(  # ;
    arg="area = " + str(area), move=True, align="left", font=("Arial", 8, "normal")  # ;
)  # ;

# Hide your turtle
my_turtle.hideturtle()  # ;

# Call turtle.done()
turtle.done()  # ;
window.mainloop()
