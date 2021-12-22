import re

points = set()
adds = 0
removes = 0
with open("input.txt") as input:
    for line in input.readlines():
        match = re.match(
            "^(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$",
            line.strip(),
        )
        if match:
            (type, xmin, xmax, ymin, ymax, zmin, zmax) = match.groups()
            xmin = max(-50, int(xmin))
            xmax = min(50, int(xmax))
            ymin = max(-50, int(ymin))
            ymax = min(50, int(ymax))
            zmin = max(-50, int(zmin))
            zmax = min(50, int(zmax))
            print(f"{xmin}->{xmax}, {ymin}->{ymax}, {zmin}->{zmax}")
        else:
            raise ValueError("{line} doesn't match pattern")

        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                for z in range(zmin, zmax + 1):
                    pt = (x, y, z)
                    if type == "on":
                        points.add(pt)
                        adds += 1
                    else:
                        points.discard(pt)
                        removes += 1

print(f"{adds} adds, {removes} removes, final size = {len(points)}")
