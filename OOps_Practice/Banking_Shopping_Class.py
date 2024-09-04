# class Bank:
#     roi = 0.1
#
#     def __init__(self,name,balance):
#         self.name = name
#         self.balance = balance
#         self.statement = []
#
#     def deposit(self,amount):
#         if amount < 0:
#             raise Exception("amount should not be less than 0")
#         self.balance += amount
#         self.statement.append(f"deposited : amount {amount}")
#
#
#     def withdraw(self,amount):
#         if amount > self.balance:
#             raise Exception("amount should not be more than balance")
#         self.balance -= amount
#         self.statement.append(f"withdrawn : {amount}")
#
#     def rate_of_interest(self):
#         interest = self.__class__.roi  * self.balance
#         self.balance += interest
#         self.statement.append(f"interest credited : {interest}")
#
#     def transfer(self,amount,to_cust):
#         self.balance = self.balance - amount
#         to_cust.deposit(amount)
#         self.statement.append(f"amount sent to {to_cust.name}")
#
#
#
# cust1 = Bank("alex", 10000)
# cust2 = Bank("mark",5000)
#
# cust1.transfer(1000,cust2)
# print(vars(cust1))


############################################################################
# shopping CArt
class Shopping:
    items = {"iphone":4, "samsung":7, "vivo":8, "oppo":4, "motorola":5}
    def __init__(self,name):
        self.name = name
        self.cart = []

    def add_item(self,item,quantity):
        if item in self.__class__.items:
            self.cart.append({item:quantity})
            self.__class__.items[item] -= quantity
        else:
            raise Exception("item out of stock")

    def remove_item(self,item):
        for i in self.cart:
            print(i)




cart1 = Shopping("steve")
cart1.add_item("iphone",3)
cart1.add_item("samsung",4)
cart1.add_item("vivo",5)
cart1.remove_item("iphone")
# print(vars(cart1))
# print(Shopping.items)
