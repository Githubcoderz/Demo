def is_even(num):
    return num % 2 == 0

assert is_even(2) == True
assert is_even(7) == False
assert is_even(10) == True
print('*' * 40)
 


def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

assert is_leap(1992) == True
assert is_leap(1900) == False
assert is_leap(2025) == False
print('*' * 40)
 

def count_ones(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

assert count_ones(0) == 0           
assert count_ones(5) == 2           
assert count_ones(15) == 4    
print('*' * 40)


def is_bit(num, pos):
    return (num & (1 << pos)) != 0

def test_is_bit():
    assert is_bit(10, 3) == True     
    assert is_bit(10, 1) == True     
    assert is_bit(10, 2) == False    
