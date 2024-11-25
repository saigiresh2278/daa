# Given input
nums = [1, 1, 1, 1, 1]
target = 3

# Calculate the total sum of nums
total_sum = sum(nums)

# Check if the target is possible
if (total_sum + target) % 2 != 0 or total_sum < target:
    print(0)
else:
    # Calculate the subset sum we need to find
    subset_sum = (total_sum + target) // 2

    # Initialize the dp array
    dp = [0] * (subset_sum + 1)
    dp[0] = 1  # There is one way to get sum 0, by not picking any element

    # Fill the dp array
    for num in nums:
        for s in range(subset_sum, num - 1, -1):
            dp[s] += dp[s - num]

    # Output the result
    print(dp[subset_sum])  # Expected output: 5
