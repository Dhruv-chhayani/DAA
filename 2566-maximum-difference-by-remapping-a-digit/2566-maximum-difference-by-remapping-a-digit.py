class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        # Maximum number
        max_str = s
        for ch in s:
            if ch != '9':
                max_str = s.replace(ch, '9')
                break

        # Minimum number
        min_str = s.replace(s[0], '0')

        return int(max_str) - int(min_str)