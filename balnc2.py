from datetime import datetime
# class bank:

def __init__(self,name,account,balance=0):
        self.name=name
        self.account= account
        self.balance= balance
        self.history = []


def getinfo(self):  
        print(f"name: {self.name}, account:{self.account}, balance:{self.balance}, ") 


def deposite(self, amount):
        self.balance = self.balance +amount
        self.history.append(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -> deposited :{amount}")
        # print("amount deposite", amount)

    # def deposite(self,amount):
    #     self.balance= self.balance + amount
    #     self.history.append(f"{}")
    #     print("amount deposite", amount)


def withdraw(self, amount):
        self.balance>=amount
        self.balance = self.balance - amount
        self.balance = self.balance +amount
        self.history.append(f"{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ->withdraw :{amount}")
        # print("Your withdraw",amount)
        
def get_history(self):
        return self._balance
        print(f"Transaction Details of {self.name}")
        for entry in self.history:
            print(entry)
    

       
c1 = (" sunaina ", 123456789)
c2 = (" kamni ", 324598123)

# c1.getinfo()
# c2.getinfo()

c1.deposite(323455)
c1.withdraw(500)

c1.get_history()

c2.deposite(1000)
c2.withdraw(30)

c2.get_history()
# pip install google.generativeai