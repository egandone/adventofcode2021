import re


class Line:
    def __init__(self, str):
        m = re.match(r"(\d+)\D+(\d+)\D+(\d+)\D+(\d+)", str)
        if not m:
            raise ValueError(
                f'The input string "{str}" does not match the expected pattern'
            )
        x1,y1,x2,y2 = int(m.groups()[0]),int(m.groups()[1]),int(m.groups()[2]),int(m.groups()[3])
        self.start = (x1, y1)
        self.end = (x2, y2)
        self.is_horizontal = y1 == y2
        self.is_vertical = x1 == x2

    def get_points(self):
        x_list = y_list = None
        if not self.is_vertical:
            dx = 1 if self.end[0] >= self.start[0] else -1
            x_list = [x for x in range(self.start[0], self.end[0] + dx, dx)]
        if not self.is_horizontal:
            dy = 1 if self.end[1] >= self.start[1] else -1
            y_list = [y for y in range(self.start[1], self.end[1] + dy, dy)]
        if not x_list:
            x_list = [self.start[0]] * len(y_list)
        if not y_list:
            y_list = [self.start[1]] * len(x_list)
        points = zip(x_list, y_list)
        return points

    def __str__(self):
        return f"{self.start[0]},{self.start[1]} -> {self.end[0]},{self.end[1]}"

    def __repr__(self):
        return str(self)
