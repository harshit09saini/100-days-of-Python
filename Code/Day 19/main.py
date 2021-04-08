import turtle as tt
import random
screen = tt.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a Bet.", prompt="Which turtle will win the race? Make your guess: ")
# print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_pos = -125
for color in colors:
    turtle = tt.Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    turtle.setpos(x=-240, y=y_pos)
    turtles.append(turtle)
    y_pos += 50

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print("Your turtle won.")
            else:
                print(f"You lose. {winning_turtle} turtle won.")
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()