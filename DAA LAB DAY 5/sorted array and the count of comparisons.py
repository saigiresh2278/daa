N = 8
a = [12, 4, 78, 23, 45, 67, 89, 1]
comparison_count = 0
size = 1
while size < N:
    for start in range(0, N, 2 * size):
        mid = min(start + size, N)
        end = min(start + 2 * size, N)
        left = a[start:mid]
        right = a[mid:end]
        i = j = 0
        for k in range(start, end):
            if i < len(left) and (j >= len(right) or left[i] <= right[j]):
                a[k] = left[i]
                i += 1
            else:
                a[k] = right[j]
                j += 1
            comparison_count += 1
    size *= 2
print("Sorted Array:", a)
print("Number of Comparisons:", comparison_count)
