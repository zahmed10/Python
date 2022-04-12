class BankAccount:
    all_accounts = []
    def __init__(self, int_rate = 0.01, balance = 0): 
# don't forget to add some default values for these parameters!
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
        self.interest_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
# your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
# your code here
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
# your code here
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
# your code here
        if self.balance > 0:
            self.balance += self.balance*self.interest_rate
        else:
            print("Insufficient funds")
        
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        # we use cls to refer to the class
        for account in cls.all_accounts:
            account.display_account_info()
        return sum