set_elements = [1, 2, 3]
n = len(set_elements)
subsets = []
for i in range(1 << n): 
    subset = []
    for j in range(n):
        if (i & (1 << j)) > 0:
            subset.append(set_elements[j])
    subsets.append(subset)
print("All subsets:")
for subset in subsets:
    print(subset)
