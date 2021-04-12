from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_forward_distance = STARTING_MOVE_DISTANCE
        for _ in range(20):
            self.generate_car()
            rand_x = random.randint(-280, 280)
            rand_y = random.randint(-230, 230)
            self.new_car.goto(rand_x, rand_y)
            self.cars.append(self.new_car)

    def generate_car(self):
        self.new_car = Turtle("square")
        self.new_car.penup()
        self.new_car.setheading(180)
        self.new_car.shapesize(stretch_wid=1, stretch_len=2)
        self.new_car.color(random.choice(COLORS))

    def random_car(self):
        self.generate_car()
        rand_y = random.randint(-230, 230)
        self.new_car.goto(280, rand_y)
        self.cars.append(self.new_car)

    def move(self):
        for car in self.cars:
            current_xcor = car.xcor()
            new_xcor = current_xcor - self.move_forward_distance
            car.goto(new_xcor, car.ycor())

    def increase_speed(self):
        self.move_forward_distance += MOVE_INCREMENT