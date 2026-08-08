class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        nums.sort()

        n = len(nums)
        mid = (n + 1) // 2

        small = nums[:mid][::-1]
        large = nums[mid:][::-1]

        for i in range(len(small)):
            nums[2 * i] = small[i]

        for i in range(len(large)):
            nums[2 * i + 1] = large[i]