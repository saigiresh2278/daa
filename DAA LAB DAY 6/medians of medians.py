arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 6
k = k - 1
sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]

if len(medians) <= 5:
    pivot = sorted(medians)[len(medians) // 2]
else:
    
    pivot_sublists = [medians[i:i+5] for i in range(0, len(medians), 5)]
    pivot_medians = [sorted(sublist)[len(sublist) // 2] for sublist in pivot_sublists]
    pivot = sorted(pivot_medians)[len(pivot_medians) // 2]
low = [x for x in arr if x < pivot]
high = [x for x in arr if x > pivot]
equal = [x for x in arr if x == pivot]
if k < len(low):
    result = sorted(low)[k]
elif k < len(low) + len(equal):
    result = pivot
else:
    result = sorted(high)[k - len(low) - len(equal)]

print("The", k + 1, "th smallest element is", result)
