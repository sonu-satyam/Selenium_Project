from time import sleep
from selenium.webdriver.firefox.webdriver import WebDriver
driver = WebDriver()
# from selenium import webdriver
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach",True)
# driver = webdriver.Chrome(options=opts)

driver.get("https://www.google.co.in/")
driver.find_element("xpath", "//textarea[@id='APjFqb']").send_keys("Python")
sleep(2)
driver.find_element("xpath", "//input[@name='btnK']").click()
sleep(2)
elements = driver.find_elements("xpath", "//a[contains(text(),'Python')]")
sleep(2)
for item in elements:
    print(item.get_attribute("href"))

