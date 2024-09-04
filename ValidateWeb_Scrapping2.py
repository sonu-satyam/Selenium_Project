import csv
from time import sleep
from csv import DictWriter,writer,reader,DictReader
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
driver = WebDriver()
sleep(3)
driver.get("file:///C:/Users/Rudra/Desktop/Selenium/demo-html-20240826T064511Z-001/demo-html/demo.html")
sleep(3)
# names = driver.find_elements("xpath", "//table[@name='customers']//td[2]")
# sleep(3)
# percentages = driver.find_elements("xpath", "//table[@name='customers']//td[4]")
# sleep(3)
#
# name_list = [name.text for name in names]
# percent_list = [percent.text for percent in percentages]

# Creating Csv File and writing into the csv file

# with open("demo_file01.csv", "w") as file:
#     writer_obj = csv.writer(file)
#     writer_obj.writerow(["name", "percent"])
#     for name,percent in zip(name_list,percent_list):
#         writer_obj.writerow([name,percent])
######################3
# read from csv file
def read_csv():
    with open("C:/Users/Rudra/PycharmProjects/SeleniumProject1/demo_file01.csv", "r") as file:
        data = {}
        reader_obj = csv.reader(file)
        header = next(reader_obj)
        for item in reader_obj:
            data[item[0]] = item[1]
    return data

data = read_csv()
for name,expected_price in data.items():
    x_path = f"//td[text()='{name}']/..//td[4]"
    actual_price = driver.find_element("xpath", x_path).text
    print(f"{actual_price}::{expected_price}")







driver.quit()
