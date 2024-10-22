words = ["abc", "car", "ada", "racecar", "cool"]
result = ""
for word in words:
    if word == word[::-1]:  
        result = word
        break  
print(result)  
