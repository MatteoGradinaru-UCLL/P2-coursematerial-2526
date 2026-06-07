def closest(points, target_points):
    return min(points, key=lambda point: ((target_points[0] - point[0])**2 + (target_points[1] - point[1])**2)**0.5)

all_points = [(1, 1), (4, 5), (9, 2)]
target = (3, 4)

print(closest(all_points, target))