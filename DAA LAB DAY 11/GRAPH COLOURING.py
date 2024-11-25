# Given input
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4

# Convert edges to adjacency list
adj_list = [[] for _ in range(n)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Function to perform graph coloring
def graph_coloring(adj_list, n):
    # Initialize color assignment array
    colors = [-1] * n
    # Initialize available colors array
    available = [False] * n
    
    # Assign the first color to the first vertex
    colors[0] = 0
    
    # Assign colors to remaining vertices
    for u in range(1, n):
        # Mark all adjacent vertices' colors as unavailable
        for v in adj_list[u]:
            if colors[v] != -1:
                available[colors[v]] = True
        
        # Find the first available color
        color = 0
        while color < n and available[color]:
            color += 1
        
        # Assign the found color to the current vertex
        colors[u] = color
        
        # Reset the available array for the next vertex
        for v in adj_list[u]:
            if colors[v] != -1:
                available[colors[v]] = False
    
    return colors

# Perform graph coloring
coloring_result = graph_coloring(adj_list, n)

# Output the result
print("Coloring of the graph:", coloring_result)
