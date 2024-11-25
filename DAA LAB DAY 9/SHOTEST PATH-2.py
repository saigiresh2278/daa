import heapq

# Number of vertices
n = 6
# Edge list
edges = [(0, 1, 7), (0, 2, 9), (0, 5, 14), (1, 2, 10), (1, 3, 15), (2, 3, 11), (2, 5, 2), (3, 4, 6), (4, 5, 9)]
# Source and target vertices
source = 0
target = 4

# Initialize the graph as an adjacency list
graph = [[] for _ in range(n)]
for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))  # Assuming undirected graph

# Initialize the distances from the source to all vertices as infinity
distances = [float('inf')] * n
distances[source] = 0

# Priority queue for Dijkstra's algorithm
priority_queue = [(0, source)]

while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_vertex == target:
        break

    if current_distance > distances[current_vertex]:
        continue

    for neighbor, weight in graph[current_vertex]:
        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))

# Output the result
result = distances[target]
print(result if result != float('inf') else -1)  # Expected output: 20
