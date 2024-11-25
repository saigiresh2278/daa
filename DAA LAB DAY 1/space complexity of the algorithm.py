test_cases = [
    [3, 7, 3, 5, 2, 5, 9, 2],
    [-1, 2, -1, 3, 2, -2],          
    [1000000, 999999, 1000000]       
]

for nums in test_cases:
    unique_elements = []
    seen = set()  

    for num in nums:
        if num not in seen:
            unique_elements.append(num)
            seen.add(num)
    print(unique_elements)
