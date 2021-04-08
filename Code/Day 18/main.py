import turtle as t
import random
import colorgram

turtle = t.Turtle()
# Sets the colormode to use the rgb and use values from 0 to 255
t.colormode(255)
screen = t.Screen()
turtle.speed("fastest")


def extract_colors():
    # Uses the colorgram module to extract colors from an image and return a list of rgb values
    colors = colorgram.extract('hirst.jpg', 40)
    colors_list = []

    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors_list.append((r, g, b))


extracted_colors = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
                    (39, 105, 157),
                    (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90),
                    (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
                    (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
                    (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]


# Function to generate the hirst painting


def hirst():
    screen.bgcolor("mint cream")

    t.setworldcoordinates(-1, -1, 10, 10)
    turtle.hideturtle()

    def draw_row():
        for i in range(10):
            turtle.dot(15, random.choice(extracted_colors))
            turtle.penup()
            turtle.forward(1)
            turtle.pendown()

    for row in range(10):
        turtle.penup()
        turtle.goto(0, row)
        turtle.pendown()
        draw_row()


# hirst()

###########################################################################

def fractal_tree():
    screen.bgcolor("light blue")
    turtle.color("dark green")
    turtle.speed("fastest")
    turtle.pensize(2)

    turtle.penup()
    turtle.setpos(0, -300)
    turtle.pendown()

    length = 200
    turtle.setheading(90)

    def draw(branch_len):
        angle = 30
        if branch_len < 4:
            return
        else:
            turtle.pensize(round(branch_len * 0.05))
            turtle.forward(branch_len)
            turtle.right(angle)
            draw(branch_len * 0.67)
            turtle.left(angle*2)
            draw(branch_len * 0.67)
            turtle.right(angle)
            turtle.backward(branch_len)
            turtle.hideturtle()

    draw(length)


fractal_tree()


###########################################################################

# Random color using RGB tuples


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def spirograph():
    screen.screensize(2000, 1500)
    screen.bgcolor("black")
    angle = 0
    while angle <= 360:
        turtle.color(random_color())
        turtle.circle(150)
        angle += 1
        turtle.setheading(angle)


colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
          "SeaGreen"]
directions = [0, 90, 180, 270]


###########################################################################


def random_walk():
    for _ in range(200):
        turtle.color(random_color())
        left_right_random = random.randint(0, 1)
        turtle.forward(random.randint(0, 50))
        if left_right_random == 1:
            turtle.right(random.choice(directions))
        else:
            turtle.left(random.choice(directions))
        turtle.forward(random.randint(0, 50))


###########################################################################


def shape(sides):
    sides = sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)
    for i in range(sides):
        turtle.forward(100)
        turtle.left(360 / sides)


# for i in range(3, 11):
#     turtle.color(random.choice(colors))
#     shape(i)

screen.exitonclick()
