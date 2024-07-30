import turtle
from tkinter import messagebox, simpledialog, Tk


# Ask the user what shape they want to draw and store it in a variable using the askstring() method
shape = simpledialog.askstring(  # ;
    None,  # ;
    "What kind of shape do you want to draw?\nOptions: triangle, square, circle",  # ;
)


def draw_shape(shape):
    # Delete the pass statement and write your code here
    pass
    # Create a turtle object
    my_turtle = turtle.Turtle()  # ;
    # Set the turtle's shape to "turtle" using the .shape() method
    my_turtle.shape("turtle")  # ;
    # Set the turtle's pen down using the .pendown() method
    my_turtle.pendown()  # ;

    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":  # ;
        for i in range(3):  # ;
            my_turtle.forward(100)  # ;
            my_turtle.right(120)  # ;
    elif shape == "square":  # ;
        for i in range(4):  # ;
            my_turtle.forward(100)  # ;
            my_turtle.right(90)  # ;
    elif shape == "circle":  # ;
        my_turtle.circle(100, 360, steps=50)  # ;
    else:  # ;
        messagebox.showerror(None, "I don't know how to draw a " + shape)  # ;

    # Call the turtle .done() method
    turtle.done()  # ;


window = Tk()
window.withdraw()

# Call the draw_shape() function and pass the user's shape as an argument
draw_shape(shape)  # ;

# Call the mainloop() method
window.mainloop()  # ;
