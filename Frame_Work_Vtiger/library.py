from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.firefox.webdriver import WebDriver as FireFox



def _wait(func):
    def wrapper(*args,**kwargs):
        # driver,locator = args
        instance = args[0]
        locator = args[1]
        w = WebDriverWait(instance.driver,10)
        w.until(ec.presence_of_element_located(locator))
        return func(*args,**kwargs)
    return wrapper

class All_Operations:

    def __init__(self,driver):
        self.driver = driver
    @_wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()

    @_wait
    def send_data(self,locator, data):
        self.driver.find_element(*locator).send_keys(data)

    @_wait
    def dropdown(self,locator,data):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(data)


    def popup_accept(self):
        alert = self.driver.switch_to.alert
        alert.accept()


    def popup_dismiss(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()


    def windows_handle(self,n):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[n])
    @_wait
    def double_click(self,locator):
        actions = ActionChains(self.driver)
        click_me = self.driver.find_element(*locator)
        actions.double_click(click_me).perform()
    @_wait
    def right_click(self,locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()
    @_wait
    def drag_drop(self,source_locator, target_locator):
        source_element = self.driver.find_element(*source_locator)
        target_element = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()










