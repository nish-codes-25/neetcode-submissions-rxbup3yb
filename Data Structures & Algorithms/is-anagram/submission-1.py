class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letterDict = {}
        for _ in s:
            letterDict[_] = 1 + letterDict.get(_, 0)
        
        for _ in t:
            letterDict[_] = letterDict.get(_, 0) - 1
            if letterDict[_] < 0:
                return False
        return True
            