import itertools
cost_matrix_1 = [
    [3, 10, 7], 
    [8, 5, 12], 
    [4, 6, 9]
]

min_cost_1 = float('inf')
optimal_assignment_1 = []
for perm in itertools.permutations(range(len(cost_matrix_1))):
    assignment_1 = [(i, perm[i]) for i in range(len(cost_matrix_1))]
    total_cost_1 = sum(cost_matrix_1[i][perm[i]] for i in range(len(cost_matrix_1)))
    
    if total_cost_1 < min_cost_1:
        min_cost_1 = total_cost_1
        optimal_assignment_1 = assignment_1

print("Test Case 1:")
print("Optimal Assignment:", [(f"worker {i+1}", f"task {j+1}") for i, j in optimal_assignment_1])
print("Total Cost:", min_cost_1)

cost_matrix_2 = [
    [15, 9, 4], 
    [8, 7, 18], 
    [6, 12, 11]
]

min_cost_2 = float('inf')
optimal_assignment_2 = []

for perm in itertools.permutations(range(len(cost_matrix_2))):
    assignment_2 = [(i, perm[i]) for i in range(len(cost_matrix_2))]
    total_cost_2 = sum(cost_matrix_2[i][perm[i]] for i in range(len(cost_matrix_2)))
    
    if total_cost_2 < min_cost_2:
        min_cost_2 = total_cost_2
        optimal_assignment_2 = assignment_2

print("\nTest Case 2:")
print("Optimal Assignment:", [(f"worker {i+1}", f"task {j+1}") for i, j in optimal_assignment_2])
print("Total Cost:", min_cost_2)
