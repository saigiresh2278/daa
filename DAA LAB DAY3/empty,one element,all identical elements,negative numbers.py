test_cases = [
    [],  
    [1],  
    [7, 7, 7, 7],  
    [-5, -1, -3, -2, -4]  
]

for i, test_case in enumerate(test_cases):
    print(f"Test Case {i + 1}:")
    print(f"Input: {test_case}")
    
    sorted_list = sorted(test_case)
    
    print(f"Output: {sorted_list}")
    print()  
