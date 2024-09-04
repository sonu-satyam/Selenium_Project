from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = WebDriver()
driver.get("file:///C:/Users/Rudra/Desktop/Selenium/demo-html-20240826T064511Z-001/demo-html/dynamic.html")
#########################################################################
# driver.find_element("xpath", "//input[@id='adder1']").click()
# w = WebDriverWait(driver, 10)
# v = visibility_of_element_located(("xpath", "//select[@id='cars1']"))
# w.until(v)
# dropdown = driver.find_element("xpath", "//select[@id='cars1']")
# select = Select(dropdown)
# select.select_by_index(4)

###########################################################################
driver.find_element("xpath","//input[@id='adder2']").click()

_wait = WebDriverWait(driver, 10)
_wait.until(ec.element_to_be_clickable(("id", "cars2")))

##############################################################################
# driver.find_element("id", "adder3").click()

# _wait = WebDriverWait(driver, 10)
# _wait.until(ec.visibility_of_element_located(("id", "cars3")))