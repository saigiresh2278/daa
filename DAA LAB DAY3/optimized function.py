nums1 = [64, 25, 12, 22, 11]
n1 = len(nums1)
for i in range(n1):
    swapped = False
    for j in range(0, n1-i-1):
        if nums1[j] > nums1[j+1]:
            nums1[j], nums1[j+1] = nums1[j+1], nums1[j]
            swapped = True
    if not swapped:
        break
print("Sorted array 1:", nums1)

nums2 = [29, 10, 14, 37, 13]
n2 = len(nums2)
for i in range(n2):
    swapped = False
    for j in range(0, n2-i-1):
        if nums2[j] > nums2[j+1]:
            nums2[j], nums2[j+1] = nums2[j+1], nums2[j]
            swapped = True
    if not swapped:
        break
print("Sorted array 2:", nums2)

nums3 = [3, 5, 2, 1, 4]
n3 = len(nums3)
for i in range(n3):
    swapped = False
    for j in range(0, n3-i-1):
        if nums3[j] > nums3[j+1]:
            nums3[j], nums3[j+1] = nums3[j+1], nums3[j]
            swapped = True
    if not swapped:
        break
print("Sorted array 3:", nums3)

nums4 = [1, 2, 3, 4, 5]
n4 = len(nums4)
for i in range(n4):
    swapped = False
    for j in range(0, n4-i-1):
        if nums4[j] > nums4[j+1]:
            nums4[j], nums4[j+1] = nums4[j+1], nums4[j]
            swapped = True
    if not swapped:
        break
print("Sorted array 4:", nums4)
