points = [(10, 0), (11, 5), (5, 3), (9, 3.5), (15, 3), (12.5, 7), (6, 6.5), (7.5, 4.5)]
hull = []

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        left, right = False, False
        for k in range(len(points)):
            if k != i and k != j:
                cross_product = (points[j][1] - points[i][1]) * (points[k][0] - points[j][0]) - (points[j][0] - points[i][0]) * (points[k][1] - points[j][1])
                if cross_product > 0: left = True
                elif cross_product < 0: right = True
        if not (left and right):
            if points[i] not in hull: hull.append(points[i])
            if points[j] not in hull: hull.append(points[j])

hull.sort()
print("Convex hull:", hull)
