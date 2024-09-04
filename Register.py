from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")

driver.maximize_window()
url_title = driver.title
url = driver.current_url
print(url_title)
print(url)

driver.find_element("link text","Register").click()
driver.find_element("id","gender-male").click()
driver.find_element("id","FirstName").send_keys("Bill")
driver.find_element("id","LastName").send_keys("Gates")
driver.find_element("id","Email").send_keys("gatesbilldmoe@gmail.com")
driver.find_element("id","Password").send_keys("bill123")
driver.find_element("id","ConfirmPassword").send_keys("bill123")
driver.find_element("id","register-button").click()
driver.find_element("xpath", "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[2]/input").click()

driver.save_screenshot("photo.png")

sleep(5)



