from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over. Final Score: {self.score}", False, align=ALIGNMENT, font=FONT)
