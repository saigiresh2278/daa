from collections import Counter

# Given input
nums = [1, 1, 2]

# Initialize the result list
results = []

# Define a function to generate unique permutations
def generate_permutations(current, counter):
    if len(current) == len(nums):
        results.append(current[:])
        return
    for num in counter:
        if counter[num] > 0:
            current.append(num)
            counter[num] -= 1
            generate_permutations(current, counter)
            current.pop()
            counter[num] += 1

# Use a Counter to handle duplicates
num_counter = Counter(nums)

# Start the permutation generation
generate_permutations([], num_counter)

# Output the result
print(results)  # Expected output: [[1, 1, 2], [1, 2, 1], [2, 1, 1]]
