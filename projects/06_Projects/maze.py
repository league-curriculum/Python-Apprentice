from mazelib import Maze
from mazelib.generate.Prims import Prims
from mazelib.generate.DungeonRooms import DungeonRooms
from dataclasses import dataclass
from guizero import App, Waffle
import numpy as np
from typing import List, Tuple
from mazelib.solve.BacktrackingSolver import BacktrackingSolver



def make_maze(x_size=15, y_size=15):
    """Generate the maze using the maze library"""
    m = Maze()
    m.generator =DungeonRooms(x_size, y_size, rooms=[[(3,3), (7,7)], [(21,21), (28,28)]])
    m.generate()
    m.generate_entrances()
    # copy the grid to a numpy array

    m.solver = BacktrackingSolver()
    print(m.solve())

    g = np.array(m.grid)
    
    g[m.start] = 0
    g[m.end] = 0

    return 2*x_size+1, 2*y_size+1, m, g

x_size, y_size, m, g = make_maze()

for p in m.solutions[0]:   
    g[p] = 4


dim = 11
pad = 0
w = (x_size+2)*(dim+pad)
h = (y_size+2)*(dim+pad)

def build_waffle(app, g, x_size, y_size, dim, pad):
    """Build the waffle grid based on the maze"""

    waffle = Waffle(app, width=x_size, height=y_size, dim=dim, pad=pad)
    waffle.set_all("black")  # Set initial grid to black

    colors = ['white', 'black', 'green', 'red', 'blue']

    for (x, y), value in np.ndenumerate(g):
            waffle.set_pixel(x, y, colors[value]) 
           

    # set the start to gree and the end to red
    waffle.set_pixel(*m.start, "green")
    waffle.set_pixel(*m.end, "red")


    return waffle

@dataclass
class Player:
    x: int
    y: int

    def move(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos(self):
        return self.x, self.y

    def __repr__(self):
        return f"Player({self.x}, {self.y})"




app = App("Maze Generator", width=w, height=h)

waffle = build_waffle(app, g, x_size, y_size, dim, pad)


player = Player(*m.start)

waffle.set_pixel(*player.pos, "yellow")  # Place the player

# Function to move the player
def move_player(event):
    
    new_x, new_y = player.pos
    key = event.tk_event.keysym

    if key == "Up":
        new_y -= 1
    elif key == "Down":
        new_y += 1
    elif key == "Left":
        new_x -= 1
    elif key == "Right":
        new_x += 1
    
    p = g[new_x][new_y]

    # Ensure the player stays within bounds and moves only on white spaces
    if 0 <= new_x < x_size and 0 <= new_y < y_size and p == 0:
        waffle.set_pixel(*player.pos, "white")  # Clear previous position
        waffle.set_pixel(new_x, new_y, "yellow")  # Move to new position
        player.move(new_x, new_y)

# Bind keys to move the player
app.when_key_pressed = move_player

app.display()
