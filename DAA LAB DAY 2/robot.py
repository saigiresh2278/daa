m, n = 7, 3  
dp = [[1] * n for _ in range(m)]
for i in range(1, m):
    for j in range(1, n):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
unique_paths = dp[m - 1][n - 1]
print(unique_paths)
