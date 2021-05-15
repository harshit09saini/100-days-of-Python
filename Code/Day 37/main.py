# Habit Tracker

import requests
import datetime as dt

# Create user

USER_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "harshitsainiii"
TOKEN = "jhsakjkshfdsf"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create_user_response = requests.post(url=USER_ENDPOINT, json=user_params)
#
# print(create_user_response.text)

# Create Graph

GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{USERNAME}/graphs"
GRAPH_ID = "graph-reading1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Reading",
    "unit": "pages",
    "type": "int",
    "color": "ichou",
}

header = {
    "X-USER-TOKEN": TOKEN
}
# graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=header)
#
# print(graph_response.text)

# Create Pixel

PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"

now = dt.datetime.now()
formatted_date = now.strftime("%Y%m%d")

pixel_params = {
    "date": formatted_date,
    "quantity": "10",
}
pixel_response = requests.post(
    url=PIXEL_ENDPOINT, json=pixel_params, headers=header)
print(pixel_response.text)

# Update pixel

pixel_update_response = requests.put(
    url=f"{PIXEL_ENDPOINT}/{formatted_date}", json={"quantity": "10"}, headers=header)
print(pixel_update_response.text)
