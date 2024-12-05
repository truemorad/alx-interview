#!/usr/bin/python3
"""
this os an interview practice
"""


def island_perimeter(grid):
    """Return the sides of an island.
    The grid represents water by 0 and land by 1.
    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The sides of the island defined in grid.
    """
    sides = 0
    index = len(grid)
    numbers = len(grid[0])
    for i in range(index):
        for j in range(numbers):
            if grid[i][j] == 1:
                if j == numbers or grid[i][j - 1] == 0:
                    sides += 1
                if j == numbers - 1 or grid[i][j + 1] == 0:
                    sides += 1
                if i == index - 1 or grid[i + 1][j] == 0:
                    sides += 1
                if i == 0 or grid[i - 1][j] == 0:
                    sides += 1
    return 0 if sides == 0 else sides

