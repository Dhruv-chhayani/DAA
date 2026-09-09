class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0

        # Take 1s
        take = min(k, numOnes)
        ans += take
        k -= take

        # Take 0s
        take = min(k, numZeros)
        k -= take

        # Take -1s
        take = min(k, numNegOnes)
        ans -= take

        return ans