from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = WebDriver()

driver.get("https://www.makemytrip.com/")
_wait= WebDriverWait(driver,15)
_wait.until(ec.presence_of_element_located(("xpath","//span[@data-cy='closeModal']"))).click()

_wait = WebDriverWait(driver, 15)
_wait.until(ec.presence_of_element_located(("xpath", "//span[@class='chNavIcon appendBottom2 chSprite chHotels inactive']"))).click()

_wait = WebDriverWait(driver,15)
_wait.until(ec.presence_of_element_located(("xpath", "//button[text()='Search']"))).click()
sleep(3)
names = driver.find_elements("xpath", "//span[@class='wordBreak appendRight10']")
sleep(3)
prices = driver.find_elements("xpath", "//p[@id='hlistpg_hotel_shown_price']")
sleep(3)
name_list = [name.text for name in names]
sleep(3)
price_list = [price.text for price in prices]
sleep(3)
name_price_pair = {name:price for name,price in zip(name_list,price_list)}

print(name_price_pair)
