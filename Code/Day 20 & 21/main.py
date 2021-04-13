from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

INNER_BOUNDARY = 345

screen = Screen()

# Set up the screen dimensions
screen.setup(width=700, height=700)

# Change the screen background color
screen.bgcolor("floral white")

# Stops updating screen automatically
screen.tracer(0)

# Create the snake instance
snake = Snake("maroon")

# Create the food instance
food = Food()

def quit_game():
    global is_game_on
    is_game_on = False
    screen.bye()

# Onscreen Key listeners to move the snake
screen.listen()
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(quit_game, "space")

# Create the scoreboard instance
scoreboard = Scoreboard()

# Determines the state of the game
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.spawn()
        scoreboard.increase_score()
        snake.increase_length()

    # Detect Collision with Walls
    if snake.head.xcor() > INNER_BOUNDARY or snake.head.xcor() < -INNER_BOUNDARY \
            or snake.head.ycor() > INNER_BOUNDARY or snake.head.ycor() < -INNER_BOUNDARY:
        scoreboard.reset()
        snake.reset()
        # scoreboard.game_over()
        # is_game_on = False

    # Detect Collision with Body
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            # scoreboard.game_over()
            # is_game_on = False

    # Increase the difficulty by making the food turtle move randomly
    if scoreboard.score > 10:
        food.walk()

screen.exitonclick()
