# Workout Tracker

import requests
import datetime as dt
API_KEY = ""
APP_ID = ""
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 170
AGE = 20

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETS_ENDPOINT = "https://api.sheety.co/cbc529d238ca12e3e1d04ea9697cdd09/myWorkoutsPythonTest/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": "ran twenty miles and swam for 30 minutes",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

bearer_headers = {
    "Authorization": "Bearer randomaccesstokenforaccessinggooglesheetsbyharshitsaini"
}

response = requests.post(url=EXERCISE_ENDPOINT,
                         json=parameters, headers=headers)
response.raise_for_status()

exercise_data = response.json()["exercises"]

exercises_performed = []

now = dt.datetime.now()
date = now.strftime("%d/%m/%Y")
time = now.strftime("%H:%M:%S")

for exercise in exercise_data:
    exercise_dict = {
        "date": date,
        "time": time,
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"],
        "exercise": exercise["name"].title(),
    }
    exercises_performed.append(exercise_dict)

    body_to_send = {
        "workout": exercise_dict
    }
    sheet_response = requests.post(
        url=SHEETS_ENDPOINT, json=body_to_send, headers=bearer_headers)
    print(sheet_response.text)
