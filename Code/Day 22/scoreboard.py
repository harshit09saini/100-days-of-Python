from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "bold")
COLOR = "black"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color(COLOR)
        self.hideturtle()
        self.draw_center_line()
        self.penup()
        self.left_score()
        self.right_score()

    def draw_center_line(self):
        self.penup()
        self.goto(0, 300)
        self.pendown()
        self.pensize(3)
        self.setheading(270)

        for _ in range(16):
            self.forward(20)
            self.penup()
            self.forward(20)
            self.pendown()
        self.penup()

    def left_score(self):
        self.goto(-100, 200)
        self.write_score(self.score_left)

    def right_score(self):
        self.goto(100, 200)
        self.write_score(self.score_right)

    def write_score(self, score):
        self.write(f"{score}", move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.draw_center_line()
        self.left_score()
        self.right_score()

    def increase_score_left(self):
        self.score_left += 1
        self.update()

    def increase_score_right(self):
        self.score_right += 1
        self.update()
