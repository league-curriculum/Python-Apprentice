from tkinter import messagebox, simpledialog, Tk

# Create a new window variable, window = Tk()
window = Tk()  # ;

# Hide the window using the window's .withdraw() method
window.withdraw()  # ;

# Ask the user for their name and save it to a variable
# name = simpledialog.askstring(title='Greeter', prompt="What is your name?")
name = simpledialog.askstring(title="Question", prompt="What is your name?")  # ;

# Show a message box with your message using the .showinfo() method
messagebox.showinfo(message="Hello " + name + "!!!")  # ;

# Print your message to the console using the print() function
print("Hello " + name + "!!!!")  # ;

# Optional: show an error message using messagebox.showerror()
messagebox.showerror("err", "Run " + name + " , run!!!!")  # ;

# Run the window's .mainloop() method
window.mainloop()  # ;
