# Automated Birthday Wisher

##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
import datetime as dt
import pandas
import smtplib

# Read CSV file to get birthdays

df = pandas.read_csv("birthdays.csv")

birthdays_list = df.to_dict(orient="records")

# Get a random letter
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
rand_letter = random.choice(letters)

with open(f"letter_templates/{rand_letter}") as letter_file:
    letter_content = letter_file.readlines()


# Send Email Function
def send_email(message, receiver_email, name):
    my_email = ""
    password = ""

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Happy Birthday, {name}\n\n{message}")


# Get date and time

now = dt.datetime.now()
year_now = now.year
month_now = now.month
day_now = now.day
for birthday in birthdays_list:
    birthday_year = birthday["year"]
    birthday_month = birthday["month"]
    birthday_day = birthday["day"]

    if month_now == birthday_month and day_now == birthday_day:
        letter_content[0] = letter_content[0].replace(
            "[NAME]", birthday["name"])

        message_to_send = """"""
        for line in letter_content:
            message_to_send += line

        email = birthday["email"]
        name = birthday["name"]
        send_email(name=name, message=message_to_send, receiver_email=email)
