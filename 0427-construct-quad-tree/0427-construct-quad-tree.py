class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def build(row, col, size):
            same = True

            for i in range(row, row + size):
                for j in range(col, col + size):
                    if grid[i][j] != grid[row][col]:
                        same = False

            if same:
                return Node(grid[row][col] == 1, True)

            half = size // 2

            topLeft = build(row, col, half)
            topRight = build(row, col + half, half)
            bottomLeft = build(row + half, col, half)
            bottomRight = build(row + half, col + half, half)

            return Node(False, False, topLeft, topRight, bottomLeft, bottomRight)

        return build(0, 0, len(grid))