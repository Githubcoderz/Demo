rows = 3
cols = 4

# Step 1: Create the matrix
matrix = []
num = 1
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(num)
        num += 1
    matrix.append(row)

# Step 2: Print elements in spiral order
spiral_order = []

top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:
    # Move left to right along top
    for i in range(left, right + 1):
        spiral_order.append(matrix[top][i])
    top += 1

    # Move top to bottom along right
    for i in range(top, bottom + 1):
        spiral_order.append(matrix[i][right])
    right -= 1

    if top <= bottom:
        # Move right to left along bottom
        for i in range(right, left - 1, -1):
            spiral_order.append(matrix[bottom][i])
        bottom -= 1

    if left <= right:
        # Move bottom to top along left
        for i in range(bottom, top - 1, -1):
            spiral_order.append(matrix[i][left])
        left += 1

# Print the spiral order
print("Spiral Order:", *spiral_order)
