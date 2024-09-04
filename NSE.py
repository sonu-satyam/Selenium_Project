from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

driver = WebDriver()
driver.get("https://www.nseindia.com/")
sleep(3)
names = driver.find_elements("xpath", "//div[@id='tab1_tableGainer']//td[1]")
sleep(3)
shares_prices = driver.find_elements("xpath", "//div[@id='tab1_tableGainer']//td[2]")
sleep(3)

driver.minimize_window()
sleep(3)
name_text = [name.text for name in names]
sleep(3)
share_text = [share.text for share in shares_prices]
sleep(3)
while True:
    for n,s in zip(name_text,share_text):
        print(f"{n} \t : {s} \t",end="")
    sleep(3)
    print()
