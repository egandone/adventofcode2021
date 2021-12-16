from collections import defaultdict
import sys

INF = sys.maxsize


def get_neigbours(r, c, grid):
    neighbours = {}
    # if r > 0:
    #     neighbours[(r - 1, c)] = grid[r - 1][c]
    if r + 1 < len(grid):
        neighbours[(r + 1, c)] = grid[r + 1][c]
    # if c > 0:
    #     neighbours[(r, c - 1)] = grid[r][c - 1]
    if c + 1 < len(grid[c]):
        neighbours[(r, c + 1)] = grid[r][c + 1]
    return neighbours


def get_min_cost_path(start, end, visited, graph, costs):
    #    print(f"checking {start} -> {end} {visited}")
    if start == end:
        return 0

    visited.append(start)

    ans = INF

    for n in graph[start]:
        if n not in visited:
            curr = get_min_cost_path(n, end, visited, graph, costs)
            if curr < INF:
                ans = min(ans, curr + costs[(start, n)])

    visited.pop()
    return ans


grid = []
with open("input.txt") as input:
    for line in input.readlines():
        grid.append([int(c) for c in line.strip()])
print(grid)

graph = defaultdict(list)
costs = {}
for r in range(len(grid)):
    for c in range(len(grid[r])):
        for point, weight in get_neigbours(r, c, grid).items():
            graph[(r, c)].append(point)
            costs[((r, c), point)] = weight
graph


min_cost = get_min_cost_path((0, 0), (99, 99), [], graph, costs)
print(min_cost)
