points = [(0, 0), (1, 1), (2, 2), (2, 0), (1, 0), (0, 2)]
def is_left(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]) > 0
hull = []
n = len(points)
for i in range(n):
    for j in range(n):
        if i != j:
            on_left = True
            for k in range(n):
                if k != i and k != j:
                    if not is_left(points[i], points[j], points[k]):
                        on_left = False
                        break
            if on_left:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])
print("Convex Hull points:")
for point in hull:
    print(point)
