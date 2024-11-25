# Given input
A = [1, 2, 3]

# Sort the input to ensure lexicographical order
A.sort()

# Initialize the result list
subsets = []

# Define a function to generate subsets
def generate_subsets(index, current):
    subsets.append(current[:])
    for i in range(index, len(A)):
        if i > index and A[i] == A[i - 1]:
            continue
        current.append(A[i])
        generate_subsets(i + 1, current)
        current.pop()

# Start generating subsets
generate_subsets(0, [])

# Output the result
print(subsets)  # Expected output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
