from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from re import findall
driver = WebDriver()

driver.get("https://www.flipkart.com/")
sleep(3)
elements = driver.find_elements("xpath", "//div[@class='_1ZMrY_']//a")
driver.minimize_window()
for e in elements:
    print(e.get_attribute("href"))


