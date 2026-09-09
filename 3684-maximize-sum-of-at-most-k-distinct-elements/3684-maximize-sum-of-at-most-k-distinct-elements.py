class Solution:
    def maxKDistinct(self, nums: list[int], k: int) -> list[int]:
        nums = sorted(set(nums), reverse=True)

        return nums[:k]