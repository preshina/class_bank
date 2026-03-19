def total(rate, quantity):
    grand_total = rate*quantity
    return grand_total


t1 = total(4, 2)
t2 = total(5, 6)
t3 = total(50, 12)

full_amt = t1+t2+t3
print(full_amt)
print(t1)
