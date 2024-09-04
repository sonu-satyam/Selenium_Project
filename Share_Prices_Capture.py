from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()

driver.get("file:///C:/Users/Rudra/Desktop/Selenium/demo-html-20240826T064511Z-001/demo-html/demo.html")
driver.minimize_window()

# companies = ['MSFT', 'AAPL', 'FB']
# share_price = driver.find_element("xpath", "//td[text()='MSFT']/..//td[3]")
# for c in companies:
#     print(f"{c}\t\t", end="")
# print()
# sleep(2)
#
# while True:
#     for company in companies:
#         _xpath = f"//td[text()='{company}']/..//td[3]"
#         share_price = driver.find_element("xpath", _xpath).text
#         print(f"{share_price}\t\t", end="")
#     print()
#     sleep(2)
#############################################
# check whether first name is in ascending order
# fname = driver.find_elements("xpath", "//table[@name='customers']//td[2]")
#
# fnames  =[i.text for i in fname]
#
# sort_fname = sorted(fnames)
# if fnames == sort_fname:
#     print("pass")
# else:
#     print("fail")
###########################################
# check every second price change of
f=open('demo_file.txt', "w")
stocks = ['AAPL', 'MSFT', 'AA', 'FB']
while True:
    for stock in stocks:
        price_xpath = f"//td[text()='{stock}']/..//td[@class='price']"
        name_xpath = f"//td[text()='{stock}']"
        price = driver.find_element("xpath", price_xpath).text
        name = driver.find_element("xpath", name_xpath).text
        print(f"{name} \t : {price} \t",file = f, flush=True)
        sleep(1)
    print()



# while True:
#     if float(price.text) > 0.5:
#         print(f"{price.text}:{name.text}")
#         sleep(2)