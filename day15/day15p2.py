import pprint
from collections import defaultdict
import sys

pp = pprint.PrettyPrinter()
INF = sys.maxsize


def get_neighbours(r, c, grid):
    neighbours = []
    if r > 0:
        neighbours.append((r - 1, c))
    if r + 1 < len(grid):
        neighbours.append((r + 1, c))
    if c > 0:
        neighbours.append((r, c - 1))
    if c + 1 < len(grid[c]):
        neighbours.append((r, c + 1))
    return neighbours


grid = []
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        line_length = len(line)
        widen_line = [int(c) for c in line] * 5
        for copy in range(1, 5):
            for p in range(copy * line_length, len(widen_line)):
                widen_line[p] = widen_line[p] + 1 if widen_line[p] < 9 else 1
        grid.append(widen_line)
for l in grid:
    print("".join([str(n) for n in l]))
print("---------------")

original_length = len(grid)
for i in range(4):
    for y in range(original_length):
        new_line = grid[i * original_length + y].copy()
        for _ in range(len(new_line)):
            new_line[_] = new_line[_] + 1 if new_line[_] < 9 else 1
        grid.append(new_line)

# for l in grid:
#     print("".join([str(n) for n in l]))

rows = len(grid)
columns = len(grid[rows - 1])
print(f"Total size = {rows} x {columns}")

vertex_set = set()
dist = dict()
for r in range(len(grid)):
    for c in range(len(grid[r])):
        p = (r, c)
        dist[p] = INF
        vertex_set.add(p)
dist[(0, 0)] = 0

while vertex_set:
    u = min(vertex_set, key=lambda _: dist[_])
    vertex_set.remove(u)

    for v in get_neighbours(u[0], u[1], grid):
        if v in vertex_set:
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt

print(f"{dist[(rows-1, columns-1)]}")
