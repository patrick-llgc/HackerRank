#!/bin/python3

import sys


n = int(input().strip())
grid = []
grid_i = 0
for grid_i in range(n):
    grid_t = str(input().strip())
    grid.append(grid_t)

new_map = []
for i in range(0, n):
    new_line = ''
    for j in range(0, n):
        t_char = grid[i][j]
        if not (i==0 or i==n-1 or j==0 or j==n-1):
            # not border
            current_cell = int(grid[i][j])
            if current_cell > int(grid[i][j+1]) and current_cell > int(grid[i][j-1]):
                if current_cell > int(grid[i-1][j]) and current_cell > int(grid[i+1][j]):
                    t_char = 'X'
        new_line = new_line + t_char
    new_map.append(new_line)

for line in new_map:
    print(line)
                    