import math
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
n = len(points)
min_distance = float('inf')
closest_pair = None
for i in range(n):
    for j in range(i + 1, n):
        distance = math.sqrt((points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_pair = (points[i], points[j])
if closest_pair:
    print(f"The closest pair of points is: {closest_pair} with a distance of {min_distance:.2f}")
