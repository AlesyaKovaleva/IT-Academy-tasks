def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = int(input('How many Fibonacci numbers to print? '))
for fib in fibonacci(count):
    print(fib)


