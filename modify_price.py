# Goal: Modify an attribute using a parameter.

# Add a method upgrade_price(amount) that increases the price by the amount given.

# Test by calling the method and printing the new price.

pass


class Price:
    def __init__(self, amount):
        self.amount = amount

    def upgrade_price(self):
        self.amount += 4000


d1 = Price(50000)
d1.upgrade_price()
print(d1.amount)
