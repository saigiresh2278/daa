nums = [1, 2, 3, 1]
n = len(nums)
low, high = 0, n - 1
while low < high:
    mid = (low + high) // 2
    if nums[mid] < nums[mid + 1]:
        low = mid + 1
    else:
        high = mid
print("Index of a peak element:", low)
