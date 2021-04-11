import time
from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

BGCOLOR = "snow"

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor(BGCOLOR)
screen.title("Pong")

is_game_on = False


def start_screen():
    global is_game_on
    start = Turtle()
    start.penup()
    start.hideturtle()
    start.color("dark slate blue")
    start.write("Welcome to Pong!", move=False, align="center", font=("Courier", 50, "bold"))
    # start_game = screen.textinput("Do you want to play Pong? ", "y/n ")
    time.sleep(3)
    is_game_on = True
    start.clear()
    # if start_game == "y":
    #     is_game_on = True
    #     start.clear()
    # else:
    #     screen.bye()


start_screen()

screen.tracer(0)

left_paddle = Paddle((-350, 0), "indigo")
right_paddle = Paddle((350, 0), "indigo")

ball = Ball()

screen.listen()

screen.onkeypress(left_paddle.up, "Up")
screen.onkeypress(left_paddle.down, "Down")
screen.onkeypress(right_paddle.up, "w")
screen.onkeypress(right_paddle.down, "s")

scoreboard = Scoreboard()

while is_game_on:
    screen.update()
    time.sleep(0.065)

    ball.move()

    # if right_paddle.ycor() > -250

    # Detect collision with top and bottom wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(right_paddle) <= 50 and ball.xcor() >= 330 or \
            ball.distance(left_paddle) <= 50 and ball.xcor() <= -330:
        ball.bounce_x()
        ball.increase_speed()

    # If the ball is missed, then increase the score
    if ball.xcor() > 410:
        ball.reset_game()
        scoreboard.increase_score_left()
        ball.xmove = 10
    if ball.xcor() < -410:
        ball.reset_game()
        scoreboard.increase_score_right()
        ball.xmove = 10

screen.exitonclick()
