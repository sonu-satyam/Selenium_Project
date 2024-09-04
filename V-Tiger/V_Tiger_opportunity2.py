from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = WebDriver()
driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")
sleep(2)
driver.find_element("xpath", "//input[@name='user_name']").send_keys("admin")
sleep(2)
driver.find_element("xpath", "//input[@name='user_password']").send_keys("admin")
sleep(2)
driver.find_element("xpath", "//input[@id='submitButton']").click()
sleep(2)
driver.find_element("xpath", "//td[@class='tabUnSelected']/..//a[text()='Opportunities']").click()
sleep(2)
# elements = driver.find_elements("xpath", "//input[@name='selected_id']")
# sleep(2)
# for e in elements:
#     e.click()
# sleep(5)
# driver.find_element("xpath", "(//table[@class='small']/..//input[@class='crmbutton small delete'])[1]").click()
# sleep(3)
# popup = driver.switch_to.alert
# popup.accept()

# edit
driver.find_element("xpath", "//input[@id='642']/../..//a[text()='edit']").click()
dropdown = driver.find_element("xpath", "//select[@name='sales_stage']")
select = Select(dropdown)
select.select_by_index(4)
