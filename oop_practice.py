# Defining a class:
class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0

# Adding a deposit "method (class-function)":
    def make_deposit(self, amount):                 # takes an argement that is the amount of the deposit
        self.account_balance += amount              # the specific user's account increases by the amount of the value received

