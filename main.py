from turtle import *
from paddle import paddle
from ball import Ball
from scoreboard import Scoreboard
from winsound import *
import time

# Set up the game screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('background.gif')

# Register game shapes
screen.addshape('ball.gif')
screen.addshape('paddle.gif')

screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

# Create game objects
r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

# Start the game
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        PlaySound('wall.wav', SND_FILENAME | SND_ASYNC)

    # Detect collision with the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 335) or \
       (ball.distance(l_paddle) < 50 and ball.xcor() < -335):
        ball.bounce_x()
        PlaySound('paddle.wav', SND_FILENAME | SND_ASYNC)

    # Check if the ball goes past the right side
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Check if the ball goes past the left side
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()