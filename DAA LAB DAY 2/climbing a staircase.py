n = 4  
if n == 1:
    total_ways = 1
elif n == 2:
    total_ways = 2
else:
    prev1, prev2 = 1, 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1 = prev2
        prev2 = current
    
    total_ways = prev2
print(total_ways)
