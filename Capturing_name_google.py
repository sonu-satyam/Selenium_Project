from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = WebDriver()

driver.get("https://www.google.com/")

_wait = WebDriverWait(driver, 15)
_wait.until(ec.presence_of_element_located(("xpath", "//textarea[@id='APjFqb']"))).send_keys("jishan")
sleep(5)
driver.find_element("xpath", "(//input[@class='gNO89b'])[1]").click()
sleep(5)
names = driver.find_elements("xpath", "//*[contains(text(),'Jishan')]")
sleep(3)
for name in names:
    print(name.text)