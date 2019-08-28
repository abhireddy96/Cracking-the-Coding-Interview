"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?

Solution:
1. Perform a circular rotation on each layer, moving the
top edge -> right edge
right edge -> bottom edge
bottom edge -> left edge
left edge -> top edge
2. Swap on each layer, starting from the outermost layer and working our way inwards.
"""
__author__ = 'abhireddy96'
from typing import List


class Solution:
    def rotateMatrix(self, matrix: List):
        n = len(matrix)

        for layer in range(n // 2):
            # We perform such a swap on each layer, starting from the outermost layer and working our way inwards.
            for i in range(layer, n - layer - 1):
                # save top
                top = matrix[layer][i]

                # left -> top
                matrix[layer][i] = matrix[-i - 1][layer]

                # bottom -> left
                matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

                # right -> bottom
                matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

                # top -> right
                matrix[i][- layer - 1] = top

        return matrix


if __name__ == "__main__":
    print(*Solution().rotateMatrix(
        [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
    ))


