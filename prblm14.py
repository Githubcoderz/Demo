#Using Comprehensive
start, end, step = 1, 10, 2
myRange = (i for i in range(start, end, step))

for i in myRange:
    print(i, end=' ')
print()


#USING function
def myRange(start, end, step=1):
    while (step > 0 and start < end) or (step < 0 and start > end):
        yield start
        start += step

# Example usage:
for i in myRange(1, 10, 2):
    print(i, end=' ')
print()