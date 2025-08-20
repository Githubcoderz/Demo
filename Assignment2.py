
num = int(input("Enter any number: "))

even_numbers = []
odd_numbers = []

current = num
count = 0
while count < 5:
    if current % 2 == 0:
        even_numbers.append(current)
        count += 1
    current += 1

current = num
count = 0
while count < 5:
    if current % 2 != 0:
        odd_numbers.append(current)
        count += 1
    current += 1

if num % 2 == 0:
    print("Even:", *even_numbers)
    print("Odd:", *odd_numbers)
else:
    print("Odd:", *odd_numbers)
    print("Even:", *even_numbers)
