X = 1234
Y = 5678
X_str = str(X)
Y_str = str(Y)
n = max(len(X_str), len(Y_str))
m = n // 2
high_X = int(X_str[:-m] or '0')
low_X = int(X_str[-m:])
high_Y = int(Y_str[:-m] or '0')
low_Y = int(Y_str[-m:])
z0 = low_X * low_Y
z1 = (low_X + high_X) * (low_Y + high_Y)
z2 = high_X * high_Y
Z = z2 * 10**(2 * m) + (z1 - z2 - z0) * 10**m + z0

print("The product Z is:", Z)
