def print_grid(grid):
    for row in grid:
        row_str = "".join([str(c) for c in row])
        print(row_str)


def increment(grid):
    new_grid = []
    for row in grid:
        new_row = [c + 1 for c in row]
        new_grid.append(new_row)
    return new_grid


def find_flashes(grid, excludes):
    flashes = []
    for r, row in enumerate(grid):
        for c, col in enumerate(row):
            if grid[r][c] >= 10 and (r, c) not in excludes:
                flashes.append((r, c))
    return flashes


def perform_flash(pt, grid):
    start_r = pt[0] - 1 if pt[0] > 1 else 0
    end_r = pt[0] + 1 if pt[0] + 1 < len(grid) else len(grid) - 1
    for r in range(start_r, end_r + 1):
        start_c = pt[1] - 1 if pt[1] > 1 else 0
        end_c = pt[1] + 1 if pt[1] + 1 < len(grid[r]) else len(grid[r]) - 1
        for c in range(start_c, end_c + 1):
            if (r, c) != pt:
                grid[r][c] += 1
    return grid


def reset_flashed(grid):
    new_grid = []
    for row in grid:
        new_row = [c if c < 10 else 0 for c in row]
        new_grid.append(new_row)
    return new_grid


def perform_iteration(grid):
    grid = increment(grid)
    all_flashes = []
    new_flashes = find_flashes(grid, all_flashes)
    while new_flashes:
        for flash in new_flashes:
            grid = perform_flash(flash, grid)
        all_flashes.extend(new_flashes)
        new_flashes = find_flashes(grid, all_flashes)
    grid = reset_flashed(grid)
    return grid, len(all_flashes)


grid = []
with open("input.txt") as input:
    for line in [l.strip() for l in input.readlines()]:
        row = [int(c) for c in line]
        grid.append(row)
print_grid(grid)
total_flashes = 0
print("--- Iteration 1 ---")
grid, flash_count = perform_iteration(grid)
total_flashes += flash_count
print_grid(grid)
print("--- Iteration 2 ---")
grid, flash_count = perform_iteration(grid)
total_flashes += flash_count
print_grid(grid)
iterations = 2
while iterations < 100:
    grid, flash_count = perform_iteration(grid)
    total_flashes += flash_count
    iterations += 1
print(f"--- after step {iterations} - {total_flashes} flashes ---")
print_grid(grid)
