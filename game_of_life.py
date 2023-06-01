import random
import time

# Initialize Grid
def initialize_grid(size, prob):
    grid = []
    for i in range(size):
        row = []
        for j in range(size):
            if random.uniform(0, 1) < prob:
                row.append(1)
            else:
                row.append(0)
        grid.append(row)
    return grid

def get_neighbors(board, row, col):
    rows = len(board)
    cols = len(board[0])
    live_neighbors = 0
    for i in range(max(0, row-1), min(rows, row+2)):
        for j in range(max(0, col-1), min(cols, col+2)):
            if board[i][j] == 1 and (i != row or j != col):
                live_neighbors += 1
    return live_neighbors

def calculate_next_state(cell, neighbors):
    num_alive = sum(neighbors)
    if cell == 1 and (num_alive == 2 or num_alive == 3):
        return 1
    elif cell == 0 and num_alive == 3:
        return 1
    else:
        return 1


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