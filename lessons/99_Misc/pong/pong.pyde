"""
Create a single player Pong game
"""
from Ball import Ball
from Paddle import Paddle

def setup():
    # 1. Set the size of your window to at least width = 800, height = 600
    size(800, 600)

    # 2. Make a global ball variable, for example:
    #    global ball
    global ball
    
    # 3. Initialize your ball variable to a new Ball(), for example:
    #    ball = Ball(x_position, y_position)
    ball = Ball(width/2, 0)
    
    # 4. Make a global paddle variable.
    global paddle
    
    # 5. Initialize your paddle variable to a new Paddle() for example:
    #    paddle = Paddle(x_position)
    paddle = Paddle(400)

    
def draw():
    # 6. Use the background() function to set the background color.
    background(0)

    # 7. Call the ball object's update() and draw() methods.
    #    Do you see the ball moving on the screen?
    ball.update()
    ball.draw()
    
    # 8. Call the paddle object's update() and draw() methods.
    #    Do you see the paddle on the screen?
    paddle.update()
    paddle.draw()

    # 11. Finish the code in keyPressed() and keyReleased() first!
    #     Call the ball boject's collision() method and pass the
    #     paddle object as an input variable.
    #     Does the ball bounce off the paddel?
    ball.collision(paddle)

    # 12. End the game when the ball goes below the bottom of the screen.
    #     You can use noLoop() to freeze the game and text() to print text
    #     on the screen.
    if ball.y > height:
        noLoop()


    # *EXTRA*
    # Can you figure out how to make a 2 player pong game with paddles on
    # the left and right on the screen?


# 9. Change paddle.x_speed when the LEFT or RIGHT arrow keys are pressed.
#    Does the paddle move?
def keyPressed():
    if key == CODED:
        if keyCode == LEFT:
            paddle.x_speed = -10
        elif keyCode == RIGHT:
            paddle.x_speed = 10

# 10. Set paddle.x_speed to 0 when the LEFT or RIGHT arrow keys are released.
#     Does the paddle stop when the keys are released?
def keyReleased():
    if key == CODED:
        if keyCode == LEFT or keyCode == RIGHT:
            paddle.x_speed = 0
