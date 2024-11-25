arr = [-9, 3, 4, 6, 8, 9, 10, 30] 
key = 10  
left, right = 0, len(arr) - 1

while left <= right:
    mid = (left + right) // 2
    
    if arr[mid] == key:
        print(f"Element {key} is found at position {mid}")
        break
    elif arr[mid] < key:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"Element {key} is not found")
