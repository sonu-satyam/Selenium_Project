from selenium.webdriver.firefox.webdriver import WebDriver
from selenium import webdriver

driver = WebDriver()
driver.get("file:///C:/Users/Rudra/Desktop/Selenium/demo-html-20240826T064511Z-001/demo-html/demo.html")
cars = ["Hyundai", "Maruti Suzuki", "Tata"]
Bikes = ["Yamaha", "Hero", "Honda"]
languages = ["Java", "Python", "Ruby"]

first_row = driver.find_elements("xpath","//table[@name='companies']//td//input[@class='first_row']")
for element,car in zip(first_row,cars):
    element.send_keys(car)

second_row = driver.find_elements("xpath","//table[@name='companies']//td//input[@class='second_row']")
for element,bike in zip(second_row,Bikes):
    element.send_keys(bike)

third_row = driver.find_elements("xpath","//table[@name='companies']//td//input[@class='third_row']")
for element,language in zip(third_row,languages):
    element.send_keys(language)

