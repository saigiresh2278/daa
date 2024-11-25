# Given input
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2), (2, 4), (4, 0)]
n = 5

# Convert edges to adjacency list
adj_list = [[] for _ in range(n)]
for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)

# Function to check if there exists a Hamiltonian cycle
def has_hamiltonian_cycle():
    path = [-1] * n

    def is_valid_vertex(v, pos):
        if v not in adj_list[path[pos - 1]]:
            return False
        if v in path:
            return False
        return True

    def ham_cycle_util(pos):
        if pos == n:
            if path[pos - 1] in adj_list[path[0]]:
                return True
            else:
                return False

        for v in range(n):
            if is_valid_vertex(v, pos):
                path[pos] = v
                if ham_cycle_util(pos + 1):
                    return True
                path[pos] = -1

        return False

    path[0] = 0  # Start the path with the first vertex
    if not ham_cycle_util(1):
        return False

    return True

# Check for Hamiltonian cycle
has_cycle = has_hamiltonian_cycle()

# Output the result
print(has_cycle)  # Expected output: True
