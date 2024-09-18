from selenium.webdriver.firefox.webdriver import WebDriver
from lib import All_Operations
def test_login(tear_bear_down):
    a=All_Operations(tear_bear_down)
    a.send_data(("xpath","//input[@name='user_name']"),"admin")
    a.send_data(("xpath", "//input[@name='user_password']"),"admin")
    a.click_element(("id", "submitButton"))