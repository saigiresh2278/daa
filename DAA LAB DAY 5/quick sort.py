N = 9
a = [10, 16, 8, 12, 15, 6, 3, 9, 5]
low = 0
high = N - 1
stack = [(low, high)] 

while stack:
    low, high = stack.pop()
    if low < high:
        pivot = a[low]
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
