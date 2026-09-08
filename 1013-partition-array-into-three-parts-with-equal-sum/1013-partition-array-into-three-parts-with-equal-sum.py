class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        total = sum(arr)

        if total % 3 != 0:
            return False

        target = total // 3
        count = 0
        curr = 0

        for num in arr:
            curr += num

            if curr == target:
                count += 1
                curr = 0

        return count >= 3