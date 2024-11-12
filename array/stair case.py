n = 4
if n == 0:
    ways = 0
elif n == 1:
    ways = 1
else:
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    ways = dp[n]
print(ways)
