arr = [12, 3, 5, 7, 19]
k = 2
sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
pivot = sorted(medians)[len(medians) // 2]
low = [x for x in arr if x < pivot]
high = [x for x in arr if x > pivot]
equal = [x for x in arr if x == pivot]
if k <= len(low):
    result = sorted(low)[k - 1]
elif k <= len(low) + len(equal):
    result = pivot
else:
    result = sorted(high)[k - len(low) - len(equal) - 1]

print("The", k, "th smallest element is", result)
