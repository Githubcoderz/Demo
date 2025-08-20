
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

start = int(input("Enter a num: "))

count = 0
num = start
primes = []

while count < 25:
    if is_prime(num):
        primes.append(num)
        count += 1
    num += 1

for p in primes:
    print(p, end=" ")
print()
