# Reference recipe.html for instructions
song = ""  # ;

for verse in range(2):  # ;
    if verse == 1:  # ;
        song += "\n\n"  # ;

    for i in range(14):  # ;
        if i == 11:  # ;
            song += "Badger\n"  # ;
        elif i == 12:  # ;
            song += "Mushroom, "  # ;
        elif i == 13:  # ;
            song += "Mushroom, "  # ;
        else:  # ;
            song += "Badger, "  # ;
else:  # ;
    song += "\nA snake!"  # ;

print(song)  # ;
