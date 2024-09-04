from time import sleep

from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select

driver = WebDriver()
driver.get("http://49.249.28.218:8888/index.php?module=Home&action=index&parenttab=My%20Home%20Page")
# login
driver.find_element("xpath", "//input[@name='user_name']").send_keys("admin")
driver.find_element("xpath", "//input[@type='password']").send_keys("admin")
driver.find_element("xpath","//input[@id='submitButton']").click()

driver.find_element("xpath","//a[@href='index.php?module=Potentials&action=index']").click()
driver.find_element("xpath", "//img[@src='themes/softed/images/btnL3Add.gif']").click()

driver.find_element("xpath", "//input[@name='potentialname']").send_keys("changu")

element = driver.find_element("xpath", "//select[@id='related_to_type']")
select = Select(element)
select.select_by_index(1)

driver.find_element("xpath", '''//img[contains(@onclick,'return window.open("index.php?module="+')]''').click()

driver.switch_to.window(driver.window_handles[1])
sleep(5)
driver.find_element("xpath", "//a[@id='6']").click()
sleep(3)
driver.switch_to.window(driver.window_handles[0])
sleep(3)

# dropdown2
element1 = driver.find_element("xpath", "//select[@name='opportunity_type']")
select1= Select(element1)
select1.select_by_index(2)
sleep(3)
# dropdown3
element2 = driver.find_element("xpath", "//select[@name='leadsource']")
select2= Select(element2)
select2.select_by_index(5)
sleep(3)
driver.find_element("xpath", "//input[@name='assigntype'][2]").click()
sleep(5)

# dropdown4
element3 = driver.find_element("xpath", "//select[@name='assigned_group_id']")
select3= Select(element3)
select3.select_by_index(2)

sleep(2)
driver.find_element("xpath", "//img[@style='cursor:hand;cursor:pointer']").click()
driver.switch_to.window(driver.window_handles[1])
sleep(5)
driver.find_element("xpath", "//a[@id='1']").click()
driver.switch_to.window(driver.window_handles[0])

driver.find_element("xpath", "//input[@name='amount']").send_keys("1200")
driver.find_element("xpath", "//img[@id='jscal_trigger_closingdate']").click()
driver.find_element("xpath", "//input[@name='closingdate']").send_keys("2024-08-20")
driver.find_element("xpath", "//input[@id='nextstep']").send_keys("waiting")

element4 = driver.find_element("xpath", "//select[@name='sales_stage']")
select4 = Select(element4)
sleep(3)
select4.select_by_index(5)

driver.find_element("xpath", "//input[@id='probability']").send_keys("80")

driver.find_element("xpath", "//textarea[@class='detailedViewTextBox']").send_keys("hello python")
driver.find_element("xpath", '''(//input[@class="crmbutton small save"])[2]''').click()

driver.find_element("xpath", "(//input[@class='crmbutton small delete'])[2]").click()

popup = driver.switch_to.alert
sleep(3)
popup.accept()