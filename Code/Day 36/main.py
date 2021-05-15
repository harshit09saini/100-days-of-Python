# Stock Trading News Alter
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = ""
STOCK_API = ""
SMS_AUTH = ""


def send_sms(text):
    account_sid = ''
    auth_token = SMS_AUTH
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        messaging_service_sid='',
        body=text,
        to='+91-YOURNUMBER'
    )

    print(f"Sent - {message.status}")


# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API,
}
stock_response = requests.get(STOCK_ENDPOINT, params=parameters)
stock_response.raise_for_status()
daily_data = stock_response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in daily_data.items()]
data_yesterday = data_list[0]
closing_price_yesterday = float(data_yesterday["4. close"])

data_day_before = data_list[1]
closing_price_day_before = float(data_day_before["4. close"])

price_difference = closing_price_yesterday - closing_price_day_before

up_down_emoji = None

if price_difference > 0:
    up_down_emoji = "📈"
else:
    up_down_emoji = "📉"

percent_diff = round(((price_difference / closing_price_yesterday) * 100), 2)

# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
parameters_news = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API,
}
news_response = requests.get(NEWS_ENDPOINT, params=parameters_news)
news_response.raise_for_status()
news_articles = news_response.json()["articles"]


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title  and description to your phone number.
if abs(percent_diff) > 4:
    for article in news_articles[:3]:
        article_title = article["title"]
        article_description = article["description"]

        formatted_article = f"{STOCK} - {up_down_emoji} {percent_diff}%\n" \
                            f"Headline: {article_title}\nBrief: {article_description}\n"
        send_sms(formatted_article)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
