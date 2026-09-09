class Solution:
    def maxSum(self, nums: list[int]) -> int:
        positive = set()

        for num in nums:
            if num > 0:
                positive.add(num)

        if positive:
            return sum(positive)

        return max(nums)