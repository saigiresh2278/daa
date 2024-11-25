m, n, N, start_i, start_j = 2, 2, 2, 0, 0  
MOD = 10**9 + 7
dp = [[0] * n for _ in range(m)]
dp[start_i][start_j] = 1  

total_ways = 0
for _ in range(N):
    new_dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i > 0: new_dp[i][j] += dp[i - 1][j]
            if i < m - 1: new_dp[i][j] += dp[i + 1][j]
            if j > 0: new_dp[i][j] += dp[i][j - 1]
            if j < n - 1: new_dp[i][j] += dp[i][j + 1]
            new_dp[i][j] %= MOD
            if i == 0: total_ways = (total_ways + dp[i][j]) % MOD
            if i == m - 1: total_ways = (total_ways + dp[i][j]) % MOD
            if j == 0: total_ways = (total_ways + dp[i][j]) % MOD
            if j == n - 1: total_ways = (total_ways + dp[i][j]) % MOD

    dp = new_dp  
print(total_ways)
