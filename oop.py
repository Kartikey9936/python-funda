# deposit()
# withdraw()
# check_balance()

class bankbalance:
    def __init__(self):
        self.balance = 0
    def deposit(self,amount):
        self.balance += amount
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("insufficient balance")
    def check_balance(self):
        print("balance:", self.balance)
    
acc = bankbalance()
acc.deposit(40)
acc.check_balance()


