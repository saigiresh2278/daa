test_cases = [
    [1, 2, 3, 4, 5],    
    [7, 7, 7, 7, 7],    
    [-10, 2, 3, -4, 5]  
]
for nums in test_cases:
    max_element = nums[0]
    for num in nums:
        if num > max_element:
            max_element = num
    
    print(max_element)
