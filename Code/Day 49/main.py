# Linkedin Job Automator
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\\Program Files (x86)\\chromedriver.exe"

USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASSWORD"

driver = webdriver.Chrome(executable_path=PATH)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/")
time.sleep(2)
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

time.sleep(2)
login_username = driver.find_element_by_xpath('//*[@id="username"]')
login_username.send_keys(USERNAME)
login_password = driver.find_element_by_xpath('//*[@id="password"]')
login_password.send_keys(PASSWORD)

login_password.send_keys(Keys.ENTER)

try:
    not_now = driver.find_element_by_xpath('//*[@id="remember-me-prompt__form-secondary"]/button')
except:
    print("No such element")
else:
    not_now.click()

time.sleep(5)

# Get Jobs
job_keyword = driver.find_element_by_xpath('//*[@aria-label="Search by title, skill, or company"]')
job_keyword.find_element_by_css_selector("input").send_keys("Python Developer")

location_keyword = driver.find_element_by_xpath('//*[@aria-label="City, state, or zip code"]')
location_keyword.find_element_by_css_selector("input").send_keys("Remote" + Keys.ENTER)

time.sleep(3)
easy_apply = driver.find_element_by_xpath('//*[@aria-label="Easy Apply filter."]').click()
time.sleep(3)
remote = driver.find_element_by_xpath('//*[@aria-label="Remote filter."]').click()
time.sleep(5)
# Loop through the jobs and apply

job_results = driver.find_elements_by_css_selector('.ember-view.job-card-container__link.job-card-list__title')
print(len(job_results))
for job in job_results:
    # job_card = job.find_element_by_css_selector(".jobs-search-results__list-item")
    job.click()
    time.sleep(2)
    # Write a function that applies for jobs and automate the easy apply procedure (skipping for now)

