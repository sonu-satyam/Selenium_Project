from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
url_title = driver.title
url = driver.current_url
print(url_title)
print(url)


driver.find_element("xpath","//a[@class='ico-login']").click()
driver.find_element("id","Email").send_keys("gatesbilldmoe@gmail.com")
driver.find_element("id", "Password").send_keys("bill123")
driver.find_element("xpath", "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input").click()
driver.find_element("xpath", "/html/body/div[4]/div[1]/div[2]/ul[1]/li[1]/a").click()
driver.find_element("xpath", "/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[1]/div/div[2]/div[3]/div[2]/input").click()
driver.find_element("xpath", "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a/span[1]").click()



