from csv import reader
from csv import DictWriter
import csv
from re import findall
from time import sleep
#
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver
driver = WebDriver()
driver.get("https://demowebshop.tricentis.com/")
# sleep(3)
# book_names = driver.find_elements("xpath", "//h2[@class='product-title']")
# sleep(3)
# books = [book.text for book in book_names]
# sleep(3)
# book_prices = driver.find_elements("xpath", "//span[@class='price actual-price']")
# prices = [price.text for price in book_prices]
# book_price_pair = []
# for b,p in zip(books,prices):
#     d={
#         "book":b,
#         "price":"".join(findall(r"[\d\.]",p)),
#     }
#     book_price_pair.append(d)
# #writing in text file
# # f=open("book_price.txt","w")
# # for item in book_price_pair:
# #     print(item["book"],
# #           item["price"],file=f,flush=True)
#
# # writing in csv file
# with open("book_pricedemo.csv","w") as file:
#     writer = DictWriter(file,fieldnames=['book','price'])
#     writer.writeheader()
#     writer.writerows(book_price_pair)
#
#
# # reading from csv file
def read_csv():
    data = {}
    path = "C:/Users/Rudra/PycharmProjects/SeleniumProject1/book_pricedemo.csv"
    with open(path,"r") as file:
        rows = csv.reader(file)
        headers = next(rows)
        for row in rows:
            data[row[0]]=row[1]
        return data

data = read_csv()

for book,expected_price in data.items():
    _xpath = f"//a[text()='{book}']/../..//span[@class='price actual-price']"
    actual_price = driver.find_element("xpath", _xpath).text
    if actual_price == expected_price:
        print("pass")
    else:
        print("fail")
#



driver.quit()