words = ["mass", "as", "hero", "superhero"]
result = []
for i in range(len(words)):
    for j in range(len(words)):
        if i != j and words[i] in words[j]:
            result.append(words[i])
            break  

print(result)
