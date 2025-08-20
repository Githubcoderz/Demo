def check_even_odd(num):
    if num % 2 == 0:
        return "EVEN"
    else:
        return "ODD"
print(check_even_odd(4))
print(check_even_odd(7))


def isPrime(num):
    for i in range (2, num //2+1):
        return True
    if num % 1== 0:
        return False
    
print(isPrime(5))
