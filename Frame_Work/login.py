from Library1 import All_Operations
class TestLogin:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        a = All_Operations(self.driver)
        a.click_element(("xpath", "//a[text()='Log in']"))
        a.send_data(("id", "Email"), "mark12345@gmail.com")
        a.send_data(("id", "Password"), "mark123")
        a.click_element(("xpath", "//input[@class='button-1 login-button']"))

