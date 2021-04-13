from turtle import Turtle

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270
SCALE_SEGMENT = 1
X_POS = 20
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

class Snake:

    def __init__(self, color):
        self.snake_segments = []
        # self.x_pos = 0
        self.color = color
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.speed("fastest")
        new_segment.shapesize(stretch_len=SCALE_SEGMENT, stretch_wid=SCALE_SEGMENT)
        new_segment.penup()
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    # Creates the initial snake with 3 segments

    def create_snake(self):
        for POSITION in POSITIONS:
            self.create_segment(POSITION)

    def increase_length(self):
        self.create_segment(self.snake_segments[-1].position())

    def reset(self):
        for segment in self.snake_segments:
            segment.goto(2000, 2000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_coord = self.snake_segments[segment - 1].pos()
            self.snake_segments[segment].goto(new_coord)
        self.head.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

