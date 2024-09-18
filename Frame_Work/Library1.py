from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

def _wait(func):
    def wrapper(*args,**kwargs):
        # driver,locator = args
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver,10)
        w.until(ec.presence_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper

def wait_class(cls):
    for key,value in cls.__dict__.items():
        if callable(value) and key!="__init__" and key!= "windows_handle" and key!="pop_up_accept":
            setattr(cls,key,_wait(value))
    return cls

@wait_class
class All_Operations:

    def __init__(self,driver):
        self.driver = driver
    # @_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    # @_wait
    def send_data(self,locator,data):
        self.driver.find_element(*locator).send_keys(data)
    # @_wait
    def select_data(self,locator,data):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(data)


    # @_wait
    def windows_handle(self,n):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])


    # @_wait
    def page_scroll(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_UP).perform()

    def pop_up_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def mouse_hover(self,locator):
        action = ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()
