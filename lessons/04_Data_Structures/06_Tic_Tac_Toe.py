#imports
from guizero import App, Box, PushButton, Text

# Functions
def clear_board():
    new_board = [[None, None, None], 
                 [None, None, None], 
                 [None, None, None]]
    # generate a 3x3 grid
    for x in range(3):
        for y in range(3):
            button = PushButton(
                board, text='', grid=[x, y], width=3, command=choose_square, args=[x,y])
            new_board[x][y] = button
    return new_board

def choose_square(x, y):
    board_square[x][y].text = turn
    board_square[x][y].disable()
    take_turns()
    check_win()

def take_turns():
    
    global turn

    if turn == "x":
        turn = "o"
    else:
        turn = "x"

    message.value = "It's your turn, " + turn

def check_win():
    winner = None

    # vertical lines
    if(
        board_square[0][0].text == board_square[0][1].text == board_square[0][2].text
    ) and board_square[0][2].text in ["X", "O"]:
        winner = board_square[0][0]
    elif (
        board_square[1][0].text == board_square[1][1].text == board_square[1][2].text
    ) and board_square[1][2].text in ["X", "O"]:
        winner = board_square[1][0]
    elif (
        board_square[2][0].text == board_square[2][1].text == board_square[2][2].text
    ) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[2][0]

    # horizontal
    elif (
        board_square[0][0].text == board_square[1][0].text == board_square[2][0].text
    ) and board_square[2][0].text in ["X", "O"]:
        winner = board_square[0][0]
    elif (
        board_square[0][1].text == board_square[1][1].text == board_square[2][1].text
    ) and board_square[2][1].text in ["X", "O"]:
        winner = board_square[0][1]   
    elif (
        board_square[0][2].text == board_square[1][2].text == board_square[2][2].text
    ) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[0][2]  

    # diagonals
    elif (
        board_square[0][0].text == board_square[1][1].text == board_square[2][2].text
    ) and board_square[2][2].text in ["X", "O"]:
        winner = board_square[0][0]   
    elif (
        board_square[2][0].text == board_square[1][1].text == board_square[0][2].text
    ) and board_square[0][2].text in ["X", "O"]:
        winner = board_square[0][2]  

    if winner is not None:
        message.value = winner.text + " wins!"
    elif moves_taken() == 9:
        message.value = "It's a tie🤝🤝"
        disable_buttons()

def moves_taken():
    moves = 0
    for row in board_square:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves = moves + 1
    return moves 

def reset_game():
    global turn
    turn = "X"
    message.value = "It's your turn, " + turn
    for row in board_square:
        for col in row:
            col.text = ""
            col.enable()

def disable_buttons():
    for row in board_square:
        for col in row:
            col.disable()


# Variables
turn = "X"

# App
app = App('Tic Tac Toe Game', bg='burlywood')
board = Box(app, layout='grid') # Create the board        
board_square = clear_board()
message = Text(app, text="It is your turn, " + turn)
message.text_color = "green"

# Display app
app.display()
