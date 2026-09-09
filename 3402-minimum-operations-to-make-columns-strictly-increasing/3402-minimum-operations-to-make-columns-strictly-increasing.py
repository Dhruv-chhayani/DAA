class Solution:
    def minimumOperations(self, grid: list[list[int]]) -> int:
        operations = 0

        for j in range(len(grid[0])):
            for i in range(1, len(grid)):
                if grid[i][j] <= grid[i - 1][j]:
                    diff = grid[i - 1][j] + 1 - grid[i][j]
                    grid[i][j] += diff
                    operations += diff

        return operations