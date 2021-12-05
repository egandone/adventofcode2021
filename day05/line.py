import re


class Line:
    def __init__(self, str):
        m = re.match(r"(\d+)\D+(\d+)\D+(\d+)\D+(\d+)", str)
        if not m:
            raise ValueError(
                f'The input string "{str}" does not match the expected pattern'
            )
        x1 = int(m.groups()[0])
        y1 = int(m.groups()[1])
        x2 = int(m.groups()[2])
        y2 = int(m.groups()[3])
        self.start = (x1, y1)
        self.end = (x2, y2)
        self.is_horizontal = y1 == y2
        self.is_vertical = x1 == x2

    def get_points(self):
        points = []
        if self.is_horizontal:
            y = self.start[1]
            dx = 1 if self.end[0] >= self.start[0] else -1
            for x in range(self.start[0], self.end[0] + dx, dx):
                points.append((x, y))
        elif self.is_vertical:
            x = self.start[0]
            dy = 1 if self.end[1] >= self.start[1] else -1
            for y in range(self.start[1], self.end[1] + dy, dy):
                points.append((x, y))
        else:
            dx = 1 if self.end[0] >= self.start[0] else -1
            dy = 1 if self.end[1] >= self.start[1] else -1
            (x, y) = self.start
            points.append((x, y))
            while (x, y) != self.end:
                x += dx
                y += dy
                points.append((x, y))
        return points

    def __str__(self):
        return f"{self.start[0]},{self.start[1]} -> {self.end[0]},{self.end[1]}"

    def __repr__(self):
        return str(self)
