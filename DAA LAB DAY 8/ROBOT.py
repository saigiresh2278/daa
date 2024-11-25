# Define the grid dimensions
m = 3
n = 7

# Initialize a 2D list with dimensions m x n
dp = [[1] * n for _ in range(m)]

# Fill the dp table
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

# The number of unique paths to the bottom-right corner
result = dp[m-1][n-1]

# Output the result
print(result)  # Expected output: 28
