from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


# Instantiate Chrome
driver = webdriver.Chrome()

# Get Helb Website
driver.get("https://portal.helb.co.ke")

# Login
email = driver.find_element_by_css_selector('#logid')
pin.clear()
pin.send_keys('KRAPIN')
driver.find_element_by_css_selector(
    '#normalDiv > table > tbody > tr:nth-child(3) > td:nth-child(2) > a').click()
password = driver.find_element_by_css_selector('#xxZTT9p2wQ')
password.send_keys('KRAPASS')
