matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

rows = len(matrix)
cols = len(matrix[0])

zero_rows = set()
zero_cols = set()

# Step 1: Find which rows and columns need to be zero
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 0:
            zero_rows.add(i)
            zero_cols.add(j)

# Step 2: Set rows to zero
for i in zero_rows:
    for j in range(cols):
        matrix[i][j] = 0

# Step 3: Set columns to zero
for j in zero_cols:
    for i in range(rows):
        matrix[i][j] = 0

# Print the result
for row in matrix:
    print(row)
