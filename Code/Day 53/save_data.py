import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\Program Files (x86)\\chromedriver.exe"
FORM_URL = ""


class SaveData:
    def __init__(self, prices, addresses, links):
        self.prices = prices
        self.addresses = addresses
        self.links = links
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get(FORM_URL)
        self.fill_form()

    def fill_form(self):

        for price, address, link in zip(self.prices, self.addresses, self.links):
            address_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_field = self.driver.find_element_by_xpath(
                '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = self.driver.find_element_by_css_selector(
                'span.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel')

            address_field.send_keys(address)
            price_field.send_keys(price)
            link_field.send_keys(link)
            submit_button.click()
            self.driver.find_element_by_link_text(
                'Submit another response').click()
            time.sleep(0.5)
