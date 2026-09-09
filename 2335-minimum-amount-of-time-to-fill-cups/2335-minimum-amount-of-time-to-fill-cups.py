class Solution:
    def fillCups(self, amount: list[int]) -> int:
        total = sum(amount)
        maximum = max(amount)

        return max(maximum, (total + 1) // 2)