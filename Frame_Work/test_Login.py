from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.select import Select
from Library1 import All_Operations
from login import TestLogin
def test_login(setup_tear_down):
    a = All_Operations(setup_tear_down)
    d = TestLogin(setup_tear_down)
    d.login()



