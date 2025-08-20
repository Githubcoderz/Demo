rows = 3
cols = 4

matrix = []
num = 1

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1
    matrix.append(row)

print(matrix)
