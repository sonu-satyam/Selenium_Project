from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep
from selenium.webdriver.support.select import Select
from Library1 import All_Operations
def test_Register(setup_tear_down):
    a = All_Operations(setup_tear_down)

    a.click_element(("link text", "Register"))
    a.click_element(("id", "gender-male"))
    a.send_data(("id", "FirstName"), "mark")
    a.send_data(("id", "LastName"),"henry")
    a.send_data(("id","Email"),"mark12345@gmail.com")
    a.send_data(("id","Password"),"mark123")
    a.send_data(("id", "ConfirmPassword"),"mark123")
    a.click_element(("id", "register-button"))
    a.click_element(("xpath", "//a[text()='Twitter']"))
    a.windows_handle(0)

