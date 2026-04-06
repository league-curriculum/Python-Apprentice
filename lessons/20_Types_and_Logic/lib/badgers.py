import tkinter as tk
from tkinter import PhotoImage
from pathlib import Path

class FizzBuzzer():

    """Run a user defined function on a sequence of numbers and display the result in a Tkinter window"""

    def __init__(self):
        self.current_number = 0


        
    # Function to update the display based on the current number
    def update_display(self):

        result = self.cb(self.current_number)

        def isnumber(x):
            try:
                int(x)
                return True
            except:
                return False

        if result == 'snake':
            self.display_label.config(image=self.snake_img)
            self.display_label.image = self.snake_img
        elif result == 'badger':
            self.display_label.config(image=self.badger_img)
            self.display_label.image = self.badger_img
        elif result == 'mushroom':
            self.display_label.config(image=self.both_img)
            self.display_label.image = self.both_img
        elif not isnumber(result):
            self.display_label.config(text=result, image='', fg='red')
        else:
            self.display_label.config(text=result, image='', fg='black')
        
        self.current_number+= 1

    def __init__(self, cb=None):

        self.cb=cb

        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.title("FizzBuzz with Tkinter")

        self.root.geometry("300x300")

        # Load images
        image_dir = Path(__file__).parent / 'images'


        self.snake_img = PhotoImage(file=image_dir/"snake.gif")
        self.badger_img = PhotoImage(file=image_dir/"badger.gif")
        self.both_img = PhotoImage(file=image_dir/"mushroom.gif")  # Create a combined image for both

        # Create label to display the result
        self.display_label = tk.Label(self.root, font=("Helvetica", 48))

        # Create button to update the display
        next_button = tk.Button(self.root, text="Next", command=self.update_display, font=("Helvetica", 24))

        # Configure the display label to be at the top
        self.display_label.pack(side=tk.TOP)

        # Configure the next button to be at the bottom
        next_button.pack(side=tk.BOTTOM)

        self.current_number = 1

    def run(self):
        self.root.mainloop()