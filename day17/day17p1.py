# x_min, x_max = 20, 30
# y_min, y_max = -10, -5

x_min, x_max = 265, 287
y_min, y_max = -103, -58


def generate_path(v_x, v_y):
    x, y = 0, 0
    while y >= y_min and x <= x_max:
        yield (x, y)
        if v_x > 0:
            x = x + v_x
            v_x -= 1
        y = y + v_y
        v_y -= 1


def path_hit(path):
    for (x, y) in path:
        if (x_min <= x <= x_max) and (y_min <= y <= y_max):
            return (x, y)
    return None


def get_peak(path):
    return max([y for (x, y) in path])


hit_list = []
max_peak = 0
for x in range(1, x_max + 1):
    for y in range(y_min, abs(y_min) + 1):
        path = [(x, y) for (x, y) in generate_path(x, y)]
        hit = path_hit(path)
        if hit:
            hit_list.append((x, y))
            peak = get_peak(path)
            if peak > max_peak:
                max_peak = peak
#            print(f"({x},{y}): {peak} {hit} <- {path}")

print(f"highest peak = {max_peak}")
print(f"possible paths = {len(hit_list)}")
