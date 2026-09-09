class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                smaller = min(s[left], s[right])
                s[left] = smaller
                s[right] = smaller

            left += 1
            right -= 1

        return ''.join(s)