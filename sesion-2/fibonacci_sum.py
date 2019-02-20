def fibonacci(n):
    if n <= 1:
        return n
    else:
        x = fibonacci(n-1)+fibonacci(n-2)
        return x

def fibonacci_sum(n):
    i = 0
    for a in range(n):
        i = fibonacci(n)+i
    return print(i)

num = int(input("Enter the number of term: "))
fibonacci_sum(num)