import time
def timeIt(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"Execution time for {func.__name__}: {end - start:.2f} seconds")
        return result
    return wrapper

@timeIt
def factorial(num):
    result = 1
    for i in range(2, num + 1):
        result *= i
    return result


@timeIt
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)

print("Factorial Result:", factorial(10))
print("Fibonacci Result:", fibo(5))