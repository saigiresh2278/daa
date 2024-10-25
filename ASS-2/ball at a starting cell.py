m = 2  
n = 2  
N = 2  
i = 0  
j = 0  

MOD = 10**9 + 7
dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
for steps in range(1, N+1):
    for r in range(m):
        for c in range(n):
            up = dp[steps-1][r-1][c] if r > 0 else 1
            down = dp[steps-1][r+1][c] if r < m-1 else 1
            left = dp[steps-1][r][c-1] if c > 0 else 1
            right = dp[steps-1][r][c+1] if c < n-1 else 1
            
            dp[steps][r][c] = (up + down + left + right) % MOD

print(dp[N][i][j])  

m = 1  
n = 3  
N = 3  
i = 0  
j = 1  

dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(N+1)]
for steps in range(1, N+1):
    for r in range(m):
        for c in range(n):
            up = dp[steps-1][r-1][c] if r > 0 else 1
            down = dp[steps-1][r+1][c] if r < m-1 else 1
            left = dp[steps-1][r][c-1] if c > 0 else 1
            right = dp[steps-1][r][c+1] if c < n-1 else 1
            
            dp[steps][r][c] = (up + down + left + right) % MOD

print(dp[N][i][j]) 
