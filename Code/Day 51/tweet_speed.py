import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

USERNAME = ""
PASSWORD = ""


class Tweet:
    def __init__(self, tweet):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.tweet = tweet

    def tweet_speed(self):
        self.driver.get("https://twitter.com/")
        time.sleep(1)
        self.driver.maximize_window()
        self.login()
        time.sleep(5)
        message_box = self.driver.find_element_by_css_selector(
            "div[class='public-DraftStyleDefault-block public-DraftStyleDefault-ltr'")
        message_box.send_keys(self.tweet)

        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]'
                                                         '/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div'
                                                         '/div/div[2]/div[3]/div/span/span').click()

    def login(self):
        # Login Functionality
        login = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]')
        login.click()
        username_input = self.driver.find_element_by_css_selector(
            "input[name='session[username_or_email]'")
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element_by_css_selector(
            "input[name='session[password]'")
        password_input.send_keys(PASSWORD + Keys.ENTER)
