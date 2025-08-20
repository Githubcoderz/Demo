a,b = 0,1
n= 5
lst = [a+b for i in range(n)]
print()



def fiboGenerator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fiboGenerator(5):
    print(num, end=' ')