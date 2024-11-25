points = [(1, 1), (4, 6), (8, 1), (0, 0), (3, 3)]
hull = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        left, right = False, False
        for k in range(len(points)):
            if k != i and k != j:
                cross = (points[j][1] - points[i][1]) * (points[k][0] - points[j][0]) - (points[j][0] - points[i][0]) * (points[k][1] - points[j][1])
                if cross > 0: left = True
                elif cross < 0: right = True
        if not (left and right):
            if points[i] not in hull: hull.append(points[i])
            if points[j] not in hull: hull.append(points[j])

hull.sort()
print("Convex Hull:", hull)
