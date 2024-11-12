m, n, N, i, j = 2, 2, 2, 0, 0
dp = [[[0 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
dp[i][j][0] = 1
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
count = 0
for steps in range(1, N+1):
    dp_temp = [[[0 for _ in range(N+1)] for _ in range(n)] for _ in range(m)]
    for x in range(m):
        for y in range(n):
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    dp_temp[nx][ny][steps] += dp[x][y][steps-1]
                else:
                    count += dp[x][y][steps-1]
    dp = dp_temp
print(count)
