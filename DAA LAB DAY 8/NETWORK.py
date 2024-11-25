import heapq

# Input
times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
n = 4
k = 2

# Initialize the adjacency list
graph = [[] for _ in range(n + 1)]
for u, v, w in times:
    graph[u].append((v, w))

# Initialize the distances
dist = [float('inf')] * (n + 1)
dist[k] = 0

# Priority queue for Dijkstra's algorithm
priority_queue = [(0, k)]

while priority_queue:
    cur_dist, node = heapq.heappop(priority_queue)
    
    if cur_dist > dist[node]:
        continue
    
    for neighbor, weight in graph[node]:
        distance = cur_dist + weight
        
        if distance < dist[neighbor]:
            dist[neighbor] = distance
            heapq.heappush(priority_queue, (distance, neighbor))

# Find the maximum distance
max_dist = max(dist[1:])

# Output the result
result = max_dist if max_dist != float('inf') else -1
print(result)  # Expected output: 2
