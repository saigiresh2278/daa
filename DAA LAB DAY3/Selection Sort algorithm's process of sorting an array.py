nums = [1, 2, 3, 1]
n = len(nums)
if n == 1:
    peak_index = 0
else:
    for i in range(n):
        left = nums[i-1] if i > 0 else float('-inf')
        right = nums[i+1] if i < n-1 else float('-inf')
        
        if nums[i] > left and nums[i] > right:
            peak_index = i
            break  
print("Peak index:", peak_index)
