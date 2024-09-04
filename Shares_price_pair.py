from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()

driver.get("file:///C:/Users/Rudra/Desktop/Selenium/demo-html-20240826T064511Z-001/demo-html/demo.html")

price = driver.find_element("xpath", "//td[text()='AAPL']/..//td[@class='price']")
name = driver.find_element("xpath", "//td[text()='AAPL']")

while True:
    print(f"{price.text} : {name.text}")

