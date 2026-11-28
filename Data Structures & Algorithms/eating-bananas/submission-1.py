class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        while l<=r:
            m = (l+r)//2
            time = 0
            for p in piles:
                time += math.ceil(float(p)/m)
            if time <= h:
                res = m
                r = m - 1
            elif time > h:
                l = m + 1
        return res