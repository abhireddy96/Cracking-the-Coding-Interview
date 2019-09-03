"""
A monochrome screen is stored as a single array of bytes, allowing eight consecutive pixels to be stored in one byte.
The screen has width w, where w is divisible by 8 (that is, no byte will be split across rows).
The height of the screen, of course, can be derived from the length of the array and the width.
Implement a function that draws a horizontal line from (xl, y) to (x2, y).

Solution:
1. Recognize that if xl and x2 are far away from each other, several full bytes will be contained between them.
2. These full bytes can be set one at a time by doing screen[byte] 0xFF.
3. The residual start and end of the line can be set using masks.
"""
__author__ = 'abhireddy96'


class Solution:
    def drawLine(self, screen, width, x1, x2, y):
        byte_width = width // 8
        height = len(screen) // byte_width

        # Find Smaller of x1 and x2
        if x1 < x2:
            x_start, x_end = x1, x2
        else:
            x_start, x_end = x2, x1

        # x should not be less than zero
        # x should not be greater than width
        # y should not be greater than height
        if x_start < 0 or x_end > width or y > height:
            return None

        # Create masks for start and end of line
        byte_start = y * byte_width + x_start // 8
        byte_end = y * byte_width + x_end // 8

        screen[byte_start] = (1 << (x_start % 8)) - 1
        byte_start += 1

        while byte_start < byte_end:
            screen[byte_start] = 255
            byte_start += 1

        screen[byte_start] = 255 ^ ((1 << (x_end % 8)) - 1)
        return screen


if __name__ == "__main__":
    screen = [0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0,
              0, 0, 0, 0, 0, 0, 0, 0]
    print(Solution().drawLine(screen, 64, 20, 42, 1))
