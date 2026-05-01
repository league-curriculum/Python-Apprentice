"""
FizzBuzz Grid

We're going to use a Windowing library, guizero, to create a 10x10 grid of
numbers, with each number in a separate cell, but we're also going to set the
color of the number based on the following rules:

* If the number is evenly divisible by 5, print '🦡'
* If the number is evenly divisible by 3, print '🍄'
* If the number is evenly divisible by 15, print '🐍'
* If it is divisible by none of these, print the number.

Because any multiple of 15 is also a multiple of 5 and 3, check for 15 first.

If you are displaying a number, color it as follows:

* If the sum of the digits of the number is even, color the number blue
* If the sum of the digits of the number is odd, color the number red

This lesson uses `guizero`, a small GUI library. Don't worry about how it works —
copy the examples and change the `Text(...)` call to show what you want.

Here is how you can display a number in your grid. Call this function in your loop
to display the number in the grid cell at the row and column you specify.

    Text(app, text=str(number), grid=[col, row], color=color)

Or to display a badger:

    Text(app, text='🦡', grid=[col, row], color=color)

or you can convert the number to a string and iterate over the digits

HINT: You can use % and // to get the first and last digit of a number.

uid: cKjBvzzU
name: Fizzbuzz Gui Grid
"""

from guizero import App, Box, Text

app = App("Numbers Grid", layout="grid")

# Create a 10x10 grid using nested loops
# Or you can use a single loop and calculate the row and column

for col in range(0,9):
    for row in range(0,9):
        Text(app, text='🦡', grid=[col, row], color='red')

# In the loop, calculate or increment the number

# Use % to determine the display, using FizzBuzz rules

# If you are displaying a number, calculate the sum of the digits and determine the color

# Call Text(app, text='...', grid=[col, row], color=...) to display something.

app.display()
