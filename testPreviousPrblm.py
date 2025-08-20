def is_even(num):
    return num % 2 == 0

assert is_even(2) == True
assert is_even(7) == False
assert is_even(10) == True



def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap(1992) == True
assert is_leap(1900) == False
assert is_leap(2025) == False