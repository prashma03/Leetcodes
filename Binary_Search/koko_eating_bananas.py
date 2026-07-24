from typing import List

class Solution:
    def canEat(self, piles: List[int], h: int, speed: int) -> bool:
        hours = 0

        for pile in piles:
            hours += (pile + speed - 1) // speed  # Ceiling division
            if hours > h:
                return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if self.canEat(piles, h, mid):
                right = mid
            else:
                left = mid + 1

        return left
