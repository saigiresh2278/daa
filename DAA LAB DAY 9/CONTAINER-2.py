# Given input
n = 7
weights = [5, 10, 15, 20, 25, 30, 35]
max_capacity = 50

# Sort weights in descending order to attempt larger weights first
weights.sort(reverse=True)

# Initialize the number of containers
container_count = 0

while weights:
    current_capacity = 0
    i = 0
    
    # Try to fit as many items as possible in the current container
    while i < len(weights):
        if current_capacity + weights[i] <= max_capacity:
            current_capacity += weights[i]
            weights.pop(i)
        else:
            i += 1

    # One container is used up
    container_count += 1

# Output the result
print(container_count)  # Expected output: 3
