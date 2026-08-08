class Solution:
    def countElements(self, nums, k):

        # If k is 0, every element is valid
        if k == 0:
            return len(nums)

        # Sort the array
        nums.sort()

        n = len(nums)
        answer = 0

        # This value must be strictly smaller
        # than the element at n-k
        limit = nums[n - k]

        for i in range(n - k):

            if nums[i] < limit:
                answer += 1

        return answer