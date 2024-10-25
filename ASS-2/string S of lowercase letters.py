s = "abbxxxxzzy" 
result = []
start = 0
for i in range(1, len(s) + 1):
    if i == len(s) or s[i] != s[start]:
        if i - start >= 3:
            result.append([start, i - 1])  
        start = i
print(result)  

s = "abc"  
result = []
start = 0
for i in range(1, len(s) + 1):
    if i == len(s) or s[i] != s[start]:
        if i - start >= 3:
            result.append([start, i - 1]) 
        start = i
print(result)  
