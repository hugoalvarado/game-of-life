import pytest
from main import count_neighbors


def test_count_neighbors():
    total = count_neighbors([[1]], 0, 0)
    assert total == 8

    total = count_neighbors([[0]], 0, 0)
    assert total == 0

    grid = [[1, 1, 1, ],
            [1, 1, 1, ],
            [1, 1, 1, ]]
    total = count_neighbors(grid, 2, 2)
    assert total == 8

    grid = [[1, 1, 1, ],
            [1, 1, 1, ],
            [1, 1, 1, ]]
    total = count_neighbors(grid, 1, 1)
    assert total == 8

    grid = [[1, 1, 1, ],
            [0, 0, 0, ],
            [0, 0, 0, ]]
    total = count_neighbors(grid, 1, 1)
    assert total == 3

    grid = [[1, 1, 1, ],
            [0, 0, 0, ],
            [1, 0, 1, ]]
    total = count_neighbors(grid, 1, 1)
    assert total == 5

    grid = [[1, 0, 0, ],
            [0, 0, 0, ],
            [0, 0, 1, ]]
    total = count_neighbors(grid, 1, 1)
    assert total == 2

    grid = [[1, 1, 1, ],
            [0, 0, 0, ],
            [1, 0, 1, ]]
    total = count_neighbors(grid, 1, 2)
    assert total == 5

