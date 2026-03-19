def composite(x):
    for each in range(1, x):
        print(each)
        for i in range(2, each):
            if x % each == 0:
                return x


print(composite(10))
