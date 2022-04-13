    #Bank account class
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

class User:
    from user import BankAccount
    # class attributes get defined in the class 
    bank_name = "First National Dojo"
    # now our method has 2 parameters!
    def __init__(self , name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account = []
        # BankAccount(self)

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account.deposit(amount)	# the specific user's account increases by the amount of the value receive

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    
    def display_user_balance(self):
        self.account.display_account_info()
    
    def make_accounts(self, num_accounts):
        for i in range(1, num_accounts, 1):
            self.account.append(BankAccount(self))

user1 = User("gee", "gee@123.org")
user1.make_deposit(100)
user1.display_user_balance()

user2 = User("new guy", "new@guy.org")
user2.make_accounts(5)

BankAccount.all_balances()

