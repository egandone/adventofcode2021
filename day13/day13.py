import pprint

pp = pprint.PrettyPrinter()


def do_xfold(points, x):
    new_points = set()
    for (ptx, pty) in points:
        if ptx > x:
            ptx = 2 * x - ptx
        new_points.add((ptx, pty))
    return new_points


def do_yfold(points, y):
    new_points = set()
    for (ptx, pty) in points:
        if pty > y:
            pty = 2 * y - pty
        new_points.add((ptx, pty))
    return new_points


points = set()
folds = []
reading_points = True
with open("input.txt") as input:
    for line in input.readlines():
        line = line.strip()
        if not line:
            reading_points = False
        elif reading_points:
            point = line.split(",")
            point = (int(point[0]), int(point[1]))
            points.add(point)
        else:
            parse = line.split("=")
            coord = int(parse[1].strip())
            dir = parse[0][-1]
            folds.append((dir, coord))

pp.pprint(points)
pp.pprint(folds)
print(f"starting points = {len(points)}")
for fold in folds:
    if fold[0] == "x":
        points = do_xfold(points, fold[1])
    else:
        points = do_yfold(points, fold[1])
    print(f"after {fold} - {len(points)}")

max_x = max([x for x, y in points])
max_y = max([y for x, y in points])
lines = []
for y in range(max_y + 1):
    line = []
    for x in range(max_x + 1):
        line.append(" ")
    lines.append(line)
for (x, y) in points:
    lines[y][x] = "#"
for line in lines:
    print("".join(line))
