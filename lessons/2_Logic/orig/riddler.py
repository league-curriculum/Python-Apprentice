"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got correct
"""

from tkinter import messagebox, simpledialog, Tk


window = Tk()
window.withdraw()


correct_answers = 0  # ;

riddle_question = "Why did the bike fall to the ground?"  # ;
riddle_answer = "two tired"  # ;

answer = simpledialog.askstring(None, riddle_question)  # ;

if answer is not None:  # ;
    if "two" in answer.lower() and "tired" in answer.lower():  # ;
        messagebox.showinfo(None, "Correct!")  # ;
        correct_answers += 1  # ;
    else:  # ;
        messagebox.showinfo(  # ;
            None,
            f"Incorrect! It fell over because it was {riddle_answer.upper()}!",  # ;
        )  # ;
else:  # ;
    messagebox.showinfo(None, "You didn't answer the riddle!")  # ;


# Repeat the above code for at least two more riddles  # ;

# Call the mainloop method
window.mainloop()  # ;

# Tell the user how many riddles they got correct
messagebox.showinfo(None, f"You got {correct_answers} riddles correct!")  # ;
