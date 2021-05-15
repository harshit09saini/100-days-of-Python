# Introduction to API Endpoints
# ISS Overhead Notifier
import smtplib
import time

import requests
import datetime as dt

MY_LAT = 28.650523
MY_LONG = 77.366307


def is_iss_overhead():
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data = response_iss.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT - 5 <= iss_longitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response_sun = requests.get(
        "https://api.sunrise-sunset.org/json", params=parameters)
    response_sun.raise_for_status()

    sun_time = response_sun.json()["results"]
    sunrise = int(sun_time["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_time["sunset"].split("T")[1].split(":")[0])

    hour_now = dt.datetime.now(dt.timezone.utc).hour

    if hour_now >= sunset and hour_now <= sunrise:
        return True


def send_mail():
    my_email = ""
    password = ""
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="",
                            msg="Subject:ISS CROSSING YOUR LOCATION NOW\n\nAye yo look up.")


while(True):
    print("Started")
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        send_mail()
    else:
        print("Not here yet. waittt, you'll get the mail")
