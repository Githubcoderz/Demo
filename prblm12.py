#USING generator expression
start, end = 1, 10
evenNumbers = (i for i in range( start, end + 1) if i % 2 == 0)
for i in evenNumbers:
    print(i, end=' ')
print()

#USING generator function
def evenGenerator(start, end):
    for i in range(start, end + 1):
        if i % 2 == 0:
             yield i

start, end = 1, 10
evenNumbers = evenGenerator(start, end)

for i in evenNumbers:
    print(i, end=' ')
print()