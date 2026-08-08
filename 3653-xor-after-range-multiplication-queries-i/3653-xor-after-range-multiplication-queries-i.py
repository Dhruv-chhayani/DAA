class Solution:
    def xorAfterQueries(self, nums, queries):

        MOD = 10**9 + 7

        # Process every query one by one
        for l, r, k, v in queries:

            # Start from l
            idx = l

            # Keep jumping by k
            while idx <= r:

                # Multiply the current element
                nums[idx] = (nums[idx] * v) % MOD

                # Move to the next index
                idx += k

        # Find XOR of all elements
        ans = 0

        for x in nums:
            ans ^= x

        return ans