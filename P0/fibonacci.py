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


number = int(input("Introduce the number: "))
result = fibonacci(number)
print("The result for the number introduced is: {}".format(result))