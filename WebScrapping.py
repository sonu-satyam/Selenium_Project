from csv import DictWriter
from re import findall
from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()

driver.get("https://ticker.finology.in/market/index/nse/niftyjr")
sleep(2)
# company_names
company_names = driver.find_elements("xpath", "//table[@id='companylist']//td[2]")
sleep(2)
names = [name.text for name in company_names]
# share_price
share_prices = driver.find_elements("xpath", "//table[@id='companylist']//td[3]")
sleep(2)
prices = [price.text for price in share_prices]
sleep(2)
# percent_change
percent_change = driver.find_elements("xpath", "//table[@id='companylist']//td[4]")
sleep(2)
change = [changes.text for changes in percent_change]
sleep(2)

# mcap
company_mcap = driver.find_elements("xpath", "//table[@id='companylist']//td[5]")
sleep(2)
mcap = [m.text for m in company_mcap]
stocks = []
for n,p,c,m in zip(names,prices,change,mcap):
    d = {
        "company":n,
        "price":float("".join(findall(r"[\d\.]",p))),
        "change":float("".join(findall(r"[\d\.]",c))),
        "mcap":float("".join(findall(r"[\d\.]",m))),
        }
    stocks.append(d)
# writing in text file
# f = open("stocks.txt","w")
# for stock in stocks:
#     print(stock["company"],
#           stock["price"],
#           stock["change"],
#           stock["mcap"],file=f, flush=True)

# writing in csv file
with open ("stocks.csv", "w") as file:
    writer = DictWriter(file, fieldnames= ["company","price","change","mcap"])
    writer.writeheader()
    for stock in stocks:
        writer.writerow(stock)

driver.quit()