from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
driver = WebDriver()

driver.get("https://www.python.org/")
driver.find_element("link text", "Downloads").click()
sleep(5)

elements = driver.find_elements("xpath","//div[@class='row download-list-widget']//a")

for i in elements:
    href = i.get_attribute("href")
    print(href)
