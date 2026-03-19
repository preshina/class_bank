# Create a class Student with:

# attributes: name, age

# method: display details

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_details(self):
#         print(f"the name is {self.name} and the age is {self.age}")


# d1 = Student("hari", 23)
# d1.display_details()


# Create a class Rectangle:

# attributes: length, width

# methods:

# area()

# perimeter()

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return f"the area is {self.length*self.width}"

#     def perimeter(self):
#         return f"the preimeter is {2*(self.length+self.width)}"


# d1 = Rectangle(2, 4)
# print(d1.area())
# print(d1.perimeter())

# Create a class BankAccount:

# attributes: balance

# methods:

# deposit(amount)

# withdraw(amount)

# show_balance()
# Be strict: don’t allow withdrawing more than balance.

# class BankAccount:
#     def __init__(self, balance=0):
#         self.balance = balance

#     def deposit(self, amount):
#         if amount <= 0:
#             print("Deposit must be positive")
#             return
#         self.balance += amount
#         print(f"Deposited {amount}")

#     def withdraw(self, amount):
#         if amount <= 0:
#             print("Withdrawal must be positive")
#             return
#         if amount > self.balance:
#             print("Insufficient balance")
#             return
#         self.balance -= amount
#         print(f"Withdrew {amount}")

#     def show_balance(self):
#         print(f"Current balance: {self.balance}")


# acc = BankAccount(100)

# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(200)   # should fail
# acc.show_balance()


# Create a class BankAccount with account_number and balance.
# Add a method to deposit money and another to withdraw money.

pass

# Create a class Circle with an attribute radius. Add a method to calculate the circumference.


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def circumference(self):
#         circum = 2*3.14*self.radius
#         return circum


# d1 = Circle(2)
# print(d1.circumference())

# Create a class Laptop with attributes brand and price. Add a method that prints the details in a readable format.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def details(self):
        print(f"the brand is {self.brand} and the price {self.price}")

    def discount(self):
        self.price = self.price-50000

    def change_brand(self, new_brand):
        self.brand = new_brand

    def is_more_expensive_than(self, other_laptop):
        # here self.price represents the first object u pass in, for eg: d1 is_more_expensive_than(d2): d1 lai self.price ma rakxa, ani d2 lai other object ma rakxa.
        if self.price > other_laptop.price:
            return True
        else:
            return False

    def brand_swap(self, other_brand):
        self.brand = other_brand.brand


d1 = Laptop("Hp", 500000)
d2 = Laptop("lenovo", 340000)
d1.discount()
d1.discount()
# d1.change_brand("lenovo")
d1.details()
print(d1.is_more_expensive_than(d2))
print(d2.is_more_expensive_than(d1))
d1.brand_swap(d2)
