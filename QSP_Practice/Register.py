from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.webdriver import WebDriver
driver = WebDriver()

# register
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
# driver.find_element("xpath", "//input[@placeholder='Enter your name']").send_keys("Sonu Satyam")
# driver.find_element("xpath", "//input[@id='email']").send_keys("sonustm@gmail.com")
# driver.find_element("xpath", "//input[@id='password']").send_keys("jh15m7700")
# sleep(3)
# driver.find_element("css selector", "button[type='submit']").click()

# "login"
# driver.get("https://demoapps.qspiders.com/ui/login")
# driver.find_element("xpath","//input[@id='email']").send_keys("sonustm@gmail.com")
# driver.find_element("xpath", "//input[@id='password']").send_keys("jh15m7700")
# driver.find_element("css selector", "button[type='submit']").click()

################################
# checkbox
# driver.get("https://demoapps.qspiders.com/ui/checkbox?sublist=0")
# driver.maximize_window()
# checkboxes = driver.find_elements("xpath", "//input[@type='checkbox']")
# for checkbox in checkboxes:
#     checkbox.click()


##########################################
# radio button
# driver.get("https://demoapps.qspiders.com/ui/radio?sublist=0")
# driver.maximize_window()
# radio_ = driver.find_elements("xpath", "//input[@type='radio']")
# for radio in radio_:
#     radio.click()
#     sleep(2)

########################
# buttons
# driver.get("https://demoapps.qspiders.com/ui/button")
# driver.find_element("css selector","button[id='btn']").click()


####################################################################################
# links
sleep(3)
driver.find_element("xpath", "//a[@href='/ui/link']").click()
sleep(3)
driver.find_element("xpath", "//a[@href='/ui/link/linkNew?sublist=1']").click()
sleep(5)
# driver.find_element("xpath", "//a[text()='Contact Us']").click()
# driver.switch_to.window(driver.window_handles[1])

# driver.minimize_window()
###################################
# clicking on all elements
links = driver.find_elements("xpath", "//a")
for link in links:
    link.click()
    sleep(3)
    driver.get("https://demoapps.qspiders.com/ui/link/linkNew?sublist=1")
    sleep(3)
