class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        for ch in set(s):
            if s.count(ch) < k:
                parts = s.split(ch)

                answer = 0

                for part in parts:
                    answer = max(answer, self.longestSubstring(part, k))

                return answer

        return len(s)