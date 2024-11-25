test_cases = [
    [],      
    [5]      
]

for nums in test_cases:
    if not nums:
        print("The list is empty.")
    else:
        nums.sort()
        max_element = nums[-1]
        
        print(max_element)
