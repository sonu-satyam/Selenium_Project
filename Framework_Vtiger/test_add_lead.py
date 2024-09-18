from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
from lib import All_Operations
def test_add_lead(tear_bear_down):
    a = All_Operations(tear_bear_down)
    a.send_data(("xpath","//input[@name='user_name']"),"admin")
    a.send_data(("xpath", "//input[@name='user_password']"),"admin")
    a.click_element(("id", "submitButton"))
    a.click_element(("xpath", "(//a[text()='Leads'])[1]"))
    a.click_element(("xpath", "//img[@title='Create Lead...']"))
    a.drop_down(("xpath", "//select[@name='salutationtype']"),"Mr.")
    a.send_data(("xpath", "//input[@name='firstname']"),"mark")
    a.send_data(("xpath", "//input[@name='lastname']"),"Henry")
    a.send_data(("xpath", "//input[@name='company']"),"tek pyramid")
    a.send_data(("name", "designation"),"Qa")
    a.drop_down(("xpath", "//select[@name='leadsource']"),"Employee")
    a.drop_down(("xpath", "//select[@name='industry']"),"Engineering")
    a.send_data(("xpath", "//input[@name='annualrevenue']"),"1200000")
    a.send_data(("id", "noofemployees"),"100")
    a.send_data(("xpath", "//input[@id='secondaryemail']"),"mark9987@gmail.com")
    a.send_data(("xpath","//input[@id='phone']"),"9876567891")
    a.send_data(("xpath", "//input[@id='mobile']"),"9878654123")
    a.send_data(("xpath", "//input[@id='fax']"),"1234543213")
    a.send_data(("xpath", "//input[@id='email']"),"mark123456@gmail.com")
    a.drop_down(("xpath","//select[@name='leadstatus']"),"Hot")
    a.drop_down(("xpath", "//select[@name='rating']"),"Active")
    a.click_element(("xpath","(//input[@name='assigntype'])[2]"))
    a.drop_down(("xpath","//select[@name='assigned_group_id']"),"Support Group")
    a.click_element(("xpath", "(//input[@name='button'])[3]"))





