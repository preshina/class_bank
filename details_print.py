# Goal: Practice returning values from methods instead of printing directly.

# Add a method details() that returns a string like "Brand: Dell, Price: 500000".

# Print the returned string.
class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        return f"{self.brand} {self.price}"


d1 = Laptop("hp", 50000)
print(d1.details())
