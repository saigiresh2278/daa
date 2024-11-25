poured = 2
query_row = 1
query_glass = 1
tower = [[0] * (i + 1) for i in range(query_row + 1)]
tower[0][0] = poured
for i in range(query_row):
    for j in range(i + 1):
        if tower[i][j] > 1:
            excess = tower[i][j] - 1
            tower[i][j] = 1
            tower[i + 1][j] += excess / 2
            tower[i + 1][j + 1] += excess / 2
result = min(1, tower[query_row][query_glass])
print(result)  
