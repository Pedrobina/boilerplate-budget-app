class Category:


    def __init__(self, name):
        self.category_name = name
        self.ledger = []
        self.balance = 0
        self.inicialdeposit = 0

    # Deposit
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount
        self.inicialdeposit = amount

    # Check Founds
    def check_funds(self, amount):
        if amount < self.balance:
            return True
        else:
            return False

    # Withdraw
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": 0 - amount, "description": description})
            self.balance -= amount
            return True
        else:
            return False

    # Balance
    def get_balance(self):
        return self.balance

    # Transfer
    def transfer(self, amount, transfer_category):
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + transfer_category.name)
            transfer_category.deposit(amount, "Transfer from " + self.category_name)
            return True
        else:
            return False

    def display(self):
        #Get Category Name
        i = 1
        space = ""
        displayName = ""
        space_line = (30 - len(self.category_name))/2
        while i <= space_line:
            displayName = displayName + "*"
            i = i + 1
        displayName = displayName + self.category_name
        i = 1
        while i <= space_line:
            displayName = displayName + "*"
            i = i + 1

        #Get Initial Deposit
        countDeposit = len(str(self.inicialdeposit))
        countSpace = 15 - countDeposit
        i = 1
        while i <= countSpace:
            space = space + " "
            i = i + 1
        displayName = displayName + "\n" + "initial deposit" + space + str(self.inicialdeposit)



        return displayName




def create_spend_chart(categories):
        name = ""
