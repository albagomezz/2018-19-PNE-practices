def fibonacci(n):
    if n <= 1:
        return n
    else:
        x = fibonacci(n-1)+fibonacci(n-2)
        return x
num = int(input("Enter the number of term: "))
print(fibonacci(num))