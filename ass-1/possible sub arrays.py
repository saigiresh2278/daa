nums = [1, 2, 1]
n = len(nums)
total_sum = 0
for i in range(n):
    distinct_count = set()  
    for j in range(i, n):
        distinct_count.add(nums[j])  
        total_sum += len(distinct_count) ** 2  

print(total_sum)  
