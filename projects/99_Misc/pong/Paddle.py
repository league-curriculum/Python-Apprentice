class Paddle():
    def __init__(self, x, y=None, paddle_width=100, paddle_height=20):
        self.x = x
        self.y = height - paddle_height
        self.width = paddle_width
        self.height = paddle_height
        self.x_speed = 0
        
        if y is not None:
            self.y = y
        
    def update(self):
        if (self.x + self.x_speed >= 0) and (self.x + self.x_speed <= width - self.width):
            self.x += self.x_speed
        
    def draw(self):
        push()
        fill(255)
        rect(self.x, self.y, self.width, self.height)
        pop()
