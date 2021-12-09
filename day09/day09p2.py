def get_adjacents(pt, grid):
    points = {}
    x = pt[1]
    y = pt[0]
    if x > 0:
        points[(y, x - 1)] = grid[y][x - 1]
    if (x + 1) < len(grid[y]):
        points[(y, x + 1)] = grid[y][x + 1]
    if y > 0:
        points[(y - 1, x)] = grid[y - 1][x]
    if (y + 1) < len(grid):
        points[(y + 1, x)] = grid[y + 1][x]
    return points


def compute_basin(pt, grid, basin=None):
    if not basin:
        basin = [pt]

    adjacents = get_adjacents(pt, grid)
    new_adjacents = {k: v for k, v in adjacents.items() if v != 9 and k not in basin}
    if new_adjacents:
        basin.extend(new_adjacents.keys())
        for k in new_adjacents.keys():
            basin = compute_basin(k, grid, basin)

    return basin


grid = []
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        row = [int(c) for c in line]
        grid.append(row)

sizes = []
for y in range(len(grid)):
    for x in range(len(grid[y])):
        adjacents = get_adjacents((y, x), grid)
        if grid[y][x] < min(v for v in adjacents.values()):
            basin = compute_basin((y, x), grid, None)
            sizes.append(len(basin))
            print(f"min @ {y:>2},{x:>2} = {grid[y][x]}, size = {len(basin)}")


top_three = sorted(sizes, reverse=True)[0:3]
print(f"top three: {top_three} -> {top_three[0] * top_three[1] * top_three[2]}")
