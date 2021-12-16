import pprint
from collections import defaultdict
from graph import Graph, dijsktra

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

graph = Graph()
for r in range(rows):
    for c in range(columns):
        graph.add_node((r, c))
        if r > 0:
            graph.add_edge((r, c), (r - 1, c), grid[r - 1][c])
        if r < max_row:
            graph.add_edge((r, c), (r + 1, c), grid[r + 1][c])
        if c > 0:
            graph.add_edge((r, c), (r, c - 1), grid[r][c - 1])
        if c < max_col:
            graph.add_edge((r, c), (r, c + 1), grid[r][c + 1])

visited, path = dijsktra(graph, (0, 0))

# print(visited)
# dist = sum(grid[r][c] for r, c in path.keys())
print(visited[(max_col, max_row)])
