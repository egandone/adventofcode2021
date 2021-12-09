def get_adjacents(x, y, grid):
    points = []
    if x > 0:
        points.append(grid[y][x - 1])
    if (x + 1) < len(grid[y]):
        points.append(grid[y][x + 1])
    if y > 0:
        points.append(grid[y - 1][x])
    if (y + 1) < len(grid):
        points.append(grid[y + 1][x])
    return points


grid = []
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        row = [int(c) for c in line]
        grid.append(row)
print("\n".join([f"{row}" for row in grid]))

total_risk = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        adjacents = get_adjacents(x, y, grid)
        if grid[y][x] < min(adjacents):
            print(f"min @ {y},{x} = {grid[y][x]}")
            risk_level = grid[y][x] + 1
            total_risk += risk_level
print(f"total risk = {total_risk}")
