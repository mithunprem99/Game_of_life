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

def test_get_neighbor():
    board=[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert game_of_life.get_neighbors(board,1,1)==2


def test_update_board():
    grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    new_grid = game_of_life.update_board(grid)
    expected_grid = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]

    assert new_grid == expected_grid[::-1]
def test_update_board():
    grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    new_grid = game_of_life.update_board(grid)
    expected_grid = [[0, 0, 0], [1, 1, 1], [0, 0, 0]]
    assert new_grid == expected_grid




    assert new_grid == expected_grid
    new_grid = game_of_life.update_board(new_grid)
    expected_grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    assert new_grid == expected_grid


def test_render_grid(capsys):
    grid = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
    game_of_life.render_grid(grid)
    captured = capsys.readouterr()
    assert captured.out == '*#*\n*#*\n*#*\n'