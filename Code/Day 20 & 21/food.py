from turtle import Turtle
import random

SCALE_FOOD = 0.5
SPAWN_AREA = 330
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.penup()
        self.shapesize(stretch_wid=SCALE_FOOD, stretch_len=SCALE_FOOD)
        self.spawn()

    def spawn(self):
        rand_x = random.randint(-SPAWN_AREA, SPAWN_AREA)
        rand_y = random.randint(-SPAWN_AREA, SPAWN_AREA)
        self.goto(rand_x, rand_y)

    def walk(self):
        directions = [RIGHT, UP, LEFT, DOWN]
        self.forward(10)
        self.setheading(random.choice(directions))
        self.forward(10)
        if self.xcor() > SPAWN_AREA:
            self.setheading(LEFT)
        elif self.xcor() < -SPAWN_AREA:
            self.setheading(RIGHT)
        elif self.ycor() < -SPAWN_AREA:
            self.setheading(UP)
        elif self.ycor() > SPAWN_AREA:
            self.setheading(DOWN)
