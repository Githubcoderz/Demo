def is_even(num):
    "return true or false"
    if num%2 == 0:
        print("even")
    else:
        print("odd")
print(f'num 10 is {is_even(10)}')
print (True or False)

def isprime(num):
    "return true or false"
    if num<= 1 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num% i== 0:
            return False
            
        return True
print(f'num 7 is {isprime(7)}')



def isPalindrome(num):
    
    str_num = str(num)

    return str_num == str_num[::-1]
print(isPalindrome(121))  
print(isPalindrome(123))  




def isArmstrong(num):
    "return true or false"
    num_str= str(num)
    num_digit = len(num_str)
    sum_of_power = 0
    for digit_char in num_str:
        digit= int(digit_char)
        sum_of_power += digit ** num_digit
    return sum_of_power == num
print(f'num 153 is {isArmstrong(153)}')


def isFactorial(n):
    "return true or false"
    if n<0:
        return "Factorial not defined"
    elif n ==0:
        return 1
    else:
        return n* isFactorial(n-1)
    
print(f' n 2 is {isFactorial(2)}')


def isLeap(year):
    "return true or false"
    if (year%4 == 0 and year %100!= 0) or (year % 400 == 0):
        return True
    else:
        return False