from turtle import Turtle
import time

BALLCOLOR = "maroon"


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shapesize(stretch_wid=0.6, stretch_len=0.6)
        self.penup()
        self.color(BALLCOLOR)
        self.shape("circle")
        self.xmove = 10
        self.ymove = 10

    def move(self):
        new_xcor = self.xcor() + self.xmove
        new_ycor = self.ycor() + self.ymove
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        self.ymove *= -1

    def bounce_x(self):
        self.xmove *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x()
        time.sleep(1)

    def increase_speed(self):
        self.xmove *= 1.1
