class Category:

    def __init__(self, name):
        self.category_name = name
        self.ledger = []
        self.withdraws_description = []
        self.withdraws_value = []
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
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": 0 - amount, "description": description})
            self.withdraws_description.append(description)
            self.withdraws_value.append(0 - amount)
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
            self.withdraws_description.append("Transfer to " + self.category_name)
            self.withdraws_value.append(0 - amount)
            return True
        else:
            return False


    def display(self):

        # Get Category Name
        i = 1
        space = ""
        displayList = ""
        space_line = (30 - len(self.category_name)) / 2
        while i <= space_line:
            displayList = displayList + "*"
            i = i + 1
        displayList = displayList + self.category_name
        i = 1
        while i <= space_line:
            displayList = displayList + "*"
            i = i + 1

        # Get Initial Deposit
        countDeposit = len(str(self.inicialdeposit))
        countSpace = 15 - countDeposit
        i = 1
        while i <= countSpace:
            space = space + " "
            i = i + 1
        displayList = displayList + "\n" + "initial deposit" + space + str(self.inicialdeposit)

        # Get Withdraws List
        withdrawsCounter = len(self.withdraws_value)
        i = 0
        while i < withdrawsCounter:
            displayList = displayList + "\n" + self.withdraws_description[i] + " " + str(self.withdraws_value[i])
            i = i + 1


        return displayList


def create_spend_chart(categories):
    name = ""
