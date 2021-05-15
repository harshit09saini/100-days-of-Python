# Bumble Automator
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://bumble.com/app")

driver.maximize_window()
time.sleep(2)
login = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[3]/form/div[3]/div/span/span/span').click()
number_input = driver.find_element_by_xpath('//*[@id="phone"]')
number_input.send_keys('YOUR NUMBER' + Keys.ENTER)

print("Waiting for OTP")
time.sleep(60)


like = driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span')

while True:
    like.click()
    print("Liked")
    time.sleep(3)
