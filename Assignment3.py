
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("First 30 Mersenne Numbers:")
count = 0
n = 1

while count < 30:
    mersenne = (2 ** n) - 1
    status = "P" if is_prime(mersenne) else "NP"
    print(f"2^{n} - 1 = {mersenne} --> {status}")
    count += 1
    n += 1
