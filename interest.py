# def interest(p, t, r):
#     interest = (p*t*r)/100
#     return interest


# print(interest(100, 2, 2))
# print(interest(200, 4, 6))

# def compound_interest(p, r, n, t):
#     amount = p*(1+r/n)**(n*t)
#     return amount


# print(compound_interest(2, 4, 1, 1))

def total(rate, quantity):
    grand_total = rate*quantity
    return grand_total


print(total(4, 2))
print(total(5, 6))
print(total(50, 12))
