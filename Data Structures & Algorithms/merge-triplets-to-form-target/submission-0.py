class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()

        for a in triplets:
            if a[0] > target[0] or a[1] > target[1] or a[2] > target[2]:
                continue
            for i, v in enumerate(a):
                if v==target[i]:
                    good.add(i)
            if len(good)==3:
                return True
        return False