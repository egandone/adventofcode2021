import numpy as np
from matrix import read_matrices
import pytest

test_points = np.array(
    [[-1, -1, 1], [-2, -2, 2], [-3, -3, 3], [-2, -3, 1], [5, 6, -4], [8, 0, 7]]
)

matrices = read_matrices()

def test_point0_unique():
    check_set = set()
    for m in matrices:
        tx_pts = test_points @ m
        print(tx_pts[0])
        check_set.add(tuple(tx_pts[0]))
    assert len(check_set) == 24
