class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int,
                         energy: list[int], experience: list[int]) -> int:

        hours = 0
        currentEnergy = initialEnergy
        currentExperience = initialExperience

        for i in range(len(energy)):

            # Train energy if needed
            if currentEnergy <= energy[i]:
                needed = energy[i] + 1 - currentEnergy
                hours += needed
                currentEnergy += needed

            # Fight opponent
            currentEnergy -= energy[i]

            # Train experience if needed
            if currentExperience <= experience[i]:
                needed = experience[i] + 1 - currentExperience
                hours += needed
                currentExperience += needed

            # Gain experience
            currentExperience += experience[i]

        return hours