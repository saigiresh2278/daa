board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
] 

m = len(board)
n = len(board[0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

def count_live_neighbors(board, row, col):
    live_neighbors = 0
    for d in directions:
        r = row + d[0]
        c = col + d[1]
        if 0 <= r < m and 0 <= c < n and abs(board[r][c]) == 1:
            live_neighbors += 1
    return live_neighbors

for i in range(m):
    for j in range(n):
        live_neighbors = count_live_neighbors(board, i, j)
        
        if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
            board[i][j] = -1
        if board[i][j] == 0 and live_neighbors == 3:
            board[i][j] = 2

for i in range(m):
    for j in range(n):
        if board[i][j] == -1:
            board[i][j] = 0  
        elif board[i][j] == 2:
            board[i][j] = 1  

print(board)
