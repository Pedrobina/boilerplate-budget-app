class Category:


    def __init__(self, name):
        self.category_name = name
        self.ledger = []
        self.balance = 0

    # Deposit
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.balance += amount

    # Check Founds
    def check_funds(self, amount):
        if amount < self.balance:
            return True
        else:
            return False

    # Withdraw
    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
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
        print(self.category_name)

    def create_spend_chart(categories):
        name = ""
