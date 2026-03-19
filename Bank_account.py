# Create a class called BankAccount with:

# Attributes:

# account_number

# balance
# deposit(amount)

# Add the given amount to the balance
# withdraw(amount)

# If amount is less than or equal to balance:

# subtract it from balance

# Otherwise:

# print "Not enough balance"
# show_balance()

# Print the current balance

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposite(self, amount):
        self.balance = amount+self.balance

    def withdrawl(self, amount):
        if amount <= self.balance:
            self.balance = self.balance-amount
        else:
            print("No Enough!")

    def show_balance(self):
        print(self.balance)

    def transfer(self, amount, another_bank):
        if amount >= self.balance:
            self.balance -= amount
        else:
            another_bank.balance += amount


d1 = BankAccount(1002, 4000)
d2 = BankAccount(1223, 3000)
d1.deposite(3000)
d1.withdrawl(1000)
d1.transfer(1000, d2)
print(d1.balance)
print(d2.balance)
d1.show_balance()
