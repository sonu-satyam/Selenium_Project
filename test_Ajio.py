from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from re import findall
def test_Ajio():
    driver = WebDriver()
    driver.get("https://www.flipkart.com/")
    driver.find_element("xpath","//input[@class='Pke_EE']").send_keys("apple watch")
    sleep(2)
    driver.find_element("xpath", "//button[@class='_2iLD__']").click()
    sleep(3)
    element_name = driver.find_elements("xpath", "//a[@class='WKTcLC']")
    names=[]
    for name in element_name:
       names.append(name.text)

    element_price = driver.find_elements("xpath", "//div[@class='Nx9bqj']")
    prices = []
    for price in element_price:
        price_ = price.text
        p=float("".join(findall(r"[\d\.]",price_)))
        prices.append(p)

    price_name_pair={name:price for name,price in zip(names,prices)}

    sort_ = sorted(price_name_pair.items(),key=lambda item:item[1])
