# Given array of coin piles
piles = [2, 4, 1, 2, 7, 8]

# Sort the piles in descending order
piles.sort(reverse=True)

# Initialize the number of coins you can collect
your_coins = 0

# Iterate through the sorted piles and collect your coins
for i in range(1, len(piles) * 2 // 3, 2):
    your_coins += piles[i]

# Output the result
print(your_coins)  # Expected output: 9
