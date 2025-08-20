def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) 
print(factorial(10))

def Fibonacci():
    try:
        n = int(input("Enter the number of terms: "))
        a, b = 0, 1
        for _ in range(n):
            print(a, end=' ')
            a, b = b, a + b
    except ValueError:
        print("Error: Please enter a valid integer")

print (Fibonacci())