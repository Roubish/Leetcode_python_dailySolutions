# Problem Statement:

# Given a set of 2D points, find the Convex Hull — the smallest convex polygon that encloses all the points.
# In simple terms:
# Imagine stretching a rubber band around the outermost points.
# The shape formed is the convex hull.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def polar_angle(p1, p2):
    return math.atan2(p1.y - p2.y, p1.x - p2.x)


def distance(p1, p2):
    return (p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2


def cross_product(o, a, b):
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x)


def graham_scan(points):
    # Step 1: Find lowest point
    p0 = min(points, key=lambda p: (p.y, p.x))

    # Step 2: Sort points by polar angle
    sorted_points = sorted(
        points,
        key=lambda p: (polar_angle(p, p0), distance(p, p0))
    )

    # Step 3: Build hull
    hull = []
    for p in sorted_points:
        while len(hull) >= 2 and cross_product(hull[-2], hull[-1], p) <= 0:
            hull.pop()
        hull.append(p)

    return hull



# ----------------- TEST -----------------
points = [
    Point(0, 3),
    Point(2, 2),
    Point(1, 1),
    Point(2, 1),
    Point(3, 0),
    Point(0, 0),
    Point(3, 3)
]

convex_hull = graham_scan(points)

print("Convex Hull Points:")
for p in convex_hull:
    print(p)




# Step 1: Choose Starting Point

# Select the point with:

# Lowest y coordinate

# If tie → lowest x

# This point is called p0

# Step 2: Sort by Polar Angle

# Sort remaining points based on:

# Angle made with p0

# If angles are equal:

# Keep the farthest point

# This ensures we traverse points counter-clockwise.

# Step 3: Traverse and Build Hull

# Initialize empty stack (hull)

# For each point:

# Check the orientation using cross product

# If it makes a right turn or collinear → pop last point

# Else → add the point to hull

# Step 4: Final Result

# Remaining points in the stack form the convex hull

# Space Complexity

# Hull + sorting storage → O(n)
# Output
ghost@ghost-GF65-Thin-10UE:~/Documents/program_txt_folder/dsa_code$ python3 graham_scan.py 
Convex Hull Points:
(0, 0)
(3, 0)
(3, 3)
(0, 3)
