sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_value = 5
low = 0
high = len(sorted_array) - 1
result = -1 
while low <= high:
    mid = (low + high) // 2 
    if sorted_array[mid] == target_value:
        result = mid 
        break 
    elif sorted_array[mid] < target_value:
        low = mid + 1  
    else:
        high = mid - 1
if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array.")
