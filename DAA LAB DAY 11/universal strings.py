from collections import Counter

# Given input
words1 = ["amazon", "apple", "facebook", "google", "leetcode"]
words2 = ["e", "o"]

# Function to find universal strings
def universal_strings(words1, words2):
    # Calculate the maximum frequency of each character needed from words2
    max_freq = Counter()
    for word in words2:
        word_freq = Counter(word)
        for char, freq in word_freq.items():
            max_freq[char] = max(max_freq[char], freq)

    # Check each word in words1 to see if it meets the requirement
    result = []
    for word in words1:
        word_freq = Counter(word)
        if all(word_freq[char] >= freq for char, freq in max_freq.items()):
            result.append(word)

    return result

# Find and print universal strings
universal_words = universal_strings(words1, words2)
print(universal_words)  # Expected output: ["facebook", "google", "leetcode"]
