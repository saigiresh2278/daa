nums = [1, 2, 1]
total_sum = 0
for i in range(len(nums)):
    distinct_elements = set()
    for j in range(i, len(nums)):
        distinct_elements.add(nums[j])
        distinct_count = len(distinct_elements)
        total_sum += distinct_count ** 2
print(total_sum)  
