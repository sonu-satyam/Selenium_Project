from login import Login
from library import All_Operations
from add_contact import Add_Contact
from add_leads import Add_Leads
from add_organisation import AddOrg
from pytest import mark
from excel import read_data,read_headers

header = read_headers("test_add_contact","addcontact")
data = read_data("test_add_contact", "addcontact")
# header = "user_id,pwd,title,fname,lname,company,job,field,date,group"
# data = [("admin", "admin", "Mr.","bob","marley","ganja ganja","smokeyy","nasha", " 2024-09-13","Support Group"),
#         ("admin", "admin", "Mr.","bobby","marleyy","testing","smoke testing","regression", " 2024-09-13","Support Group")]
@mark.parametrize(header,data)
def test_add_contact(_driver,user_id,pwd,title,fname,lname,company,job,field,date,group):
    a= All_Operations(_driver)
    login = Login(_driver)
    login.test_login(user_id,pwd)

    b = Add_Contact(_driver)
    b.add_contact(title,fname,lname,company,job,field,date,group)




def test_delete_contact(_driver):
    a= All_Operations(_driver)
    login = Login(_driver)
    login.test_login("admin","admin")
    a.click_element(("xpath", "(//a[text()='Contacts'])[1]"))
    a.click_element(("xpath", "(//a[text()='del'])[1]"))
    a.popup_accept()



header = "user_id,pwd,title,fname,lname,company,designation,lead_source"
data = [("admin","admin","Mr.","Henry","Kumar","TYSS", "QA Engineer","Employee"),
        ("admin","admin","Mr.", "Kevin", "Batt", "Google", "QA", "Employee")]
@mark.parametrize(header,data)
def test_add_lead(_driver,user_id,pwd,title,fname,lname ,company, designation ,lead_source):
    a = All_Operations(_driver)
    login = Login(_driver)
    login.test_login(user_id,pwd)

    add_l = Add_Leads(_driver)
    add_l.add_lead(title,fname,lname ,company, designation ,lead_source)



header = "user_id,pwd,driver,orgname,website,ticker,memberof,industry,type"
data = [("admin","admin","TCS","www.tcs.com","hey","hii","testing", "Banking","Press"),
        ("admin","admin","Wipro", "www.wipro.com", "website", "hjihklo","development", "Banking", "Press")]
@mark.parametrize(header,data)
def test_add_org(_driver,user_id,pwd,driver,orgname,website,ticker,memberof,industry,type):
    a = All_Operations(_driver)
    login = Login(_driver)
    login.test_login(user_id,pwd)

    add_org = AddOrg(_driver)
    add_org.add_org(driver,orgname,website,ticker,memberof,industry,type)


