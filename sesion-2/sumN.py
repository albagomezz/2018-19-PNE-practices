def sum(n):
    x = 0
    for a in range(n):
        x = x + a + 1
    return print(x)

numbers = int(input("Enter the numbers to sum: "))
sum(numbers)
