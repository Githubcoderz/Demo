# Program to calculate average of a list of integers with error handling

# Step 1: Get length of the list
n_input = input("Enter the length of the list: ")

if not n_input.isdigit():
    print("Error: The length of the list must be a non-negative integer.")
    exit()

n = int(n_input)

if n <= 0:
    print("Error: The length of the list must be a non-negative integer.")
    exit()

# Step 2: Get list elements
numbers = []
for i in range(n):
    num_input = input(f"Enter element {i+1}: ")
    if not num_input.lstrip('-').isdigit():
        print("Error: You must enter a numeric value.")
        exit()
    numbers.append(int(num_input))

# Step 3: Calculate average
average = sum(numbers) / n
print(f"Average: {average:.2f}")






















