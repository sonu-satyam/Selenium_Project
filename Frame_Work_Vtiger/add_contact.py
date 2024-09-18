from asyncio import sleep

from library import All_Operations

class Add_Contact:

    locators = {"contact":("xpath", "//table[@class='hdrTabBg']//a[text()='Contacts']"),
                "create":("xpath", "//img[@title='Create Contact...']"),
                "salutation":("xpath", "//select[@name='salutationtype']"),
                "fname":("xpath", "//input[@name='firstname']"),
                "lname":("xpath", "//input[@name='lastname']"),
                "organization":("xpath", "//input[@name='account_name']"),
                "select_lead":("xpath", "//input[@name='account_name']"),
                "add_lead":("xpath", "//a[@id='1']"),
                "title":("xpath", "//input[@id='title']"),
                "department":("xpath", "//input[@id='department']"),
                "reference" :("xpath", "//input[@name='reference']"),
                "date":("xpath", "//input[@name='support_end_date']"),
                "assign_type": ("xpath", "(//input[@name='assigntype'])[2]"),
                "group":("xpath", "//select[@name='assigned_group_id']"),
                "save":("xpath", "(//input[@name='button'])[2]")
                }

    def __init__(self,driver):
        self.driver = driver

    def add_contact(self,title,fname,lname,company,job,field,date,group):
        a = All_Operations(self.driver)

        a.click_element(Add_Contact.locators["contact"])
        a.click_element(Add_Contact.locators["create"])
        a.dropdown(Add_Contact.locators["salutation"], data = title)
        a.send_data(Add_Contact.locators["fname"], data = fname)
        a.send_data(Add_Contact.locators["lname"], data = lname)
        a.send_data(Add_Contact.locators["organization"], data = company)
        a.send_data(Add_Contact.locators["title"], data = job)
        a.send_data(Add_Contact.locators["department"], data = field)
        a.click_element(Add_Contact.locators["reference"])
        a.send_data(Add_Contact.locators["date"], data = date)
        a.click_element(Add_Contact.locators["assign_type"])
        a.dropdown(Add_Contact.locators["group"], data = group)
        a.click_element(Add_Contact.locators["save"])