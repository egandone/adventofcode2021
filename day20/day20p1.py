import pprint

pp = pprint.PrettyPrinter()

INPUT_FILE = "input.txt"


def get_lit_count(grid):
    count = 0
    for rows in grid:
        count += len([c for c in rows if c == "#"])
    return count


def expand_grid(grid, boundary_char):
    lines = []
    for r in range(-2, len(grid) + 2):
        line = []
        if r < 0 or r >= len(grid):
            line = [boundary_char] * (len(grid[0]) + 4)
        else:
            for c in range(-2, len(grid[r]) + 2):
                if c < 0 or c >= len(grid[r]):
                    line.append(boundary_char)
                else:
                    line.append(grid[r][c])
        lines.append(line)
    return lines


def get_node_value(grid, r, c, boundary_char):
    str = []
    for y in range(r - 1, r + 2):
        for x in range(c - 1, c + 2):
            if y > 0 and y < len(grid) and x > 0 and x < len(grid[y]):
                str.append(grid[y][x])
            else:
                str.append(boundary_char)
    binary_str = "".join(["0" if c == "." else "1" for c in str])
    return int(binary_str, 2)


with open(INPUT_FILE) as input:
    mappings = [c for c in input.readline().strip()]
    if len(mappings) != 512:
        raise ValueError(
            f"Expecting first line to contain exactly 512 characters - but actually has {len(mappings)}"
        )
    input.readline()
    grid = []
    for line in input.readlines():
        line = line.strip()
        grid.append(list(line))

print(f"input grid has {len(grid)} rows, {len(grid[0])} columns")

pp.pprint(grid)
print()

boundary_char = "."
for iterations in range(1, 51):
    grid = expand_grid(grid, boundary_char)
    #    pp.pprint(grid)
    print()

    new_grid = []
    for r in range(len(grid)):
        new_line = []
        for c in range(len(grid[r])):
            value = get_node_value(grid, r, c, boundary_char)
            new_line.append(mappings[value])
        new_grid.append(new_line)
    grid = new_grid
    #    pp.pprint(grid)

    lit_count = get_lit_count(grid)
    print(f"iteration {iterations} - lit count = {lit_count}")
    if boundary_char == ".":
        boundary_char = mappings[0]
    else:
        boundary_char = mappings[-1]
