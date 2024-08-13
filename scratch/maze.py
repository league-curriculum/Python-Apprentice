from random import shuffle, randrange
from guizero import App, Waffle

def make_maze(waffle, w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]  # 1 means visited
    ver = [["|  "] * w + ['|'] for _ in range(h)] + [[]]  # vertical walls
    hor = [["+--"] * w + ['+'] for _ in range(h + 1)]  # horizontal walls



    def walk(x, y):
        vis[y][x] = 1  # mark as visited

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]  # directions
        shuffle(d)  # randomize the order of directions
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue  # if visited, skip
            if xx == x:
                hor[max(y, yy)][x] = "+  "  # if horizontal, remove the horizontal wall
            if yy == y:
                ver[y][max(x, xx)] = "   "  # if vertical, remove the vertical wall
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    # Update the Waffle grid
    for y in range(h):
        for x in range(w):
            if vis[y][x]:
                waffle.set_pixel(x * 2, y * 2, "white")  # Open space
            if hor[y + 1][x] == "+  ":
                waffle.set_pixel(x * 2, y * 2 + 1, "white")  # Remove horizontal wall
            if ver[y][x + 1] == "   ":
                waffle.set_pixel(x * 2 + 1, y * 2, "white")  # Remove vertical wall

def main():
    app = App("Maze Generator", width=400, height=400)
    waffle = Waffle(app, width=32, height=16, dim=9, pad=0)
    waffle.set_all("black")  # Set initial grid to black
    make_maze(waffle)
    app.display()

if __name__ == '__main__':
    main()
