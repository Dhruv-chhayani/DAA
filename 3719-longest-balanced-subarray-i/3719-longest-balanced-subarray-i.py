class Solution:
    def longestBalanced(self, nums):

        n = len(nums)
        answer = 0

        # Try every starting position
        for i in range(n):

            even = set()
            odd = set()

            # Extend the subarray to the right
            for j in range(i, n):

                # Add the number to the correct set
                if nums[j] % 2 == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])

                # Check if the subarray is balanced
                if len(even) == len(odd):
                    answer = max(answer, j - i + 1)

        return answer