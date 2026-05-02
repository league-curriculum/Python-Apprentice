#!/usr/bin/env python
"""
auto_turtle.py

This script automatically sets up the ipyturtle3 environment
for use in a Jupyter Notebook.

When used with %run, it will:
1. Import all necessary modules (turtle, Canvas, TurtleScreen, Turtle, display).
2. Create and display a default Canvas named 'myCanvas'.
3. Define a custom Turtle class that remaps the coordinate system so that
   the student's (0, 0) is at (start_x, start_y) on the canvas.
4. Display the Canvas in the notebook.
5. Wait a moment to ensure the canvas is rendered.
6. Create a TurtleScreen for the canvas named 'myTS'.
"""

import time # Might not be necessary, but used for sleep

# --- Configuration ---
canvas_width = 750         # Width of the turtle canvas
canvas_height = 250        # Height of the turtle canvas
start_x = -300             # Starting X position of the canvas
start_y = -50              # Starting Y position of the canvas
time_sleep = 0.1           # Time to wait for canvas rendering
# ---------------------

try:
    # 1. Import the main library and necessary classes
    import ipyturtle3 as turtle
    import sys, types
    from ipyturtle3 import Canvas, TurtleScreen, Turtle
    from IPython.display import display

    turtle = types.ModuleType("turtle") # Make a fake 'turtle' module
    # 2. Define a NEW Turtle class that overrides the original for custom behavior
    class turtle(Turtle):
        """
        Custom Turtle class that remaps the coordinate system.
        The student's (0, 0) is now our (START_X, START_Y).
        
        This class overrides all position-related methods to 
        translate between the student's "relative" coordinates
        and the canvas's "absolute" coordinates.
        """
        def __init__(self, screen=None, *args, **kwargs):
            """
            Initializes the turtle and moves it instantly
            to the new (0, 0) origin point.
            """
            # Store the new origin offset
            self._origin_x = start_x
            self._origin_y = start_y

            # Call the original __init__ to create the turtle
            super().__init__(screen, *args, **kwargs)
            
            # --- Set the default starting position (instantly) ---
            original_speed = self.speed()    # Save original speed
            self.speed(0)                    # Set to instant
            self.penup()
            super().goto(self._origin_x, self._origin_y) # Move to *absolute* start
            self.pendown()
            self.speed(original_speed)       # Restore original speed

        # --- Private Helper Methods ---
        
        def _to_absolute(self, x, y):
            """Converts student's relative (x, y) to absolute canvas coordinates."""
            return (x + self._origin_x, y + self._origin_y)

        def _to_relative(self, x, y):
            """Converts absolute canvas (x, y) to student's relative coordinates."""
            return (x - self._origin_x, y - self._origin_y)

        # --- Overridden Position & Movement Methods ---

        def goto(self, x, y):
            """Moves the turtle to a (student) coordinate."""
            abs_x, abs_y = self._to_absolute(x, y)
            super().goto(abs_x, abs_y)
        
        def setposition(self, x, y=None):
            """Alias for goto."""
            # This handles the case where setposition is called with one arg (a tuple)
            # or two args (x, y). Standard turtle behavior.
            if y is None:
                try:
                    x, y = x
                except TypeError:
                    # Handle error or just pass to goto to raise it
                    pass
            self.goto(x, y)

        def setx(self, x):
            """Sets the turtle's (student) x coordinate."""
            abs_x = x + self._origin_x
            super().setx(abs_x)

        def sety(self, y):
            """Sets the turtle's (student) y coordinate."""
            abs_y = y + self._origin_y
            super().sety(abs_y)

        def position(self):
            """Returns the turtle's (student) position."""
            abs_x, abs_y = super().position()
            return self._to_relative(abs_x, abs_y)
        
        def pos(self):
            """Alias for position."""
            return self.position()

        def xcor(self):
            """Returns the turtle's (student) x coordinate."""
            abs_x = super().xcor()
            return abs_x - self._origin_x

        def ycor(self):
            """Returns the turtle's (student) y coordinate."""
            abs_y = super().ycor()
            return abs_y - self._origin_y
        
        turtle.Turtle = Turtle          # This puts the class in the fame module
        sys.modules["turtle"] = turtle  # This allows "import turtle" to work. 
        
    # 3. Create a Canvas for the turtle to draw on
    myCanvas = Canvas(width=canvas_width, height=canvas_height)

    # 4. Display the Canvas in the Jupyter notebook
    display(myCanvas)

    # 5. Wait a moment to ensure the canvas is fully rendered
    time.sleep(time_sleep)

    # 6. Create a TurtleScreen
    myTS = TurtleScreen(myCanvas)
    myTS.clear()  # Clear the screen to start fresh
    
# Handle import errors gracefully
except ImportError:
    print("❌ Error: 'ipyturtle3' or 'IPython' not found.")
    print("Please make sure you are in a Jupyter environment and have")
    print("ipyturtle3 installed (e.g., `pip install ipyturtle3`).")
# Handle any other exceptions
except Exception as e:
    print(f"An error occurred during auto_turtle setup: {e}")