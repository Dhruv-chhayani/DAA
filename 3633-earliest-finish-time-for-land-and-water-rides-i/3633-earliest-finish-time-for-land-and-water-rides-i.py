class Solution:
    def earliestFinishTime(self, landStartTime: list[int], landDuration: list[int],
                           waterStartTime: list[int], waterDuration: list[int]) -> int:

        ans = float('inf')

        # Land ride first, then water ride
        for i in range(len(landStartTime)):
            land_finish = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_finish = max(land_finish, waterStartTime[j]) + waterDuration[j]
                ans = min(ans, water_finish)

        # Water ride first, then land ride
        for i in range(len(waterStartTime)):
            water_finish = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                land_finish = max(water_finish, landStartTime[j]) + landDuration[j]
                ans = min(ans, land_finish)

        return ans