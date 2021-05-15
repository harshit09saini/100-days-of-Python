# Rain Notifier

import requests
from twilio.rest import Client

API = ""
account_sid = ""
auth_token = ""

LATITUDE = 28.613939
LONGITUDE = 77.209023

parameters = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API,
    "exclude": "current,daily,minutely"
}

response = requests.get(
    f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()

weather_data = response.json()["hourly"][:12]

will_rain = False
\
for hour in weather_data:
    rain_id = hour["weather"][0]["id"]
    if int(rain_id) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='',
        body="It will rain today. Don't forget to bring an umbrella. ☔",
        to='+91-YOURNUMBER'
    )

    print(message.status)
