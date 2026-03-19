def is_prime(x):
    for i in range(2, x):
        if i == x:
            continue

        elif x % i == 0:
            break
    else:
        return x


def print_prime(number):
    for each in range(1, number):
        if (is_prime(each)):
            print(each)


print_prime(34)
