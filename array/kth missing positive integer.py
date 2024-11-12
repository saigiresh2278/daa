arr = [2, 3, 4, 7, 11]
k = 5
missing_count = 0  
current = 1 
index = 0  
while missing_count < k:
    if index < len(arr) and arr[index] == current:
        index += 1
    else:
        missing_count += 1
        if missing_count == k:
            print("The", k, "th missing positive integer is:", current)
            break
    current += 1 
