#!/usr/bin/python3
"""
this os an interview practice
"""


def island_perimeter(grid):
    sides = 0
    for i in grid:
        for j in i:
            index = grid.index(i) - 1
            if i[j] == 1:
                if grid[index][j - 1] == 0:
                    sides += 1
                if grid[index][j + 1] == 0:
                    sides += 1
                if grid[index + 1][j] == 0:
                    sides += 1
                if grid[index - 1][j] == 0:
                    sides += 1
    return 0 if sides == 0 else sides
