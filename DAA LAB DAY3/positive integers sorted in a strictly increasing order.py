arr = [2, 3, 4, 7, 11]
k = 5
missing_count = 0
current = 1
i = 0

while missing_count < k:
    if i < len(arr) and arr[i] == current:
        i += 1
    else:
        missing_count += 1
        if missing_count == k:
            print(current)
            break
    current += 1
