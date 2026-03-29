class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        n = len(s1)
        frequency = {}
        for s in s1:
            frequency[s] = 1 + frequency.get(s, 0)

        counts = {}
        for i in range(n):
            counts[s2[i]] = 1 + counts.get(s2[i], 0)

        for i in range(len(s2)-n+1):
            if frequency == counts:
                return True
            counts[s2[i]] = counts.get(s2[i]) - 1
            if counts[s2[i]]==0:
                del counts[s2[i]]
            if i+n<len(s2):
                counts[s2[i+n]] = 1 + counts.get(s2[i+n], 0)
        return False
                
