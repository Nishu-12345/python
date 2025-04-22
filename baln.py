class bank:
    def __init__(self,name,account,balance=0):
        self.name=name
        self.account= account
        self.balance= balance

    def getinfo(self):  
        print(f"name: {self.name}, account:{self.account}, balance:{self.balance} ") 

    def deposite(self,amount):
        self.balance= self.balance + amount
        print("amount deposite", amount)


    def withdraw(self, amount):
        self.balance>=amount
        self.balance = self.balance - amount
        print("Your withdraw",amount)
c1 = bank(" sunaina ", 123456789)
c2 = bank(" kamni ", 324598123)

c1.getinfo()
c2.getinfo()
c1.deposite(323455)
c2.deposite(1000)
# pip install google.generativeai