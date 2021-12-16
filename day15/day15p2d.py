import pprint
from collections import defaultdict

pp = pprint.PrettyPrinter()

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
# for l in grid:
#     print("".join([str(n) for n in l]))
# print("---------------")

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
max_row = rows - 1
columns = len(grid[rows - 1])
max_col = columns - 1
print(f"Total size = {rows} x {columns}")

graph = dict()
for r in range(rows):
    for c in range(columns):
        neighbours = []
        # if r > 0:
        #     neighbours.append((r - 1, c))
        if r < max_row:
            neighbours.append((r + 1, c))
        # if c > 0:
        #     neighbours.append((r, c - 1))
        if c < max_col:
            neighbours.append((r, c + 1))
        graph[(r, c)] = neighbours
graph

INF = rows * columns * 9 + 1

vertex_set = set()
dist = dict()
for r in range(len(grid)):
    for c in range(len(grid[r])):
        p = (r, c)
        dist[p] = INF
        vertex_set.add(p)
dist[(0, 0)] = 0

count = len(vertex_set)
while vertex_set:
    if count % 1000 == 0:
        print(f"{count} left")
    u = min(vertex_set, key=lambda _: dist[_])
    vertex_set.remove(u)
    count -= 1

    for v in graph[u]:
        if v in vertex_set:
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt

print(f"{dist[(max_row, max_col)]}")
