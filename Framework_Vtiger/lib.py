from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
def web_driver_wait(func):
    def wrapper(*args,**kwargs):
        instance = args[0]
        locator = args[1]
        _wait=WebDriverWait(instance.driver,15)
        _wait.until(ec.presence_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper

class All_Operations:

    def __init__(self,driver):
        self.driver = driver
    @web_driver_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @web_driver_wait
    def send_data(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)
    @web_driver_wait
    def drop_down(self,locator,visible_text):
        select = Select(self.driver.find_element(*locator))
        select.select_by_visible_text(visible_text)


    def popup_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def window_handle(self,n):
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[n])

    def select_multiple_element(self,locator):
        elements = self.driver.find_elements(*locator)
        for element in elements:
            element.click()



