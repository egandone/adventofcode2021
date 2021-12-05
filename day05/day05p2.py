from line import Line
from collections import Counter

with open("input.txt") as input:
    lines = [Line(l.strip()) for l in input.readlines()]

point_counter = Counter()
for line in lines:
    points = line.get_points()
    # print(f"{line} -> {points}")
    point_counter.update(points)

overlaps = [pt for pt, ct in point_counter.items() if ct >= 2]
print(f"{len(overlaps)} overlaps")
