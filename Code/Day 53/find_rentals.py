import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:\\Program Files (x86)\\chromedriver.exe"

LOCATION = "San Francisco, CA"


class FindRentals:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=path)
        self.driver.get("https://www.zillow.com/homes/for_rent/")
        self.driver.maximize_window()
        self.price = []
        self.address = []
        self.links = []

    def find_rentals(self):
        location = self.driver.find_element_by_css_selector("input[aria-label='Search: Suggestions appear below']")
        location.send_keys(Keys.CONTROL + "a")
        location.send_keys(Keys.DELETE)
        time.sleep(1)
        location.send_keys(LOCATION)
        time.sleep(2)
        location.send_keys(Keys.ENTER)
        time.sleep(2)
        price = self.driver.find_element_by_xpath('//*[@id="price"]')
        price.click()
        time.sleep(1)
        price_max = self.driver.find_element_by_css_selector('#price-exposed-max')
        price_max.click()
        self.driver.find_element_by_css_selector('li#max-3000 button').click()
        self.scrape_data()
        next_page = self.driver.find_element_by_css_selector("a[title='Next page']")

        if next_page:
            for _ in range(1, 5):
                next_page.click()
                self.scrape_data()
        self.driver.close()

    def scrape_data(self):
        time.sleep(3)
        rentals = self.driver.find_elements_by_css_selector(
            ".list-card.list-card-additional-attribution.list-card_not-saved")
        for rental in rentals:
            price = rental.find_element_by_css_selector(
                'div.list-card-info > div.list-card-heading > div.list-card-price').text
            address = rental.find_element_by_css_selector(
                'div.list-card-info > a.list-card-link > address').text
            link = rental.find_element_by_css_selector(
                'div.list-card-info > a.list-card-link').get_attribute("href")
            print(price)
            print(address)
            print(link)
            self.price.append(price)
            self.address.append(address)
            self.links.append(link)
