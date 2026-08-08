class Solution:
    def specialGrid(self, n):

        size = 2 ** n
        grid = [[0] * size for _ in range(size)]

        number = 0

        def fill(row, col, size):
            nonlocal number

            # If only one cell is left, put the number there
            if size == 1:
                grid[row][col] = number
                number += 1
                return

            half = size // 2

            # Fill top-right
            fill(row, col + half, half)

            # Fill bottom-right
            fill(row + half, col + half, half)

            # Fill bottom-left
            fill(row + half, col, half)

            # Fill top-left
            fill(row, col, half)

        fill(0, 0, size)

        return grid