from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 15, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()
        self.store_highscore()

    def read_highscore(self):
        with open("highscore.txt") as highscore_file:
            self.highscore = int(highscore_file.read())

    def store_highscore(self):
        with open("highscore.txt", mode="w") as highscore_file:
            highscore_file.write(str(self.highscore))
