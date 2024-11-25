# Given array
nums = [1, 2, 3, 1, 1, 3]

# Initialize a counter for good pairs
good_pairs_count = 0

# Iterate through the array to find good pairs
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            good_pairs_count += 1

# Output the result
print(good_pairs_count)  # Expected output: 4
