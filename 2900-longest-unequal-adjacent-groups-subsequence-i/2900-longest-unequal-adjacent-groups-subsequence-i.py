class Solution:
    def getLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        ans = []

        for i in range(len(words)):
            if not ans or groups[i] != groups[i - 1]:
                ans.append(words[i])

        return ans