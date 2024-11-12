board = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
m = len(board)
n = len(board[0])
next_state = [[board[i][j] for j in range(n)] for i in range(m)]
directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
for i in range(m):
    for j in range(n):
        live_neighbors = 0
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < m and 0 <= nj < n:
                live_neighbors += board[ni][nj]
        if board[i][j] == 1:
            if live_neighbors < 2 or live_neighbors > 3:
                next_state[i][j] = 0
        else:
            if live_neighbors == 3:
                next_state[i][j] = 1
board = next_state
for row in board:
    print(row)
