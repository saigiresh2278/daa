# Part 1: Subsets Containing the Specific Element 3
E = [2, 3, 4, 5]
x = 3

# Function to generate all subsets that contain the specific element
def subsets_with_element(E, x):
    subsets = []
    n = len(E)
    for i in range(1 << n):
        subset = [E[j] for j in range(n) if (i & (1 << j))]
        if x in subset:
            subsets.append(subset)
    return subsets

# Generate subsets containing 3
subsets_containing_x = subsets_with_element(E, x)
print("Subsets containing 3:", subsets_containing_x)

# Part 2: Power Set
nums = [1, 2, 3]

# Function to generate all possible subsets (power set)
def power_set(nums):
    subsets = []
    n = len(nums)
    for i in range(1 << n):
        subset = [nums[j] for j in range(n) if (i & (1 << j))]
        subsets.append(subset)
    return subsets

# Generate all possible subsets
all_subsets = power_set(nums)
print("All subsets:", all_subsets)
