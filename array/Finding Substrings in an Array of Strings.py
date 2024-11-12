words = ["mass", "as", "hero", "superhero"]
result = set()
for i in range(len(words)):
    for j in range(len(words)):
        if i != j and words[i] in words[j]:
            result.add(words[i])
print("Substrings found:", list(result))
