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


def update_board(board):
    rows = len(board)
    cols = len(board[0])
    updated_board = initialize_grid(rows, cols)
    for i in range(rows):
        for j in range(cols):
            live_neighbors = get_neighbors(board, i, j)
            if board[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    updated_board[i][j] = 0
                else:
                    updated_board[i][j] = 1
            else:
                if live_neighbors == 3:
                    updated_board[i][j] = 1
                else:
                    updated_board[i][j] = 0
    return updated_board