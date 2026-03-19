def fact(n):
    if n == 0 or n == 1:   # base case (critical)
        return 1
    else:
        return n * fact(n - 1)


print(fact(6))  # 720
