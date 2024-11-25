n1 = [4, 3, 2, 3, 1]
n2 = [2, 2, 5, 2, 3, 6]
ans1 = sum(1 for x in n1 if x in n2)
ans2 = sum(1 for x in n2 if x in n1)
print([ans1, ans2])
