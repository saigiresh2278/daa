nums = [1, 2, 1]
n = len(nums)
result = 0
for i in range(n):
    unique_elements = set()
    for j in range(i, n):
        unique_elements.add(nums[j])
        distinct_count = len(unique_elements)  
        result += distinct_count ** 2  
print(result) 
