from tkinter import messagebox, simpledialog, Tk

# Create a new window variable, window = Tk()
window = Tk()  # ;

# Hide the window using the window's .withdraw() method
window.withdraw()  # ;

# Put this sentence in a pop-up message box:
# "If you find yourself having to cross a piranha-infested river, here's how to do it..."

prompt = "If you find yourself having to cross a   piranha-infested river, here's how to do it..."  # ;
messagebox.showinfo(message=prompt)  # ;

# This next section of code asks the player to provide certain words to complete the story, and saves their input to variables.  The 1st variable has been created for you.
# Get the player to enter an adjective
adjective = simpledialog.askstring(None, prompt="Enter an adjective")  # ;

# Get the player to enter a type of liquid
liquid = simpledialog.askstring(None, prompt="Enter a liquid")  # ;

# Get the player to enter a body part
bodyPart = simpledialog.askstring(None, prompt="Enter a body part")  # ;

# Get the player to enter a verb
verb = simpledialog.askstring(None, prompt="Enter a verb")  # ;

# Get the player to enter a place
place = simpledialog.askstring(None, prompt="Enter a place")  # ;

# The story below has has been written as a group of Strings concatinated (joined) using f-strings.
# The story contains place holder variables, indicated by ** ** which will be replaced by the values entered by the player.
# Hint:  You will need to add more {} signs to join the variables to the other parts of the story.  The 1st {} is already there.
story = (
    f"Piranhas are more {adjective} during the day, so cross the river at\n"  # Add Adjective
    f"night. Piranhas are attracted to fresh ** ** and will most\n"  # Add Liquid
    f"likely take a bite out of your ** ** if you ** **. Whatever\n"  # Add Liquid, Body Part, Verb
    f"you do, if you have an open wound, try to find another way to get "
    f"back to the ** **. Good luck!"  # Add Place
)
story2 = (  # ;
    f"Piranhas are more {adjective} during the day, so cross the river at\n"  # ;
    f"night. Piranhas are attracted to fresh {liquid} and will most\n"  # ;
    f"likely take a bite out of your {bodyPart} if you {verb}. Whatever\n"  # ;
    f"you do, if you have an open wound, try to find another way to get "  # ;
    f"back to the {place}. Good luck!"  # ;
)  # ;


# Make a pop-up that contains the final story. The \n escape characters add line breaks to the story.
# If you need to, move them around to make your story look better in the pop-up. Hint: Use messageboxes.showinfo()
messagebox.showinfo(message=story2)  # ;

# If you want to write your own Madlib story, just change the story variable and ask the player different questions.

# Run the window's .mainloop() method
window.mainloop()  # ;
