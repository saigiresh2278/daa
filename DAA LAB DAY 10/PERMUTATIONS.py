# Given input
nums = [1, 2, 3]

# Initialize the result list
results = []

# Define a function to generate permutations
def generate_permutations(current, remaining):
    if not remaining:
        results.append(current[:])
        return
    for i in range(len(remaining)):
        next_element = remaining[i]
        generate_permutations(current + [next_element], remaining[:i] + remaining[i+1:])

# Start the permutation generation
generate_permutations([], nums)

# Output the result
print(results)  # Expected output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
