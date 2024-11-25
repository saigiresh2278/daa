import itertools

# Test Case 1
items_1 = [0, 1, 2]
weights_1 = [2, 3, 1]
values_1 = [4, 5, 3]
capacity_1 = 4

min_value_1 = 0
optimal_selection_1 = []

for r in range(1, len(items_1) + 1):
    for comb in itertools.combinations(items_1, r):
        if sum(weights_1[i] for i in comb) <= capacity_1:
            total_value_1 = sum(values_1[i] for i in comb)
            if total_value_1 > min_value_1:
                min_value_1 = total_value_1
                optimal_selection_1 = comb

print("Test Case 1:")
print("Optimal Selection:", list(optimal_selection_1))
print("Total Value:", min_value_1)

# Test Case 2
items_2 = [0, 1, 2, 3]
weights_2 = [1, 2, 3, 4]
values_2 = [2, 4, 6, 3]
capacity_2 = 6

min_value_2 = 0
optimal_selection_2 = []

for r in range(1, len(items_2) + 1):
    for comb in itertools.combinations(items_2, r):
        if sum(weights_2[i] for i in comb) <= capacity_2:
            total_value_2 = sum(values_2[i] for i in comb)
            if total_value_2 > min_value_2:
                min_value_2 = total_value_2
                optimal_selection_2 = comb

print("\nTest Case 2:")
print("Optimal Selection:", list(optimal_selection_2))
print("Total Value:", min_value_2)
