# Create a class Laptop with brand and price.

# Add a method called increase_price(amount) that:

# adds the given amount to the price.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def increase_price(self, amount):
        self.price = self.price+amount


d1 = Laptop("hp", 5000)
d1.increase_price(2000)
print(d1.price)
