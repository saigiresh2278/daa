arr = [64, 34, 25, 12, 22, 11, 90]
target = 22
n = len(arr)
found = False 
for i in range(n):
    if arr[i] == target:
        found = True
        index = i  
        break  
if found:
    print(f"Element {target} found at index: {index}")
else:
    print(f"Element {target} not found in the array.")
