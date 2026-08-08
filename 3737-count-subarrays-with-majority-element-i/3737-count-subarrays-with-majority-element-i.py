class Solution:
    def countMajoritySubarrays(self, nums, target):

        n = len(nums)
        answer = 0

        # Try every starting position
        for i in range(n):

            count = 0

            # Extend the subarray
            for j in range(i, n):

                # Count target
                if nums[j] == target:
                    count += 1

                # Check if target appears more than half
                length = j - i + 1

                if count * 2 > length:
                    answer += 1

        return answer