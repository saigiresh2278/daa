from collections import deque

# Input graph
graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]

# Game result constants
MOUSE = 1
CAT = 2
DRAW = 0

# Number of nodes
n = len(graph)

# Initialize the states (mouse position, cat position, turn) -> result
dp = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]

# Queue for BFS
queue = deque()

# Base cases
for i in range(1, n):
    dp[0][i][0] = MOUSE  # If mouse is at hole, mouse wins
    dp[0][i][1] = MOUSE  # If mouse is at hole, mouse wins
    queue.append((0, i, 0, MOUSE))
    queue.append((0, i, 1, MOUSE))

    dp[i][i][0] = CAT  # If cat catches mouse, cat wins
    dp[i][i][1] = CAT  # If cat catches mouse, cat wins
    queue.append((i, i, 0, CAT))
    queue.append((i, i, 1, CAT))

# Perform BFS to determine the outcomes
while queue:
    mouse_pos, cat_pos, turn, result = queue.popleft()

    if turn == 0:  # Mouse's turn
        for next_mouse_pos in graph[mouse_pos]:
            if dp[next_mouse_pos][cat_pos][1] == DRAW:
                if result == MOUSE:
                    dp[next_mouse_pos][cat_pos][1] = MOUSE
                    queue.append((next_mouse_pos, cat_pos, 1, MOUSE))
                elif all(dp[neigh][cat_pos][1] == CAT for neigh in graph[mouse_pos]):
                    dp[next_mouse_pos][cat_pos][1] = CAT
                    queue.append((next_mouse_pos, cat_pos, 1, CAT))
    else:  # Cat's turn
        for next_cat_pos in graph[cat_pos]:
            if next_cat_pos != 0 and dp[mouse_pos][next_cat_pos][0] == DRAW:
                if result == CAT:
                    dp[mouse_pos][next_cat_pos][0] = CAT
                    queue.append((mouse_pos, next_cat_pos, 0, CAT))
                elif all(dp[mouse_pos][neigh][0] == MOUSE for neigh in graph[cat_pos] if neigh != 0):
                    dp[mouse_pos][next_cat_pos][0] = MOUSE
                    queue.append((mouse_pos, next_cat_pos, 0, MOUSE))

# Output the result from the initial position (mouse at 1, cat at 2, mouse's turn)
result = dp[1][2][0]
print(result)  # Expected output is 0 for draw
