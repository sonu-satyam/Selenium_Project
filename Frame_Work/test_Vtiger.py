from time import sleep

from selenium.webdriver.firefox.webdriver import WebDriver
def test_Vtiger():
    driver = WebDriver()
    driver.get("http://49.249.28.218:8888/index.php?action=Login&module=Users")
    from Library1 import All_Operations
    a = All_Operations(driver)

    a.send_data(("xpath", "//input[@name='user_name']"),"admin")
    a.send_data(("xpath","//input[@name='user_password']"),"admin")
    a.click_element(("id", "submitButton"))
    a.click_element(("xpath","(//a[text()='Organizations'])[1]"))
    a.click_element(("xpath", "//img[@title='Create Organization...']"))
    a.send_data(("xpath","//input[@name='accountname']"),"bhadra01")
    a.send_data(("xpath", "//input[@name='website']"),"bhadra.com")
    a.click_element(("xpath", "//input[@title='Clear']"))
    a.click_element(("xpath", "//img[@title='Select']"))
    a.windows_handle(1)
    sleep(3)
    a.click_element(("xpath", "//a[@id='1']"))
    sleep(2)
    a.windows_handle(0)
    # a.send_data(("xpath","//input[@id='employees']"),"Automation Engineer")
    a.send_data(("xpath", "//input[@id='email2']"), "bhadra2@gmail.com")
    a.select_data(("xpath", "//select[@name='industry']"), "Education")
    a.select_data(("xpath","//select[@name='accounttype']"), "Investor")
    a.click_element(("xpath", "//input[@name='emailoptout']"))
    a.click_element(("xpath", "(//input[@name='assigntype'])[2]"))
    a.select_data(("xpath", "//select[@name='assigned_group_id']"),"Team Selling")
    a.send_data(("xpath", "//input[@id='phone']"),"8993298761")
    a.send_data(("xpath", "//input[@id='fax']"), "1234567890")
    a.send_data(("xpath", "//input[@id='otherphone']"),"9876542314")
    a.send_data(("xpath", "//input[@id='email1']"), "bhadraa123@gmail.com")
    a.send_data(("xpath", "//input[@id='ownership']"), "Private")
    a.select_data(("xpath", "//select[@name='rating']"),"Active")
    a.send_data(("xpath", "//input[@id='siccode']"),"bhadruuuuuu")
    a.send_data(("xpath", "//input[@name='annual_revenue']"),"100000")
    a.click_element(("xpath", "//input[@name='notify_owner']"))
    a.send_data(("xpath", "//textarea[@name='bill_street']"),"kotalpur,West Bengal")
    a.send_data(("xpath", "//input[@name='bill_pobox']"), "bankura")
    a.send_data(("id", "bill_state"), "West Bengal")
    a.send_data(("xpath", "//input[@name='bill_code']"), "853006")
    a.send_data(("id", "bill_country"), "India")
    a.send_data(("xpath", "//textarea[@name='description']"), "akash bhadra is going to be next elon musk")
    a.click_element(("xpath", "(//input[@name='cpy'])[2]"))
    a.click_element(("xpath", "(//input[@name='button'])[3]"))
    a.click_element(("xpath", "(//input[@name='Delete'])[1]"))
    a.pop_up_accept()







