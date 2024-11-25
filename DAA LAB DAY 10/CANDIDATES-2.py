# Given input
candidates = [2, 3, 6, 7]
target = 7

# Initialize the result list
results = []

# Define a function to find combinations
def find_combinations(candidates, target, current_combination, start):
    if target == 0:
        results.append(current_combination[:])
        return
    for i in range(start, len(candidates)):
        if candidates[i] <= target:
            current_combination.append(candidates[i])
            find_combinations(candidates, target - candidates[i], current_combination, i)
            current_combination.pop()

# Initialize an empty combination and start the recursion
find_combinations(candidates, target, [], 0)

# Output the result
print(results)  # Expected output: [[2, 2, 3], [7]]
