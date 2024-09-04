from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
driver = WebDriver()

driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element("xpath", "//a[@class='ico-login']").click()
sleep(2)
driver.find_element("id","Email").send_keys("gatesbilldmoe@gmail.com")
driver.find_element("id", "Password").send_keys("bill123")
sleep(2)
driver.find_element("xpath", "//input[@class='button-1 login-button']").click()
sleep(2)
driver.find_element("xpath", "(//a[@href='/books'])[1]").click()
driver.minimize_window()
# books=['Computing and Internet', 'Health Book', 'Fiction']
##########################################################################
# add to cart
# for book in books:
#     _xpath= f"//a[text()='{book}']/../..//input[@class='button-2 product-box-add-to-cart-button']"
#     driver.find_element("xpath", _xpath).click()
#     sleep(3)
# for _ in range(5):
#     driver.find_element("xpath", "//a[text()='Fiction']/../..//input[@class='button-2 product-box-add-to-cart-button']").click()
#     sleep(3)

# driver.find_element("xpath", "//span[text()='Shopping cart']").click()
# sleep(3)

# driver.find_element("xpath", "//tr[@class='cart-item-row']/../..//input[@name='itemquantity4526100']").clear()
books={'Computing and Internet':10.00, 'Health Book':10.00, 'Fiction':24.00}
for book,price in books.items():
    x_path= f"//a[text()='{book}']/../..//span[@class='price actual-price']"
    element = driver.find_element("xpath", x_path)
    actual_price = element.text
    sleep(2)

    if float(actual_price) == price:
        print("PASS")
    else:
        print("FAIL")


# element = driver.find_element("xpath", "//a[text()='Fiction']/../..//span[text()='24.00']")
# print(element.text)

