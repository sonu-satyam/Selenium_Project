from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = WebDriver()

################################
# for progress bar
driver.get("https://demoapps.qspiders.com/ui/progress?sublist=0")

_wait = WebDriverWait(driver, 10)
_wait.until(ec.presence_of_element_located(("xpath", "//button[@class='active:bg-green-400 transition-all duration-300 active:border-green-400 rounded-md mx-1 px-5 py-2 text-white font-bold  disabled:opacity-25  bg-orange-500 border border-orange-700 hover:bg-orange-600']"))).click()
_wait= WebDriverWait(driver, 20)
_wait.until(ec.presence_of_element_located(("xpath", "//span[text()='48%']"))).find_element("xpath", "//button[text()='Pause']" ).click()
sleep(3)
driver.find_element("xpath", "//button[text()='Start']").click()

_wait = WebDriverWait(driver, 10)
_wait.until(ec.presence_of_element_located(("xpath", "//span[text()='100%']"))).find_element("xpath","//button[text()='Reset']").click()

_wait = WebDriverWait(driver,10)
_wait.until(ec.presence_of_element_located(("xpath", "//button[text()='Start']"))).click()


################################################################################
# loading page in new tab
# driver.get("https://demoapps.qspiders.com/ui/pageLoad?sublist=0")

# _wait = WebDriverWait(driver, 10)
# _wait.until(ec.visibility_of_element_located(("xpath", "//a[text()='Open In New Tab']"))).click()
# driver.switch_to.window(driver.window_handles[1])
#
# _wait = WebDriverWait(driver, 15)
# _wait.until(ec.presence_of_element_located(("xpath", "//input[@id='email']"))).send_keys("bhadruuu@gmail.com")
#
# _wait = WebDriverWait(driver,5)
# _wait.until(ec.presence_of_element_located(("xpath", "//button[text()='Subscribe']"))).click()

######################################################################################

