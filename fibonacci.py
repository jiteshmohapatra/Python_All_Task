def fibonacci(n):
    fib_sequence = [0,1]
    while len(fib_sequence)<n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    return fib_sequence
n = int(input("enter a fibonacci term you want"))
result = fibonacci(n)
print(f"The {n}-th Fibonacci term is {result}")







