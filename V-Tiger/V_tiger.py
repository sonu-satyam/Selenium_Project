from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from time import sleep, time
from selenium import webdriver
driver = WebDriver()


driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")

driver.find_element("xpath", "//input[@name='user_name']").send_keys("admin")
driver.find_element("xpath", "//input[@type='password']").send_keys("admin")
driver.find_element("xpath", "//input[@id='submitButton']").click()
driver.find_element("xpath", "//a[@href='index.php?module=Leads&action=index']").click()
driver.find_element("xpath", "/html/body/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[1]/a/img").click()

dropdown= driver.find_element("xpath", "//select[@name='salutationtype']")
select = Select(dropdown)
sleep(5)
select.select_by_index(1)

driver.find_element("xpath", "//input[@name='firstname']").send_keys("mark")
driver.find_element("xpath", "//input[@name='lastname']").send_keys("gates")
driver.find_element("xpath", "//input[@name='company']").send_keys("TCS")
driver.find_element("xpath", "//input[@id='designation']").send_keys("MANAGER")

dropdown_lead =  driver.find_element("xpath", "//select[@name='leadsource']")
select_lead = Select(dropdown_lead)
select_lead.select_by_index(6)

dropdown_industry = driver.find_element("xpath", "//select[@name='industry']")
select_industry = Select(dropdown_industry)
select_industry.select_by_index(6)

driver.find_element("xpath", "//input[@name='annualrevenue']").send_keys("18000")
driver.find_element("xpath", "//input[@name='noofemployees']").send_keys("25")
driver.find_element("xpath", "//input[@id='secondaryemail']").send_keys("bill@gmail.com")
driver.find_element("xpath", "//input[@id='phone']").send_keys("8765432109")
driver.find_element("xpath", "//input[@id='mobile']").send_keys("9876543210")
driver.find_element("xpath", "//input[@id='fax']").send_keys("9876456782")
driver.find_element("xpath", "//input[@id='email']").send_keys("billgates@gmail.com")
driver.find_element("xpath", "//input[@name='website']").send_keys("www.tcs12345.com")

dropdown_lead_status = driver.find_element("xpath", "//select[@name='leadstatus']")
select_lead_status = Select(dropdown_lead_status)
select_lead_status.select_by_index(6)

dropdown_rating = driver.find_element("xpath", "//select[@name='rating']")
select_rating = Select(dropdown_rating)
select_rating.select_by_index(3)

driver.find_element("xpath", "//input[@value='U']").click()

driver.find_element("xpath", "//input[@id='pobox']").send_keys("sri venketeshwara nilaya")
driver.find_element("xpath", "//input[@id='code']").send_keys("560077")
driver.find_element("xpath", "//input[@id='city']").send_keys("bangalore")
driver.find_element("xpath", "//input[@id='country']").send_keys("india")
driver.find_element("xpath", "//input[@id='state']").send_keys("karnataka")
driver.find_element("xpath", "//textarea[@name='lane']").send_keys("2nd street")
driver.find_element("xpath", "//textarea[@name='description']").send_keys("saraipalya")
driver.find_element("xpath", "//input[@class='crmButton small save']").click()

driver.find_element("xpath", "//td[@class='dvtTabCache']/..//input[@name='Delete']").click()

popup = driver.switch_to.alert
sleep(5)
popup.accept()