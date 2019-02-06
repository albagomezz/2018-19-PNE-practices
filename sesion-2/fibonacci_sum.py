def fibonacci(n):
    if n <= 0:
        return print("0")
    else:
        x= (n-1)+(n-2)
        return x
num = int(input("Enter the number of term: "))
def fibonacci_sum(n):
    i = 0
    for a in range(n):
        i = fibonacci(n)+i+1
    return print(i)
fibonacci_sum(num)