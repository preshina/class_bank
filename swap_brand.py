# Create a class Laptop with attributes brand and price.

# Add a method swap_brands(other_laptop) that swaps the brands of the two Laptop objects.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def swap_brand(self, other_laptop):
        temp = self.brand
        self.brand = other_laptop.brand
        other_laptop.brand = temp


l1 = Laptop("hp", 50000)
l2 = Laptop("lenovo", 60000)
l1.swap_brand(l2)
print(l1.brand)
print(l2.brand)
