# Given array of coins and the target
coins = [1, 4, 10]
target = 19

# Initialize the current sum that can be obtained with the given coins
current_sum = 0
# Initialize the number of coins needed to be added
coins_needed = 0

# Iterate until the current_sum reaches the target
for i in range(len(coins)):
    coins.sort()
    for coin in coins:
        if current_sum + 1 < coin:
            # Add a new coin to cover the gap
            coins.append(current_sum + 1)
            coins_needed += 1
            current_sum += current_sum + 1
        current_sum += coin
        if current_sum >= target:
            break
    if current_sum >= target:
        break

# Continue adding coins if the current_sum is still less than the target
while current_sum < target:
    coins.append(current_sum + 1)
    coins_needed += 1
    current_sum += current_sum + 1

# Output the result
print(coins_needed)  # Expected output: Minimum number of coins to be added
