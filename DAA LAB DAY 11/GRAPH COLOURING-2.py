# Given input
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
n = 4
k = 3  # Number of people coloring, including you, Alice, and Bob

# Convert edges to adjacency list
adj_list = [[] for _ in range(n)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Function to perform graph coloring
def graph_coloring(adj_list, n):
    colors = [-1] * n
    available_colors = [False] * n

    # Assign the first color to the first vertex
    colors[0] = 0

    # Assign colors to remaining vertices
    for u in range(1, n):
        # Mark all adjacent vertices' colors as unavailable
        for v in adj_list[u]:
            if colors[v] != -1:
                available_colors[colors[v]] = True

        # Find the first available color
        color = 0
        while color < n and available_colors[color]:
            color += 1

        # Assign the found color to the current vertex
        colors[u] = color

        # Reset the available_colors array for the next vertex
        for v in adj_list[u]:
            if colors[v] != -1:
                available_colors[colors[v]] = False

    return colors

# Perform graph coloring
coloring_result = graph_coloring(adj_list, n)

# Function to simulate the coloring process
def simulate_coloring(adj_list, n, k, colors):
    colored_by_you = 0
    colored = [False] * n
    turn = 0  # 0 for you, 1 for Alice, 2 for Bob

    for _ in range(n):
        # Find the next region to color
        for i in range(n):
            if not colored[i]:
                colored[i] = True
                if turn == 0:
                    colored_by_you += 1
                break
        
        # Move to the next person's turn
        turn = (turn + 1) % k

    return colored_by_you

# Simulate the coloring process and find the number of regions you color
regions_colored_by_you = simulate_coloring(adj_list, n, k, coloring_result)

# Output the result
print("Coloring of the graph:", coloring_result)
print("Number of regions
