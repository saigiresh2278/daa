array = [64, 25, 12, 22, 11]
n = len(array)
for i in range(n):
    swapped = False
    for j in range(0, n - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            swapped = True
    if not swapped:
        break
print("Sorted array:", array)
