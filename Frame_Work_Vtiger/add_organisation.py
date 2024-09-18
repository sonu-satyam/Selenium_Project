from library import All_Operations
from xlrd import open_workbook

def read_excel(sheetname):
    data = {}
    wb = open_workbook("objects.xls")
    ws = wb.sheet_by_name(sheetname)
    for i in range(1 , ws.nrows):
        row_ = ws.row_values(i)
        data[row_[0]] = (row_[1],row_[2])
    return data
# print(read_excel("addorg"))

class AddOrg:
    locators = read_excel("addorg")

    def __init__(self,driver):
        self.driver = driver

    def add_org(self,driver,orgname,website,ticker,memberof,industry,type):
        a = All_Operations(self.driver)

        a.click_element(AddOrg.locators["openorg"])
        a.click_element(AddOrg.locators["addorg"])
        a.send_data(AddOrg.locators["orgname"],data = orgname)
        a.send_data(AddOrg.locators["website"],data = website)
        a.send_data(AddOrg.locators["ticker"],data = ticker)
        a.send_data(AddOrg.locators["memberof"],data = memberof)
        a.dropdown(AddOrg.locators["industry"],data = industry)
        a.dropdown(AddOrg.locators["type"],data=type)
        a.click_element(AddOrg.locators["save"])