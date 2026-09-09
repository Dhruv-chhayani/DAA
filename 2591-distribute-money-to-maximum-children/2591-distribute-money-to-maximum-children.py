class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children:
            return -1

        money -= children

        ans = min(money // 7, children)
        money -= ans * 7
        children -= ans

        # No money left: all remaining children already have $1
        if children == 0:
            if money > 0:
                return ans - 1
            return ans

        # One child has $1 and another needs the remaining $4
        if children == 1 and money == 3:
            return ans - 1

        return ans