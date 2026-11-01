from turtle import Turtle


# Create the scoreboard
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        # Initialize both scores
        self.l_score = 0
        self.r_score = 0

        self.update_score()

    # Display the current scores
    def update_score(self):
        self.clear()

        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Arial", 20, 'bold'))

        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Arial", 20, 'bold'))

    # Increase the left player's score
    def l_point(self):
        self.l_score += 1
        self.update_score()

    # Increase the right player's score
    def r_point(self):
        self.r_score += 1
        self.update_score()