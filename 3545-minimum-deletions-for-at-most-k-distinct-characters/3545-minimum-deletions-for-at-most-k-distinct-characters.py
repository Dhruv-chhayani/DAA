from collections import Counter

class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        freq = Counter(s)

        if len(freq) <= k:
            return 0

        frequencies = sorted(freq.values())

        remove = len(freq) - k

        return sum(frequencies[:remove])