from library import All_Operations
from xlrd import open_workbook
def read_data(worksheet):
    data = {}
    wb = open_workbook("objects.xls")
    ws = wb.sheet_by_name(worksheet)
    for i in range(1,ws.nrows):
        loc = ws.row_values(i)
        data[loc[0]] = (loc[1] ,loc[2])
    return data
# print(read_data("addleads"))
class Add_Leads:
    locators = read_data(worksheet = "addleads")
    def __init__(self,driver):
        self.driver = driver

    def add_lead(self,title,fname,lname,company,designation,lead_source):
        a = All_Operations(self.driver)

        a.click_element(Add_Leads.locators["openlead"])
        a.click_element(Add_Leads.locators["add_lead"])
        a.dropdown(Add_Leads.locators["salutation"],data = title)
        a.send_data(Add_Leads.locators["fname"],data = fname)
        a.send_data(Add_Leads.locators["lname"],data=lname)
        a.send_data(Add_Leads.locators["company"],data=company)
        a.send_data(Add_Leads.locators["designation"],data=designation)
        a.dropdown(Add_Leads.locators["lead_source"],data=lead_source)
        a.click_element(Add_Leads.locators["save"])



