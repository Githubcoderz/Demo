first = 100
lst2 = [ first + i for i in range(10) if (first + i)]
print(lst2)
print("-"*10)
first = 100
lst2 = [ first + i for i in range(100) if (first + i) % 2]
print(lst2)