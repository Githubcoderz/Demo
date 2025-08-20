class Prime:
    def __init__(self, start, count):
        self.start = start
        self.count = count
        self.generated = 0
        self.num = start

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.generated >= self.count:
                raise StopIteration
            if self.is_prime(self.num):
                result = self.num
                self.generated += 1
                self.num += 1
                return result
            self.num += 1

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

prime_iter = Prime(100, 25)
for prime in prime_iter:
    print(prime, end=" ")