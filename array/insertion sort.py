array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
n = len(array)
for i in range(1, n):
    key = array[i]
    j = i - 1
    while j >= 0 and array[j] > key:
        array[j + 1] = array[j]
        j -= 1
    array[j + 1] = key
print("Sorted array:", array)
