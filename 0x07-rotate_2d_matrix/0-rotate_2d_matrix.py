#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    # get the arrays count
    n = len(matrix)

    # Initialize the result matrix with zeros
    res = [[0] * n for _ in range(n)]

    # Flip the matrix clockwise using nested loops
    for i in range(n):
        for j in range(n):
            res[i][n - j - 1] = matrix[j][i]

    # Update the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = res[i][j]
