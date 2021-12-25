from itertools import combinations


class Scanner:
    def __init__(self, id: int):
        self._id = id
        self._points = []

    def add_point(self, pt: tuple):
        self._points.append(pt)

    def __str__(self):
        return f"[{self._id}]:{len(self._points)} points"

    def get_all_differentials(self) -> set:
        differentials = set()
        for s in range(len(self._points)):
            for d in range(s + 1, len(self._points)):
                d = tuple(_[1] - _[0] for _ in zip(self._points[s], self._points[d]))
                differentials.add(d)
                differentials.add((d[0], -d[1], d[2]))
                differentials.add((d[0], -d[1], -d[2]))
                differentials.add((d[0], d[1], -d[2]))
                differentials.add((-d[0], d[1], d[2]))
                differentials.add((-d[0], -d[1], d[2]))
                differentials.add((-d[0], -d[1], -d[2]))
                differentials.add((-d[0], d[1], -d[2]))
        return differentials
