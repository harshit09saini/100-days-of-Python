
from get_internet_speed import GetInternetSpeed
from tweet_speed import Tweet

get_internet_speed = GetInternetSpeed()

get_internet_speed.get_speed()
download_speed = get_internet_speed.download
upload_speed = get_internet_speed.upload

tweet_body = f"hey @excitel_rocks, why is my internet speed {download_speed}down\{upload_speed}up when I pay for 300Mbps??? "
tweet_speed = Tweet(tweet_body)

tweet_speed.tweet_speed()

