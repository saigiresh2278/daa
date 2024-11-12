poured = 1
query_row = 1
query_glass = 1
tower = [[0] * (i + 1) for i in range(100)]
tower[0][0] = poured
for row in range(query_row + 1):
    for col in range(row + 1):
        if tower[row][col] > 1:
            overflow = tower[row][col] - 1
            tower[row][col] = 1
            if row + 1 < 100: 
                tower[row + 1][col] += overflow / 2.0
                tower[row + 1][col + 1] += overflow / 2.0
result = tower[query_row][query_glass]
print(result)
