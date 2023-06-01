import pytest
import game_of_life

# Test initialization of grid
def test_initialize_grid():
    size = 5
    prob = 0.5
    grid = game_of_life.initialize_grid(size, prob)
    assert len(grid) == size
    for row in grid:
        assert len(row) == size


def test_calculate_next_state():
    cell = 1
    neighbors = [1, 0, 1, 0, 0, 1, 1, 0]
    assert game_of_life.calculate_next_state(cell, neighbors) == 1