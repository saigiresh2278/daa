# Input arrays
startTime = [1, 2, 3, 3]
endTime = [3, 4, 5, 6]
profit = [50, 10, 40, 70]

# Combine the job information into a single list and sort by end times
jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

# Initialize the DP array with zero profit
dp = [0] * len(jobs)

# Define a function to perform binary search
def binary_search(jobs, index):
    lo, hi = 0, index - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if jobs[mid][1] <= jobs[index][0]:
            if jobs[mid][1] <= jobs[index][0]:
                lo = mid + 1
            else:
                hi = mid - 1
    return lo

# Fill the DP array
for i in range(len(jobs)):
    include_profit = jobs[i][2]
    l = binary_search(jobs, i)
    if l != 0:
        include_profit += dp[l - 1]
    dp[i] = max(include_profit, dp[i - 1])

# Output the maximum profit
print(dp[-1])  # Expected output: 120
