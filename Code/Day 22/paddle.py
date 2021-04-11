from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(pos)

    def up(self):
        if self.ycor() < 250:
            self.forward(20)

    def down(self):
        if self.ycor() > -250:
            self.backward(20)
