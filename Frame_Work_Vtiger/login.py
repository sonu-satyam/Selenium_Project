from library import All_Operations
from xlrd import open_workbook
def read_data(sheetname):
    wb = open_workbook("objects.xls")
    ws = wb.sheet_by_name(sheetname)
    read_locators = {}

    for i in range(1,ws.nrows):
        row_=ws.row_values(i)
        read_locators[row_[0]] = (row_[1] ,row_[2])
    return read_locators



class Login:
    locators = read_data("loginpage")
    def __init__(self,driver):
        self.driver = driver

    def test_login(self,user_id,pwd):
        a = All_Operations(self.driver)
        a.send_data(Login.locators["username"],data=user_id)
        a.send_data(Login.locators["password"],data = pwd)
        a.click_element(Login.locators["click"])
