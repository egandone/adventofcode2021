import itertools


class BingoCell:
    def __init__(self, v):
        self.v = int(v)
        self.marked = False

    def __str__(self):
        if self.marked:
            return f"{self.v:>2}(*)"
        else:
            return f"{self.v:>2}   "

    def __repr__(self):
        return str(self)


class BingoBoard:
    def __init__(self, lines):
        self.bingo = False
        if len(lines) != 5:
            raise ValueError("Expecting 5 lines of 5 integers")
        self._rows = []
        for line in lines:
            row = [BingoCell(v) for v in line.split()]
            if len(row) != 5:
                raise ValueError("Expecting row to contain 5 values")
            self._rows.append(row)

    def mark(self, num):
        for row in self._rows:
            for ix, cell in enumerate(row):
                if cell.v == num:
                    cell.marked = True
                    if all([_.marked for _ in row]):
                        self.bingo = True
                    elif all([_.marked for _ in [_r[ix] for _r in self._rows]]):
                        self.bingo = True

    def get_unmarked_sum(self):
        return sum(cell.v for cell in itertools.chain(*self._rows) if not cell.marked)

    def __str__(self):
        lines = ["BINGO" if self.bingo else ""]
        for row in self._rows:
            lines.append(" ".join([str(_) for _ in row]))
        return "\n".join(lines)

    def __repr__(self):
        return str(self)
