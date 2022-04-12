from classes.bank_account import BankAccount

user1 = BankAccount()
user2 = BankAccount()

# To the first account, make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line 
# of code (i.e. chaining)
print("User1 transactions:")
user1.deposit(2).deposit(2).deposit(2).yield_interest().display_account_info()
user1.display_account_info()

# To the second account, make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one 
# line of code (i.e. chaining)
print("\nUser2 transactions:")
user2.deposit(4).deposit(6).withdraw(1).withdraw(1).withdraw(5).withdraw(4).yield_interest().display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info
BankAccount.all_balances()