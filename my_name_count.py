from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

driver = WebDriver()

driver.get("https://www.google.com/")
sleep(2)
driver.find_element("xpath", "//textarea[@id='APjFqb']").send_keys("Sonu")
sleep(2)
driver.find_element("xpath", "(//input[@class='gNO89b'])[1]").click()
sleep(2)

elements = driver.find_elements("xpath","//*[contains(text(),'Sonu')]")
for element in elements:
    print(element.text)

driver.minimize_window()
