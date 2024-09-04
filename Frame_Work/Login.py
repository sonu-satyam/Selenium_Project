from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select
from Library1 import All_Operations

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
a = All_Operations(driver)
a.click_element(("xpath", "//a[text()='Log in']"))
a.send_data(("id","Email"),"mark12345@gmail.com")
a.send_data(("id", "Password"),"mark123")
a.click_element(("xpath", "//input[@class='button-1 login-button']"))

