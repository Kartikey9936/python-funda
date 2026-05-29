class atm: 
    # constructor
    def __init__(self):
        self.pin =""
        self.balance = 0

        self.menu()

    def menu(self):
        # making multi string
        user_input = """
                   hello,welcome
                   1. enter 1 to create pin.
                   2. enter 2 to deposite.
                   3. enter 3 to withdraw.
                   4. enter 4 to checkbalance.
                   5. enter 5 to exit
    

""" 
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposite()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check_balance()
        elif user_input == "5":
            print("exit")
    
    def create_pin(self):
        self.pin = ("enter your pin")
        print("your pin is created")
    
    def deposite(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance + amount
            print("deposit successful")
        else:
            print("invalid pin")

    def withdraw(self):
        temp = input("enter your pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("withdraw successful")
            else:
                print("insufficient amount")

        else:
            print("invalid pin")
    
    def check_balance(self):
        temp = input("enter your pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")

