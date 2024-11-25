N = 8
a = [19, 72, 35, 46, 58, 91, 22, 31]
low = 0
high = N - 1
stack = [(low, high)]
while stack:
    low, high = stack.pop()
    if low < high:
        mid = low + (high - low) // 2
        pivot = a[mid]
        a[low], a[mid] = a[mid], a[low]
        left = low + 1
        right = high
        done = False
        
        while not done:
            while left <= right and a[left] <= pivot:
                left = left + 1
            while a[right] >= pivot and right >= left:
                right = right - 1
            if right < left:
                done = True
            else:
                a[left], a[right] = a[right], a[left]
        a[low], a[right] = a[right], a[low]
        print(a)
        stack.append((low, right - 1))
        stack.append((right + 1, high))
print("Sorted Array:", a)
