"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
column are set to 0.

Solution:
1. First pass, keep track of zero locations.
2. Second pass, to set the zeros.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def zeroMatrix(self, matrix: List):
        m = len(matrix)  # Rows
        n = len(matrix[0])  # Columns
        rows = list()
        cols = list()

        # Iterate over each cell
        for x in range(m):
            for y in range(n):
                # Fetch index of null or zero value
                if matrix[x][y] == 0:
                    rows.append(x)
                    cols.append(y)

        # Nullify row
        for row in rows:
            self.nullifyRow(matrix, row)

        # Nullify column
        for col in cols:
            self.nullifyCol(matrix, col)

        return matrix

    def nullifyRow(self, matrix, row):
        # Make row values zero
        for i in range(len(matrix[0])):
            matrix[row][i] = 0

    def nullifyCol(self, matrix, col):
        # Make column values zero
        for i in range(len(matrix)):
            matrix[i][col] = 0


if __name__ == "__main__":
    print(*Solution().zeroMatrix(
        [
            [1, 2, 3, 4, 0],
            [6, 0, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 0, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ))


