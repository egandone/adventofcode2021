class BingoCell:
    def __init__(self, v):
        self._v = int(v)
        self._marked = False

    def value(self):
        return self._v

    def mark(self):
        self._marked = True

    def marked(self):
        return self._marked

    def __str__(self):
        if self._marked:
            return f"{self._v:>2}(*)"
        else:
            return f"{self._v:>2}   "

    def __repl__(self):
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
                if cell.value() == num:
                    cell.mark()
                    if all([_.marked() for _ in row]):
                        self.bingo = True
                    else:
                        column = []
                        for r in self._rows:
                            column.append(r[ix])
                        if all([_.marked() for _ in column]):
                            self.bingo = True

    def get_unmarked_sum(self):
        sum = 0
        for row in self._rows:
            for cell in row:
                if not cell.marked():
                    sum += cell.value()
        return sum

    def __str__(self):
        lines = ["BINGO" if self.bingo else ""]
        for row in self._rows:
            lines.append(" ".join([str(_) for _ in row]))
        return "\n".join(lines)

    def __repr__(self):
        return str(self)
