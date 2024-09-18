from selenium.webdriver.firefox.webdriver import WebDriver
from lib import All_Operations
def test_delete_lead(tear_bear_down):
    a = All_Operations(tear_bear_down)
    a.send_data(("xpath", "//input[@name='user_name']"), "admin")
    a.send_data(("xpath", "//input[@name='user_password']"), "admin")
    a.click_element(("id", "submitButton"))
    a.click_element(("xpath", "(//a[text()='Leads'])[1]"))
    a.click_element(("xpath", "(//a[text()='xyz'])[1]"))
    a.click_element(("xpath", "(//input[@name='Delete'])[2]"))
    a.popup_accept()

def test_multiple_delete(tear_bear_down):
    a = All_Operations(tear_bear_down)
    a.send_data(("xpath", "//input[@name='user_name']"), "admin")
    a.send_data(("xpath", "//input[@name='user_password']"), "admin")
    a.click_element(("id", "submitButton"))
    a.click_element(("xpath", "(//a[text()='Leads'])[1]"))
    a.select_multiple_element(("xpath", "//input[@name='selected_id']"))
    a.click_element(("xpath", "(//input[@class='crmbutton small delete'])[2]"))
    a.popup_accept()



