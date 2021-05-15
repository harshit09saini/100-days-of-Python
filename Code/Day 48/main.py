# COOKIE CLICKER AUTOMATOR

from selenium import webdriver
import time

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=PATH)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.maximize_window()
cookie = driver.find_element_by_css_selector('#bigCookie')

time.sleep(5)
driver.find_element_by_css_selector(".cc_btn.cc_btn_accept_all").click()
timeout = time.time() + 5  # 5 sec from now
timeout_five_mins = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        unlocked = []
        products = driver.find_elements_by_css_selector(".product.unlocked.enabled")

        for product in products:
            price = product.find_element_by_css_selector(".content .price").text
            if "," in price:
                price = price.replace(",", "")
            price = int(price)

            title = product.find_element_by_css_selector(".content .title").text
            product_id = product.get_attribute("id")
            unlocked.append({"id": product_id, "title": title, "price": price})

        money_element = driver.find_element_by_id("cookies").text.split(" ")[0]
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)
        affordable_items = {}
        for item in unlocked:
            if cookie_count > item["price"]:
                affordable_items[item["price"]] = item["id"]

        try:
            highest_affordable = max(affordable_items)
        except ValueError:
            continue
        to_buy = affordable_items[highest_affordable]
        print(f"buying {to_buy}")
        driver.find_element_by_css_selector(f".product.unlocked.enabled#{to_buy}").click()
        timeout = time.time() + 5

        if time.time() > timeout_five_mins:
            current_cookies = driver.find_element_by_id("cookies").text
            print(f"Current Cookies: {current_cookies}")
            break

driver.quit()
