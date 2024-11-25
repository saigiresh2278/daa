from itertools import combinations
set_array = [1, 3, 9, 2, 7, 12]
target_sum = 15
mid = len(set_array) // 2
left_half = set_array[:mid]
right_half = set_array[mid:]
left_sums = set()
for i in range(len(left_half) + 1):
    for combo in combinations(left_half, i):
        left_sums.add(sum(combo))

right_sums = set()
for i in range(len(right_half) + 1):
    for combo in combinations(right_half, i):
        right_sums.add(sum(combo))
if target_sum in left_sums:
    result = True
else:
   
    result = any((target_sum - right_sum) in left_sums for right_sum in right_sums)

print( result)
