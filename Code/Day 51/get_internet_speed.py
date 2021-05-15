import time
from selenium import webdriver

PATH = "C:\\Program Files (x86)\\chromedriver.exe"


class GetInternetSpeed:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=PATH)
        self.upload = None
        self.download = None

    def get_speed(self):
        self.driver.get("https://speedtest.net/")
        time.sleep(5)
        print("maximizing")
        self.driver.maximize_window()
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()

        time.sleep(60)

        self.download = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                          'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.upload = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                        'div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text