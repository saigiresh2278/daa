arr = [38, 27, 43, 3, 9, 82, 10]
n = len(arr)
left = 0
right = n - 1
temp = [0] * n
def merge(arr, left, mid, right):
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1
    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1
    for i in range(left, right + 1):
        arr[i] = temp[i]
size = 1
while size < n:
    left = 0
    while left < n - size:
        mid = left + size - 1
        right = min((left + 2 * size - 1), (n - 1))
        merge(arr, left, mid, right)
        left += 2 * size
    size *= 2
print("Sorted array:", arr)
