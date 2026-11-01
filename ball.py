from turtle import Turtle


# Create the ball class
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('ball.gif')
        self.penup()

        # Set initial movement values
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Move the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce the ball vertically
    def bounce_y(self):
        self.y_move *= -1

    # Bounce the ball horizontally
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Reset the ball to the center
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed *= 0.1
        self.bounce_x()