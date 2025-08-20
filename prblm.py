#1
def is_palindrome(num):
     if num == num[::-1]:
        print(f"{num}Palindrome")
     else:
          print(f"{num}NOT Palindrome")

num=(input("Enter number"))
if is_palindrome(num):
    print(f'{num} is Palimdrome')
else:
    print(f'{num}is not a palindrome')

#2
def is_Armstrong(num):
    num_str = str(num)
    num_digit= len(num_str)
    total = sum(int )
    return total == num
if is_Armstrong(num):
        print(f'{num} is an armstrong')
else:
        print(f'{num} is not armstrong')



#3
def is_factorial(n):
    if n == 1:
        return True  # 0! and 1! = 1
    i = 1
    fact = 1
    while fact < n:
        i += 1
        fact *= i
    return fact == n

number = int(input("Enter a number: "))
if is_factorial(number):
    print(f"{number} is a factorial of some number.")
else:
    print(f"{number} is NOT a factorial.")
