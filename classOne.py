class NumOps:
    def __init__(self, num): 
        self.num = num

    def isEven(self):
        return self.num % 2 == 0

    def isPrime(self):
        if self.num <= 1:
            return False
        for i in range(2, int(self.num**0.5) + 1):
            if self.num % i == 0:
                return False
        return True

    def isArmstrong(self):
        digits = str(self.num)
        power = len(digits)
        total = sum(int(d)**power for d in digits)
        return total == self.num

if __name__ == '__main__':
    obj = NumOps(10)
    print(f"10 is even {obj.isEven()}")
    print(f"10 is prime {obj.isPrime()}")
    print(f"10 is Armstrong {obj.isArmstrong()}")

    obj1 = NumOps(153)
    print(f'153 is even  {obj1.isEven()}')
    print(f'153 is prime {obj1.isPrime()}')
    print(f'153 is Armstrong  {obj1.isArmstrong()}')

    obj2 = NumOps(101)
    print(f'101 is even {obj2.isEven()}')
    print(f'101 is prime {obj2.isPrime()}')
    print(f'101 is Armstrong {obj2.isArmstrong()}')