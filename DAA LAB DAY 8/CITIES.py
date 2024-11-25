# Number of cities
n = 4
# Edge list with weights
edges = [[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]]
# Distance threshold
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

# Floyd-Warshall Algorithm to find the shortest path between all pairs of cities
for k in range(n):
    for i in range(n):
        for j in range(n):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

# Find the city with the smallest number of reachable cities within the distance threshold
min_reachable_cities = INF
result_city = -1

for i in range(n):
    reachable_cities = 0
    for j in range(n):
        if i != j and dist[i][j] <= distanceThreshold:
            reachable_cities += 1
    
    if reachable_cities < min_reachable_cities:
        min_reachable_cities = reachable_cities
        result_city = i
    elif reachable_cities == min_reachable_cities:
        result_city = max(result_city, i)

# Output the result
print(result_city)  # Expected output: 3
