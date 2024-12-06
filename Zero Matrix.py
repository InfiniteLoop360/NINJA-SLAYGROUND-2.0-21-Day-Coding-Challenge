from sys import *
from collections import *
from math import *

def zeroMatrix(matrix, n, m):
    # Check if the first row and column need to be zeroed
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(m))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(n))

    # Use the first row and column to mark rows and columns to be zeroed
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero out marked rows and columns
    for i in range(1, n):
        if matrix[i][0] == 0:
            for j in range(m):
                matrix[i][j] = 0

    for j in range(1, m):
        if matrix[0][j] == 0:
            for i in range(n):
                matrix[i][j] = 0

    # Zero out the first row and column if needed
    if first_row_has_zero:
        for j in range(m):
            matrix[0][j] = 0

    if first_col_has_zero:
        for i in range(n):
            matrix[i][0] = 0

    return matrix 

