def fibonacci(n):
    for a in range(n+1):
        x = fibonacci(a-1)+fibonacci(a-2)
        return x
num = int(input("Enter the number of term: "))
print(fibonacci(num))