from itertools import combinations
array = [45, 34, 4, 12, 5, 2]
target = 50
def generate_subset_sums(array):
    subset_sums = []
    for i in range(len(array) + 1):
        for combo in combinations(array, i):
            subset_sums.append(sum(combo))
    return subset_sums
mid = len(array) // 2
left_half = array[:mid]
right_half = array[mid:]
left_sums = generate_subset_sums(left_half)
right_sums = generate_subset_sums(right_half)
right_sums.sort()
closest_sum = None
min_diff = float('inf')
for left_sum in left_sums:
    low, high = 0, len(right_sums) - 1
    while low <= high:
        mid = (low + high) // 2
        current_sum = left_sum + right_sums[mid]
        current_diff = abs(target - current_sum)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_sum = current_sum
        if current_sum < target:
            low = mid + 1
        else:
            high = mid - 1
print("Closest sum:", closest_sum)
print("Minimum difference:", min_diff)
