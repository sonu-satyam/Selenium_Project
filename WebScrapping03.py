from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()

driver.get("https://www.nseindia.com/")
sleep(3)
stocks = driver.find_elements("xpath", "//div[@id='gainers_loosers']//td[1]")
sleep(3)
prices = driver.find_elements("xpath", "//div[@id='gainers_loosers']//td[2]")
sleep(3)
stock_price_pair = {stock.text:price.text for stock,price in zip(stocks,prices)}

with open ("demo123.csv", "w") as file:
    for key, value in stock_price_pair.items():
        file.writelines(f"{key}: {value}\n")
driver.quit()