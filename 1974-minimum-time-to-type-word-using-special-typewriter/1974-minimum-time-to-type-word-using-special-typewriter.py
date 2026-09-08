class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        current = 'a'

        for ch in word:
            distance = abs(ord(ch) - ord(current))
            time += min(distance, 26 - distance)
            time += 1
            current = ch

        return time