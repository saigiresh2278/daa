nums = [1, 2, 3, 1]  

if len(nums) == 1:
    max_money = nums[0]
else:
    prev1, curr1 = 0, 0
    for i in range(len(nums) - 1):
        new_curr1 = max(curr1, prev1 + nums[i])
        prev1 = curr1
        curr1 = new_curr1
    max1 = curr1
    
    prev2, curr2 = 0, 0
    for i in range(1, len(nums)):
        new_curr2 = max(curr2, prev2 + nums[i])
        prev2 = curr2
        curr2 = new_curr2
    max2 = curr2
    
    max_money = max(max1, max2)

print(max_money)
