# Number of cities
n = 4
# Edges with weights
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
# Distance threshold (not used in this implementation but provided in the input)
distanceThreshold = 4

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

# Floyd's Algorithm to find the shortest path between all pairs of cities
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Display the distance matrix after applying Floyd's Algorithm
print("\nDistance matrix after applying Floyd's Algorithm:")
for row in dist:
    print(row)

# Identify the shortest path (finding the minimum distance excluding the diagonal)
min_dist = INF
for i in range(n):
    for j in range(n):
        if i != j and dist[i][j] < min_dist:
            min_dist = dist[i][j]

# Print the shortest path distance
print("\nThe shortest path distance is:", min_dist)
