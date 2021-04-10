from turtle import Turtle
import random

SCALE_FOOD = 0.5


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.shapesize(stretch_wid=SCALE_FOOD, stretch_len=SCALE_FOOD)
        self.spawn()

    def spawn(self):
        rand_x = random.randint(-330, 330)
        rand_y = random.randint(-330, 330)
        self.goto(rand_x, rand_y)
