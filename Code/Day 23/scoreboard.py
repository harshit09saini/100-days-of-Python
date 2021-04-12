from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", font=FONT)

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def new_level(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", align="center", font=FONT)