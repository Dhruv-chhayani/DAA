class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        answer = []

        for k, trim in queries:
            numbers = []

            for i in range(len(nums)):
                value = nums[i][-trim:]
                numbers.append((value, i))

            numbers.sort()

            answer.append(numbers[k - 1][1])

        return answer