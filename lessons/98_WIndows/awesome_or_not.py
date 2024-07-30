from tkinter import messagebox, simpledialog, Tk
import random

# Make a new window variable, window = Tk()
window = Tk()  # ;

# Hide the window using the window's .withdraw() method
window.withdraw()  # ;

# 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
randNum = random.randint(0, 3)  # ;

# 2. Print your variable to the console
print(randNum)  # ;

# 3. Get the user to enter something that they think is awesome
response = simpledialog.askstring(  # ;
    None, prompt="What is something you think is awesome?"  # ;
)  # ;

# 4. If your variable is  0
if randNum == 0:  # ;
    # -- tell the user whatever they entered is awesome!
    message = "That is awesome!"  # ;

# 5. If your variable is  1
elif randNum == 1:  # ;
    # -- tell the user whatever they entered is ok.
    message = "Meh, that's ok I guess"  # ;

# 6. If your variable is  2
elif randNum == 2:  # ;
    # -- tell the user whatever they entered is boring.
    message = "That's pretty boring"  # ;

# 7. If your variable is  3
elif randNum == 3:  # ;
    # -- invent your own message to give to the user (be nice).
    message = "While I don't agree with you, I will defend to the death your right to say it."  # ;

# Run the window's .messagebox.showinfo() method with the message variable
messagebox.showinfo(message=message)  # ;

# Run the window's .mainloop() method
window.mainloop()  # ;
