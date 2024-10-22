arr = [3, 5, 1, 8, 2, 7, 4, 6]
n = len(arr)
if n == 0:
    print("Array is empty.")
else:
    if n % 2 == 0:
        min_val = min(arr[0], arr[1])
        max_val = max(arr[0], arr[1])
        start_index = 2
    else:
        min_val = arr[0]
        max_val = arr[0]
        start_index = 1
    for i in range(start_index, n, 2):
        if i + 1 < n: 
            if arr[i] < arr[i + 1]:
                min_val = min(min_val, arr[i])
                max_val = max(max_val, arr[i + 1])
            else:
                min_val = min(min_val, arr[i + 1])
                max_val = max(max_val, arr[i])
        else: 
            min_val = min(min_val, arr[i])
            max_val = max(max_val, arr[i])
    print(f"Minimum element: {min_val}")
    print(f"Maximum element: {max_val}")
