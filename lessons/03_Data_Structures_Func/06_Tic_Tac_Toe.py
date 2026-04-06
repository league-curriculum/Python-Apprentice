#imports
import pygame
import sys

X_MARK = "X"
O_MARK = "O"

# Implement check_row() and check_win() to allow the game to check if a player has won
# IMPORTANT! In your code, you should use the constants X_MARK and O_MARK instead of the strings "x" and "o"

def check_row(l):
    """Check if a player won on a row
    Args:
        l: a 3 element iterable
        
    Returns:
        The winner's token ( x or o ) if there is one, otherwise None
        """
    if all(e == l[0] and e != "" for e in l):
            return l[0]
    return None


def check_win(board):
    """Check if a player has won on a board
    Args:
        board: a 3x3 2D array
    
    Returns:
        The winner's token ( x or o ) if there is one, otherwise None
    """
    for row in board:
            winner = check_row(row)
            if winner:
                return winner

    for col in zip(*board):
        winner = check_row(col)
        if winner:
            return winner

    winner = check_row([board[i][i] for i in range(3)])
    if winner:
        return winner

    winner = check_row([board[i][2 - i] for i in range(3)])
    if winner:
        return winner

    return None
    

# The following code is the main part of the program. It creates a GUI for the
# game and handles the game logic. Implement the functions above first, then
# after your program is working you can try chaning the code below. 

class TicTacToe:
    """A Simple Tic Tac Toe game"""

    def __init__(self, win_func=check_win):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 400))
        pygame.display.set_caption('Tic Tac Toe Game')
        self.clock = pygame.time.Clock()
        
        self.win_func = win_func
        self.reset()

    def reset(self):
        """Reset the game state"""
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn_n = 0
        self.winner = None
        self.message = "It's your turn, " + self.current_turn

    @property
    def current_turn(self):
        """Return the current player's marker, based on the current turn number"""
        return [X_MARK, O_MARK][self.turn_n % 2]

    def draw(self):
        self.screen.fill((255, 222, 173))  # burlywood
        
        # Draw grid
        for i in range(1, 3):
            pygame.draw.line(self.screen, (0, 0, 0), (i * 100, 0), (i * 100, 300), 2)
            pygame.draw.line(self.screen, (0, 0, 0), (0, i * 100), (300, i * 100), 2)
        
        # Draw marks
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == X_MARK:
                    # Draw X
                    pygame.draw.line(self.screen, (0, 0, 0), (x*100 + 20, y*100 + 20), (x*100 + 80, y*100 + 80), 3)
                    pygame.draw.line(self.screen, (0, 0, 0), (x*100 + 80, y*100 + 20), (x*100 + 20, y*100 + 80), 3)
                elif self.board[x][y] == O_MARK:
                    # Draw O
                    pygame.draw.circle(self.screen, (0, 0, 0), (x*100 + 50, y*100 + 50), 30, 3)
        
        # Draw message (simple text without font)
        # For now, skip text, or use print
        print(self.message)  # Print to console
        
        # Draw reset button
        pygame.draw.rect(self.screen, (200, 200, 200), (100, 340, 100, 40))
        # No text for button
        
        pygame.display.flip()

    def handle_click(self, pos):
        x, y = pos
        if y < 300:  # board area
            cell_x = x // 100
            cell_y = y // 100
            if self.board[cell_x][cell_y] is None and self.winner is None:
                self.board[cell_x][cell_y] = self.current_turn
                self.turn_n += 1
                self.winner = self.win_func(self.board)
                if self.winner:
                    self.message = f"Player {self.winner} won!"
                elif self.turn_n == 9:
                    self.message = "It's a draw!"
                else:
                    self.message = f"It's your turn, {self.current_turn}"
        elif 100 <= x <= 200 and 340 <= y <= 380:  # reset button
            self.reset()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
            
            self.draw()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

ttt = TicTacToe(check_win)
ttt.run()
