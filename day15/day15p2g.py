from collections import defaultdict

# Based mainly on Dijkstra's algorithm to find the shortest
# weighted path
#     see https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
#
# Some improvements include
#    1) Prebuild the connection graph
#    2) Build up the vertex set as we traverse the graph
#


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

# Prime the graph for each node with the list of all
# the adjacent nodes
graph = dict()
for r in range(rows):
    for c in range(columns):
        neighbours = []
        if r > 0:
            neighbours.append((r - 1, c))
        if r < max_row:
            neighbours.append((r + 1, c))
        if c > 0:
            neighbours.append((r, c - 1))
        if c < max_col:
            neighbours.append((r, c + 1))
        graph[(r, c)] = neighbours
graph

# Worst case is to travel through each node and each node
# has weight of 9.  So no path can be larger then this.
INF = rows * columns * 9 + 1

vertex_set = set()
dist = dict()
added = set()
# Prime the distance map with infinite for each node
for r in range(len(grid)):
    for c in range(len(grid[r])):
        p = (r, c)
        dist[p] = INF

# Rather then add all the nodes to the vertex_set initially keep
# just prime it with just the first node.  But, also keep track of
# what nodes have been added so we can add new nodes as they are
# encountered during processing.  This significantly improves
# performance because searching for the smallest distance in the
# vertex_set can be very CPU intensive if the set is large.
added.add((0, 0))
vertex_set.add((0, 0))
dist[(0, 0)] = 0

iteration_counter = 0
while vertex_set:
    if iteration_counter % 1000 == 0:
        print(f"iteration {iteration_counter:>8}")
    #     print(f"    vertex size size = {len(vertex_set)}")
    #     print(f"     added size size = {len(added)}")

    u = min(vertex_set, key=lambda _: dist[_])
    vertex_set.remove(u)

    for v in graph[u]:
        # Add all the connected nodes to the vertex set if
        # they have not been previously added.
        if v not in added:
            added.add(v)
            vertex_set.add(v)
        if v in vertex_set:
            alt = dist[u] + grid[v[0]][v[1]]
            if alt < dist[v]:
                dist[v] = alt
    iteration_counter += 1
print(f"Total iterations =  {iteration_counter:>8}")
print(f"Distance to ({max_row}, {max_col}) is {dist[(max_row, max_col)]}")
