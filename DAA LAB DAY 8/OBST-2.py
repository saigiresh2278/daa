import numpy as np

# Number of keys
n = 4
# Keys and their frequencies
keys = [10, 12, 16, 21]
frequencies = [4, 2, 6, 3]

# Initialize cost and root matrices
cost = np.zeros((n+1, n+1))
root = np.zeros((n+1, n+1), dtype=int)

# Initialize weight matrix
weight = np.zeros((n+1, n+1))
for i in range(1, n+1):
    weight[i][i] = frequencies[i-1]
for l in range(2, n+1):
    for i in range(1, n-l+2):
        j = i + l - 1
        weight[i][j] = weight[i][j-1] + frequencies[j-1]

# Calculate cost and root matrices
for i in range(1, n+1):
    cost[i][i-1] = 0
    cost[i][i] = frequencies[i-1]
    root[i][i] = i
cost[n+1][n] = 0

for l in range(2, n+1):
    for i in range(1, n-l+2):
        j = i + l - 1
        cost[i][j] = float('inf')
        for r in range(i, j+1):
            c = cost[i][r-1] + cost[r+1][j] + weight[i][j]
            if c < cost[i][j]:
                cost[i][j] = c
                root[i][j] = r

# Function to print the OBST
def print_obst(i, j, root, keys):
    if i > j:
        return ""
    if i == j:
        return f"{keys[i-1]}"
    else:
        root_node = root[i][j]
        left_subtree = print_obst(i, root_node-1, root, keys)
        right_subtree = print_obst(root_node+1, j, root, keys)
        return f"({keys[root_node-1]}, {left_subtree}, {right_subtree})"

# Print the OBST
obst = print_obst(1, n, root, keys)
print("Optimal Binary Search Tree:", obst)

# Print the cost matrix
print("\nCost Matrix:")
for row in cost:
    print(row)

# Print the root matrix
print("\nRoot Matrix:")
for row in root:
    print(row)

# Print the cost of the OBST
print("\nCost of the Optimal Binary Search Tree:", cost[1][n])
