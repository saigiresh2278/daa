# Given input
n = 5
weights = [10, 20, 30, 40, 50]
max_capacity = 60

# Sort the weights in descending order
weights.sort(reverse=True)

# Initialize the total weight loaded into the container
total_weight = 0

# Iterate through the sorted weights and add them to the container
for weight in weights:
    if total_weight + weight <= max_capacity:
        total_weight += weight
    else:
        break

# Output the result
print(total_weight)  # Expected output: 50
