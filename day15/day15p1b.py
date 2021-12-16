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
        grid.append([int(c) for c in line.strip()])
print(grid)

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

# pp.pprint(dist)
# pp.pprint(prev)

print(f"{dist[(99,99)]}")
