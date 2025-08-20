start = int(input("Enter a number: "))

print(f"{' ':>4}", end=" ")
for i in range(start, start + 10):
    print(f"{i:>4}", end=" ")
print()

for i in range(start, start + 10):
    print(f"{i:>4}", end=" ")
    for j in range(start, start + 10):
        print(f"{i*j:>4}", end=" ")
    print()
