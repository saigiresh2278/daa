nums = [2, 3, 2]  
if len(nums) == 1:
    print(nums[0])  
else:
    prev1_rob1, prev2_rob1 = 0, 0
    for k in range(len(nums) - 1):
        temp_rob1 = prev1_rob1
        prev1_rob1 = max(prev2_rob1 + nums[k], prev1_rob1)
        prev2_rob1 = temp_rob1

    prev1_rob2, prev2_rob2 = 0, 0
    for k in range(1, len(nums)):
        temp_rob2 = prev1_rob2
        prev1_rob2 = max(prev2_rob2 + nums[k], prev1_rob2)
        prev2_rob2 = temp_rob2

    print(max(prev1_rob1, prev1_rob2)) 


nums = [1, 2, 3, 1]  

if len(nums) == 1:
    print(nums[0]) 
else:
    prev1_rob1, prev2_rob1 = 0, 0  
    for k in range(len(nums) - 1):
        temp_rob1 = prev1_rob1
        prev1_rob1 = max(prev2_rob1 + nums[k], prev1_rob1)
        prev2_rob1 = temp_rob1

    prev1_rob2, prev2_rob2 = 0, 0  
    for k in range(1, len(nums)):
        temp_rob2 = prev1_rob2
        prev1_rob2 = max(prev2_rob2 + nums[k], prev1_rob2)
        prev2_rob2 = temp_rob2

    print(max(prev1_rob1, prev1_rob2)) 
