import math
points = [(1, 2), (4, 5), (7, 8), (3, 1)]
min_distance = float('inf')
closest_pair = (None, None)
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        point1, point2 = points[i], points[j]
        distance = math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
        
        if distance < min_distance:
            min_distance = distance
            closest_pair = (point1, point2)

print(f"Closest pair: {closest_pair[0]} - {closest_pair[1]}")
print(f"Minimum distance: {min_distance}")
