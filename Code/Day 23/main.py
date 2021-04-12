import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # When player reaches the top screen, proceed onto the next level

    if player.ycor() == 290:
        player.reset_level()
        scoreboard.new_level()
        car_manager.increase_speed()

    # Generate a random car at the right side of the screen every 5th loop.

    if loop_count % 5 == 0:
        car_manager.random_car()

    # Detect collision with a car

    for car in car_manager.cars:
        if player.distance(car) < 30:
            player.reset_level()
            scoreboard.game_over()
            game_is_on = False

    car_manager.move()
    loop_count += 1

screen.exitonclick()