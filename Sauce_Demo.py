from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from re import findall
driver = WebDriver()

driver.get("https://www.saucedemo.com/v1/")
driver.find_element("id", "user-name").send_keys("standard_user")
driver.find_element("id", "password").send_keys("secret_sauce")
driver.find_element("id", "login-button").click()

# elements_products = driver.find_elements("xpath", "//div[@class='inventory_item_name']")
# products = []
# for element in elements_products:
#     products.append(element.text)
# # print(products)
#
# elements_prices = driver.find_elements("xpath", "//div[@class='inventory_item_price']")
# prices = []
# for p in elements_prices:
#     prices.append(p.text)
# print(prices)

# price_product_pair = {item:price for item,price in zip(products,prices)}
# print(price_product_pair)
##################################################################################################
# print all the sauce word
words = driver.find_elements("xpath", "//*[contains(text(),'Sauce')]")
for word in words:
    print(word.text)



#################################
driver.minimize_window()