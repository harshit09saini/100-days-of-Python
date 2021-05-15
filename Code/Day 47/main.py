# Amazon Price Tracker

import requests
from bs4 import BeautifulSoup
import smtplib


AMAZON_PRODUCT = "https://www.amazon.in/Canon-EOS-200D-II-55-250mm/dp/B07S26X16N/ref=lp_1389177031_1_6"
LOWEST_PRICE = 50000

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
amazon_response = requests.get(AMAZON_PRODUCT, headers=header)
amazon_response.raise_for_status()

soup = BeautifulSoup(amazon_response.content, "html.parser")

price = soup.find("span", {"id": "priceblock_ourprice"}
                  ).getText().split("\xa0")[1]
title = soup.find("span", {"id": "productTitle"}).getText().strip()

price = float(price.replace(",", ""))

# Send email

my_email = ""
password = ""

if price < LOWEST_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        message_body = f"SUBJECT: Low Price Alert - Amazon\n\n{title} is only {price}. Buy Now!"
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=message_body)
