from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver

driver = WebDriver()
driver.get("https://www.amazon.in/")
driver.find_element("id", "twotabsearchtextbox").send_keys("iphone")
driver.find_element("id", "nav-search-submit-button").click()
element = driver.find_elements("xpath", "//span[@class='a-size-medium a-color-base a-text-normal']")
driver.minimize_window()
items = []
for e in element:
    items.append(e.text)

prices = []
elements_ = driver.find_elements("xpath","//span[@class='a-price-whole']")
for item in elements_:
    item_=item.text
    price_=float(item_.replace(",",""))
    prices.append(price_)

item_price_pairs = {item:price for item,price in zip(items,prices)}

pairs_sort = sorted(item_price_pairs.items(),key=lambda item:item[1])
print(pairs_sort[-1])
print(pairs_sort[0])


