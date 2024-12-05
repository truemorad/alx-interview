#!/usr/bin/python3
"""
this os an interview practice
"""


def island_perimeter(grid):
    sides = 0
    index = len(grid)
    number = len(grid[0])
    for i in range(index):
        for j in range(number):
            if grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    sides += 1
                if grid[i][j + 1] == 0:
                    sides += 1
                if grid[i + 1][j] == 0:
                    sides += 1
                if grid[i - 1][j] == 0:
                    sides += 1
    return 0 if sides == 0 else sides

