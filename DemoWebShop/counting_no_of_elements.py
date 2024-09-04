from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
driver = WebDriver()

driver.get("https://demowebshop.tricentis.com/")

driver.find_element("xpath", "//a[@href='/books'][1]").click()
driver.minimize_window()
# books = ['Computing and Internet', 'Copy of Computing and Internet EX', 'Fiction', 'Fiction EX', 'Health Book', 'Science']
# for book in books:
#     x_path =f"//a[text()='{book}']/../..//span[@class='price actual-price']"
#     print(f"the price of {book} is {driver.find_element("xpath", x_path).text}

elements = driver.find_elements("xpath", "//div[@class='product-item']")
for item in elements:
    print(item.text)