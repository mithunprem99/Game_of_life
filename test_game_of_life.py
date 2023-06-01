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