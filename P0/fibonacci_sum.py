def fibonacci(n):
    n1 = n3 = 0
    n2 = 1
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        for i in range(n - 2):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        return n3


def sum_fibonacci(n):
    x = 0
    for i in range(n):
        x = x + i + 1
    return x


number = int(input("Introduce the last number for the fibonacci sum: "))
part1 = fibonacci(number)
result = sum_fibonacci(part1)

print("The result of the sum is: {}".format(result))

