
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("First 8 Mersenne prime numbers:")

count = 0
p = 2

while count < 8:
    mersenne = 2 ** p - 1
    if is_prime(mersenne):
        count += 1
        print(f"Mersenne prime #{count}: 2^{p} - 1 = {mersenne}")
    p += 1
