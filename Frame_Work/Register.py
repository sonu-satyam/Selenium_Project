from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
from selenium.webdriver.support.select import Select
from Library1 import All_Operations

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
a = All_Operations(driver)

sleep(2)
a.click_element(("link text", "Register"))
sleep(2)
a.click_element(("id", "gender-male"))
sleep(2)
a.send_data(("id", "FirstName"), "mark")
sleep(2)
a.send_data(("id", "LastName"),"henry")
sleep(2)
a.send_data(("id","Email"),"mark12345@gmail.com")
sleep(2)
a.send_data(("id","Password"),"mark123")
sleep(2)
a.send_data(("id", "ConfirmPassword"),"mark123")
sleep(2)
a.click_element(("id", "register-button"))
sleep(2)
a.click_element(("xpath", "//a[text()='Twitter']"))
sleep(2)
a.windows_handle(0)

