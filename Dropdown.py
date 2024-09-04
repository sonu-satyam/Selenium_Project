from selenium.webdriver.firefox.webdriver import WebDriver
import time
from selenium.webdriver.support.select import Select

driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element("xpath","//a[@class='ico-login']").click()
driver.find_element("xpath","//input[@id='Email']").send_keys("gatesbilldmoe@gmail.com")
driver.find_element("xpath","//input[@id='Password']").send_keys("bill123")
driver.find_element("xpath","//input[@id='RememberMe']").click()
driver.find_element("xpath","//input[@class='button-1 login-button']").click()
driver.find_element("xpath","/html/body/div[4]/div[1]/div[2]/ul[1]/li[1]/a").click()
time.sleep(3)
dropdown = driver.find_element("xpath","//select[@id='products-orderby']")
select = Select(dropdown)
select.select_by_index(4)

driver.find_element("xpath","/html/body/div[4]/div[1]/div[4]/div[2]/div[2]/div[2]/div[3]/div[2]/div/div[1]/a/img").click()
driver.find_element("xpath","//input[@id='addtocart_45_EnteredQuantity']").send_keys("5")
driver.find_element("xpath","//input[@id='add-to-cart-button-45']").click()
driver.find_element("xpath","/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[3]/a/span[1]").click()



