def tax_amt(x):
    tax = (13/100)*x
    return tax


print(tax_amt(200))
ram = tax_amt(200000)
shyam = tax_amt(500000)
hari = tax_amt(600000)
print(ram, shyam, hari)
