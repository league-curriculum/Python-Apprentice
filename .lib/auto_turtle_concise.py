#!/usr/bin/env python
"""
auto_turtle_concise.py
Inherits setup from auto_turtle.py and initializes 'tina'.

This just inherits the setup from auto_turtle.py but creates 'tina' the turtle for you.
It's a more concise way to get started with Tina the Turtle without having to write the setup code again.
My intent was to use this for the later examples in this course since they already will know how to use Tina at that point.
"""

try:
    # Attempting to open and execute auto_turtle.py to inherit its setup
    # Use utf-8 to prevent a UnicodeDecodeError on some systems
    with open(".lib/auto_turtle.py", encoding="utf-8") as f:
        exec(f.read())

    # Setup Tina (using the variables inherited from auto_turtle.py)
    # These will only run if the 'exec' above was successful
    tina = turtle(myTS)          # type: ignore[name-defined]
    tina.shape('turtle')
    tina.speed(5)

except FileNotFoundError:
    print("Error: Could not find and inherit from '.lib/auto_turtle.py'.")
    print("Please ensure auto_turtle.py exists in the .lib directory.")

except Exception as e:
    # Any other exceptions that may occur
    print(f"Error: {e}")