from tkinter import messagebox, simpledialog, Tk

# Make a new window variable, window = Tk()
window = Tk()  # ;

# Hide the window using the window's .withdraw() method
window.withdraw()  # ;

# 1. Create a variable to hold the user's score. Set it equal to zero.
score = 0  # ;

response = simpledialog.askstring(None, "Which is better, Python or Java?")  # ;

if response.lower() == "python":  # ;
    score += 1  # ;
    print("Correct! Your score is " + str(score))  # ;
else:  # ;
    score -= 1  # ;
    messagebox.showerror(message="WRONG! It's Python of course!")  # ;

messagebox.showinfo(message="Your final score is " + str(score))  # ;
# ASK A QUESTION AND CHECK THE ANSWER

# // 2. Ask the user a question

# // 3. Use an if statement to check if their answer is correct

# // 4. if the user's answer was correct, add one to their score

# MAKE MORE QUESTIONS. Ask more questions by repeating the above
# // Option: Subtract a point from their score for a wrong answer

# After all the questions have been asked, tell the user their final score
# remember to convert your score variable to a string using the str() function


score = 0  # ;

questions = [  # ;
    "Which is better, Python or Java?",  # ;
    "What does OOP stand for?",  # ;
    "How many days in a non-leap year?",  # ;
]  # ;

answers = ["python", "object orientated programming", "366"]  # ;

# Loop through each question in the questions list and ask the user for their response to each one using the simpledialog.askstring() method and an if statement to check if their response is correct or not and change the score accordingly using the score variable you created earlier.  # ;
for i in range(len(questions)):  # ;
    response = simpledialog.askstring(None, questions[i])  # ;

    if response.lower() == answers[i]:  # ;
        score += 1  # ;
        print("Correct! Your score is " + str(score))  # ;
    else:  # ;
        score -= 1  # ;
        messagebox.showerror(message="WRONG! It's " + answers[i] + " of course!")  # ;

messagebox.showinfo(message="Your final score is " + str(score))  # ;

# Run the window's .mainloop() method
window.mainloop()  # ;
