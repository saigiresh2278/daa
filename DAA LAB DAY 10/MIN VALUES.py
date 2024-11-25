# Given input
arr = [3, 1, 2, 4]

# Define constants
MOD = 10**9 + 7

# Initialize variables
stack = []
result = 0
current_sum = 0

# Iterate through the array
for i, num in enumerate(arr):
    count = 1
    while stack and stack[-1][0] >= num:
        val, cnt = stack.pop()
        count += cnt
        current_sum -= val * cnt
    stack.append((num, count))
    current_sum += num * count
    result += current_sum
    result %= MOD

# Output the result
print(result)  # Expected output: 17
