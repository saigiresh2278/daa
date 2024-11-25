import itertools, math

cities_1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
start_city, min_distance, shortest_path = cities_1[0], float('inf'), []

for perm in itertools.permutations(cities_1[1:]):
    route = [start_city] + list(perm) + [start_city]
    total_distance = sum(math.sqrt((route[i][0] - route[i+1][0])**2 + (route[i][1] - route[i+1][1])**2) for i in range(len(route)-1))
    
    if total_distance < min_distance:
        min_distance, shortest_path = total_distance, route

print("Test Case 1:")
print("Shortest Distance:", min_distance)
print("Shortest Path:", shortest_path)

cities_2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]
start_city, min_distance, shortest_path = cities_2[0], float('inf'), []

for perm in itertools.permutations(cities_2[1:]):
    route = [start_city] + list(perm) + [start_city]
    total_distance = sum(math.sqrt((route[i][0] - route[i+1][0])**2 + (route[i][1] - route[i+1][1])**2) for i in range(len(route)-1))
    
    if total_distance < min_distance:
        min_distance, shortest_path = total_distance, route

print("\nTest Case 2:")
print("Shortest Distance:", min_distance)
print("Shortest Path:", shortest_path)
