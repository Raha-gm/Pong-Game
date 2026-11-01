from turtle import Turtle


# Create a paddle class
class paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape('paddle.gif')
        self.penup()
        self.goto(position)

    # Move the paddle up
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    # Move the paddle down
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)