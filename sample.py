# Sample input list
numbers = [1234, 5678, 24680, 13579, 0]

# Lambda function to process each number
process_number = lambda num: (
    sum(int(d)**2 for d in str(num) if int(d) % 2 == 0) / (count := sum(1 for d in str(num) if int(d) % 2 == 1))
    if count != 0 else 0
)

# Apply to each number
results = list(map(process_number, numbers))

print("Results:", results)

from statistics import median

# Sample input list
rainfall_data = [5.2, 12.3, 15.6, 8.4, 11.1]

# Filter values > 10 mm
filtered = list(filter(lambda x: x > 10, rainfall_data))

# Calculate median
median_value = round(median(filtered), 1) if filtered else 0.0

print("Median Rainfall:", median_value)
