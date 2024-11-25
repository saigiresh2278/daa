# Define the number of routers and the edges with their weights
n = 6  # Number of routers: A, B, C, D, E, F
edges = [
    [0, 1, 2],  # A to B with weight 2
    [0, 2, 4],  # A to C with weight 4
    [1, 2, 1],  # B to C with weight 1
    [1, 3, 7],  # B to D with weight 7
    [2, 4, 3],  # C to E with weight 3
    [3, 4, 2],  # D to E with weight 2
    [3, 5, 5],  # D to F with weight 5
    [4, 5, 1]   # E to F with weight 1
]

# Initialize the distance matrix with infinity and 0 for diagonal elements
INF = float('inf')
dist = [[INF] * n for _ in range(n)]
for i in range(n):
    dist[i][i] = 0

# Populate the initial distances based on the edges
for u, v, w in edges:
    dist[u][v] = w
    dist[v][u] = w  # Assuming undirected graph

# Display the distance matrix before applying Floyd's Algorithm
print("Distance matrix before applying Floyd's Algorithm:")
for row in dist:
    print(row)

# Floyd's Algorithm to find the shortest path between all pairs of routers
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Display the distance matrix after applying Floyd's Algorithm
print("\nDistance matrix after applying Floyd's Algorithm:")
for row in dist:
    print(row)

# Simulate the failure of the link between Router B and Router D (Router 1 and Router 3)
dist[1][3] = INF
dist[3][1] = INF

# Recalculate shortest paths using Floyd's Algorithm after the link failure
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Display the distance matrix after the link failure
print("\nDistance matrix after link failure between Router B and Router D:")
for row in dist:
    print(row)

# Display the shortest path from Router A to Router F (Router 0 to Router 5) before and after the link failure
print("\nShortest path from Router A to Router F:", dist[0][5])
