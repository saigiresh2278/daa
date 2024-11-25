import heapq

# Number of nodes
n = 3
# Edge list and success probabilities
edges = [[0, 1], [1, 2], [0, 2]]
succProb = [0.5, 0.5, 0.2]
# Start and end nodes
start = 0
end = 2

# Create adjacency list
graph = [[] for _ in range(n)]
for i in range(len(edges)):
    u, v = edges[i]
    prob = succProb[i]
    graph[u].append((v, prob))
    graph[v].append((u, prob))

# Dijkstra's algorithm to find the path with maximum probability
max_prob = [0.0] * n
max_prob[start] = 1.0
priority_queue = [(-1.0, start)]

while priority_queue:
    cur_prob, node = heapq.heappop(priority_queue)
    cur_prob *= -1

    if node == end:
        break

    for neighbor, edge_prob in graph[node]:
        new_prob = cur_prob * edge_prob
        if new_prob > max_prob[neighbor]:
            max_prob[neighbor] = new_prob
            heapq.heappush(priority_queue, (-new_prob, neighbor))

# Output the result
result = max_prob[end]
print(f"{result:.5f}")  # Expected output: 0.25000
