import re
import numpy as np

def read_matrices():
    matrices = []
    rows = []
    with open("matrix.txt") as input:
        while line := input.readline():
            line = line.strip()
            m = re.match("(-?\d+)\s*(-?\d+)\s*(-?\d+)", line)
            if m:
                rows.append([int(n) for n in m.groups()])
            if len(rows) == 3:
                matrix = np.array(rows)
                matrices.append(matrix)
                # print(matrix)
                rows = []
    return matrices
    
    
    