class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l, r = 0, len(people)-1
        res = 0

        while l<=r:
            total = people[l] + people[r]
            if total<=limit:
                l += 1
            r -= 1
            res += 1
            print(l,r)
        return res
            

# 1 2 2 3 3