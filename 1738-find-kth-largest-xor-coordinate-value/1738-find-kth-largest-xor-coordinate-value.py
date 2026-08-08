class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        values = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    matrix[i][j] ^= matrix[i - 1][j]

                if j > 0:
                    matrix[i][j] ^= matrix[i][j - 1]

                if i > 0 and j > 0:
                    matrix[i][j] ^= matrix[i - 1][j - 1]

                values.append(matrix[i][j])

        values.sort(reverse=True)

        return values[k - 1]