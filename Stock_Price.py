from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()

driver.get("https://ticker.finology.in/market/index/nse/niftyjr")

# prices = driver.find_element("xpath", "//div[@id='indiceslist']//a[text()='Vedanta']/../..//td[3]")
# percent = driver.find_element("xpath", "(//div[@id='indiceslist']//a[text()='Vedanta']/../..//td[4]")

# names= driver.find_elements("xpath", "//div[@id='indiceslist']//td[2]")
# prices = driver.find_elements("xpath", "//table[@id='companylist']//td[3]")
# percent = driver.find_elements("xpath", "//table[@id='companylist']//td[4]")
driver.minimize_window()

# for name,price in zip(names,prices):
#     print(name.text,price.text)

###########################################################################################
# check names are in sorted order

# names = driver.find_elements("xpath", "(//table[@class='table table-sm table-hover screenertable'])[3]//td[1]")
# name_text = [name.text for name in names]
# sort_name = sorted(name_text)
# # print(sort_name)

###########################################################################
# print price and percent change of stock every second

price = driver.find_element("xpath", "//table[@id='companylist']//a[text()='Vedanta']/../..//td[3]")
percent= driver.find_element("xpath", "//table[@id='companylist']//a[text()='Vedanta']/../..//td[4]")

while True:
    print(f"{price.text}: {percent.text}")
    sleep(2)

