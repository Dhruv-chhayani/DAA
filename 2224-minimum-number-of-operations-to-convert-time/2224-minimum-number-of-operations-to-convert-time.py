class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        h1, m1 = map(int, current.split(":"))
        h2, m2 = map(int, correct.split(":"))

        current_minutes = h1 * 60 + m1
        correct_minutes = h2 * 60 + m2

        diff = correct_minutes - current_minutes
        operations = 0

        for step in [60, 15, 5, 1]:
            operations += diff // step
            diff %= step

        return operations