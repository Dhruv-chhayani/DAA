class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()

        ans = []

        for query in queries:
            total = 0
            count = 0

            for num in nums:
                total += num

                if total > query:
                    break

                count += 1

            ans.append(count)

        return ans