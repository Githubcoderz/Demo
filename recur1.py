def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

print(factorial(5)) 


def sum_recursive(n):
    # Base case: sum of numbers up to 0 is 0
    if n == 0:
        return 0
    # Recursive case
    else:
        return n + sum_recursive(n - 1)

print(sum_recursive(5)) 

def reverse_string(s):
    # Base case: if string is empty or has one character
    if len(s) == 0:
        return ""
    # Recursive case
    else:
        return s[-1] + reverse_string(s[:-1])

print(reverse_string("hello World"))

def reverse_list(lst):
    # Base case: if list is empty or has one element
    if len(lst) <= 1:
        return lst
    # Recursive case
    return [lst[-1]] + reverse_list(lst[:-1])

print(reverse_list([1, 2, 3, 4, 5])) 

def reverse_number(n, rev=0):
    # Base case: when n becomes 0
    if n == 0:
        return rev
    # Recursive case
    return reverse_number(n // 10, rev * 10 + n % 10)

print(reverse_number(1234))