s = "abbxxxxzzy"  
result = []
i = 0
for j in range(len(s)):
    if j == len(s) - 1 or s[j] != s[j + 1]:
        if j - i + 1 >= 3:
            result.append([i, j])
        i = j + 1

# Print the result
print(result)
