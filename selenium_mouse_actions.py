from time import sleep

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(options= opts )



# mouse hover
# driver.get("https://demoapps.qspiders.com/ui/mouseHover?sublist=0")
# actions = ActionChains(driver, 2000)
# sleep(3)
# actions.move_to_element(driver.find_element("xpath", "//img[@class='w-5 h-5 mt-5 ml-3 cursor-pointer ']")).perform()

###########################################################
# tooltip mouse hover on image
# driver.get("https://demoapps.qspiders.com/ui/mouseHover/mouseHoverimage?sublist=1")
# actions = ActionChains(driver, 2000)
# sleep(3)
# actions.move_to_element(driver.find_element("xpath", "//img[@title='Order Placed Image']")).perform()

########################################################
#right click
# driver.get("https://demoapps.qspiders.com/ui/button/buttonRight?sublist=1")
# actions = ActionChains(driver, 2000)
# sleep(3)
# actions.context_click(driver.find_element("xpath", "(//button[text()='Right Click'])[1]")).perform()
# sleep(2)
# driver.find_element("xpath", "(//div[@class='py-1 ps-1 hover:bg-orange-300'])[1]").click()

##################################################
# double_click
# driver.get("https://demoapps.qspiders.com/ui/button/buttonDouble?sublist=2")
# actions = ActionChains(driver,2000)
# sleep(3)
# actions.double_click(driver.find_element("xpath", "//button[@id='btn20']")).perform()