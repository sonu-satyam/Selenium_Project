from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= opts)

driver.get("https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=1")
sleep(3)
actions = ActionChains(driver)
sleep(3)
source = driver.find_element("xpath","//div[text()='Mobile Charger']")
sleep(3)
dest = driver.find_element("xpath","(//div[@class='drop-column min-h-[200px] bg-slate-100'])[1]")
sleep(3)
actions.drag_and_drop(source,dest).perform()

sleep(3)
source1 = driver.find_element("xpath", "//div[text()='Laptop Cover']")
sleep(3)
dest1 = driver.find_element("xpath", "//div[@class='drop-column min-h-[200px] bg-slate-100']")
actions.drag_and_drop(source1,dest1).perform()


