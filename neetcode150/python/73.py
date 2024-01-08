"""73"""
from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        first_row_has_zero = 0 in matrix[0]
        first_column_has_zero = 0 in [l[0] for l in matrix]

        # Find zeroes in the rows
        for row in matrix:
            if 0 in row:
                row[0] = 0

        # Find zeroes in the columns
        for i in range(1, len(matrix[0])):
            if 0 in [row[i] for row in matrix]:
                matrix[0][i] = 0
    
        # Apply changes to the matrix
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Apply to first row and column
        matrix[0] = [0 for _ in range(len(matrix[0]))] if first_row_has_zero else matrix[0]

        if first_column_has_zero:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return 