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

def calculate_next_state(cell, neighbors):
    num_alive = sum(neighbors)
    if cell == 1 and (num_alive == 2 or num_alive == 3):
        return 1
    elif cell == 0 and num_alive == 3:
        return 1
    else:
        return 1