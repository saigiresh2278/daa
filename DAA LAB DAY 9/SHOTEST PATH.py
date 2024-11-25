import heapq

# Number of vertices
n = 5
# Define the graph as an adjacency matrix
Infinity = float('inf')
graph = [
    [0, 10, 3, Infinity, Infinity],
    [Infinity, 0, 1, 2, Infinity],
    [Infinity, 4, 0, 8, 2],
    [Infinity, Infinity, Infinity, 0, 7],
    [Infinity, Infinity, Infinity, 9, 0]
]
# Source vertex
source = 0

# Initialize the distances from the source to all vertices as infinity
distances = [Infinity] * n
distances[source] = 0

# Priority queue for Dijkstra's algorithm
priority_queue = [(0, source)]

while priority_queue:
    current_distance, current_vertex = heapq.heappop(priority_queue)

    if current_distance > distances[current_vertex]:
        continue

    for neighbor in range(n):
        weight = graph[current_vertex][neighbor]
        if weight == Infinity:
            continue
        distance = current_distance + weight

        if distance < distances[neighbor]:
            distances[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))

# Output the result
print(distances)  # Expected output: [0, 7, 3, 9, 5]
