# Reference recipe.html for instructions
from tkinter import messagebox, simpledialog, Tk


window = Tk()
window.withdraw()


age = simpledialog.askinteger(None, "How old are you?")  # ;

for i in range(age):  # ;
    print("In " + str(2023 - i) + ", I was " + str(age - i) + " years old.")  # ;

window.mainloop()  # ;


# OR:  # ;

# for i in range(age):  # ;
#     messagebox.showinfo(  # ;
#         None, "In " + str(2020 - i) + ", I was " + str(age - i) + " years old."  # ;
#     )  # ;
