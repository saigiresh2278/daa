arr = [10, 7, 8, 9, 1, 5]
stack = []
low = 0
high = len(arr) - 1
stack.append((low, high))
while stack:
    low, high = stack.pop()
    if low < high:
        pivot = arr[high]
        i = low - 1  
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i] 
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        pivot_index = i + 1
        stack.append((low, pivot_index - 1)) 
        stack.append((pivot_index + 1, high))
print("Sorted array:", arr)
