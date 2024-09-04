from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= opts )
#####################
# login
# driver.get("https://www.flipkart.com/account/login?ret=/")
# _wait = WebDriverWait(driver, 10)
# _wait.until(ec.visibility_of_element_located(("xpath", "//input[@class='r4vIwl BV+Dqf']"))).send_keys("7762998177")
#
# _wait = WebDriverWait(driver,10)
# _wait.until(ec.visibility_of_element_located(("xpath", "//button[text()='Request OTP']"))).click()
#####################

