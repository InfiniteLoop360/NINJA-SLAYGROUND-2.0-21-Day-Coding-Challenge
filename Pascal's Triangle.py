from math import *

def printPascal(n: int):
    # Initialize the list to store rows of Pascal's Triangle
    result = []
    
    # Loop through each row
    for i in range(n):
        # Start each row with 1
        row = [1]
        # Calculate intermediate values of the row
        if i > 0:
            for j in range(1, i):
                row.append(result[i - 1][j - 1] + result[i - 1][j])
            # End each row with 1
            row.append(1)
        result.append(row)
    
    return result

