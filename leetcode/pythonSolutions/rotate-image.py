class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1

        while l < r :
            for i in range(r-l):
                top, bottom = l, r

                # save the topleft
                topLeft = matrix[top][l+i]

                # move bottom left into top left
                matrix[top][l+i] = matrix[bottom - i][l]

                # move bottom right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right 
                matrix[top + i][r] = topLeft
            r -= 1
            l += 1


"""

another way of solving would be to transposing the matrix and reversing each row

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        # Transpose the matrix
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # Reverse each row
        for row in matrix:
            row.reverse()


"""
