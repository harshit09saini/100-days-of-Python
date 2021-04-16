import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("India States Game")
# screen.setup(1000, 1200)
turtle = Turtle()

# Read csv file
data = pandas.read_csv("states.csv")

# Add a custom image
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

# Convert states column to a list
all_states = data["states"].to_list()

# Store all the correctly guessed states
guessed = []

# Keep track of the correctly guessed states
score = Turtle()
score.hideturtle()
score.penup()
score.goto(100, 200)

while len(guessed) < 36:
    score.clear()
    score.write(f"{len(guessed)}/36", font=("courier", 24, "bold"))

    # Take user input and convert it into title case
    user_answer = screen.textinput("Guess the State", "Name a state or UT: ").title()

    # Grabs the row of the user guessed state
    state_data = data[data["states"] == user_answer]

    # Exit condition
    if user_answer == "Exit":
        # Check all the guessed states and append missing states to the list
        # for state in all_states:
        #     if state not in guessed:
        #         missed.append(state)

        # Make the above code concise using list comprehension
        missed = [state for state in all_states if state not in guessed]
        print(missed)
        break

    # If user guess exists in the state list from csv
    if user_answer in all_states:
        new_state = Turtle()
        new_state.hideturtle()
        new_state.penup()
        x_pos = int(state_data.x)
        y_pos = int(state_data.y)
        new_state.setpos(x_pos, y_pos)
        new_state.write(user_answer, align="center")
        guessed.append(user_answer)

# Convert missing states to a csv file
pandas.DataFrame(missed).to_csv("States_to_learn.csv")

# MAP GAME ENDS
#################################################################################################
# Run this code to get a csv file with turtle screen coordinates for each state

# states = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh ',
#           'Assam', 'Bihar', 'Chandigarh','Chhattisgarh', 'Dadra and Nagar Haveli',
#           'Daman and Diu', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh',
#           'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep',
#           'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
#           'Nagaland', 'National Capital Territory of Delhi', 'Odisha', 'Puducherry',
#           'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura',
#           'Uttar Pradesh', 'Uttarakhand', 'West Bengal']
#
# x_coord = [178.0, -57.0, 216.0, 184.0, 62.0, -105.0, -9.0, -184.0, -187.0, -147.0, -191.0, -106.0, -90.0, -133.0,
# 50.0, -120.0, -106.0, -172.0, -80.0, -127.0, 202.0, 152.0, 184.0, 215.0, -94.0, 43.0, -46.0, -125.0, -160.0, 104.0,
# -72.0, -62.0, 158.0, -37.0, -56.0, 93.0]
#
# y_coord = [-234.0, -155.0, 103.0, 60.0, 45.0, 146.0, -39.0, -58.0, -76.0, -150.0, -3.0, 116.0, 175.0, 220.0, 6.0,
# -157.0, -236.0, -238.0, -1.0, -74.0, 26.0, 39.0, -3.0, 55.0, 102.0, -54.0, -212.0, 154.0, 69.0, 83.0, -226.0,
# -100.0, 9.0, 79.0, 140.0, -1.0]
#
# map_dict = {
#     "states": states,
#     "x": x_coord,
#     "y": y_coord,
# }
#
# pandas.DataFrame(map_dict).to_csv("states.csv")

# Function to get screen coordinates where cursor is clicked

# def get_mouse_click_coor(x, y):
#     x_coord.append(x)
#     y_coord.append(y)
#     print(x, y)
#
#
# turtle.onclick(get_mouse_click_coor)
#
# screen.mainloop()
#
# print(x_coord)
# print(y_coord)

############################################################

# Challenges
# data = pandas.read_csv("4.2 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#
# counts = data["Primary Fur Color"].value_counts()
# counts_list = counts.to_list()
# counts_dict = {
#     "fur_color": ["Gray", "Cinnamon", "Black"],
#     "count": counts_list,
# }
#
# new_data = pandas.DataFrame(counts_dict)
# new_data.to_csv("squirrel_count.csv")
# print(new_data)


# df = pandas.read_csv("2.1 weather_data.csv")
#
#
# temp_list = df["temp"].to_list()
# print(temp_list)
# max_temp = int(df["temp"].max())
# print(df[df["temp"] == max_temp])
