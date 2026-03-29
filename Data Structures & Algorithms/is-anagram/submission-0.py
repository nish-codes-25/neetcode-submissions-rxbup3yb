class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDict = {}
        for _ in s:
            letterDict[_] = 1 + letterDict.get(_, 0)
        
        for _ in t:
            if letterDict.get(_):
                letterDict[_] = letterDict.get(_) - 1
                if letterDict[_] == 0:
                    letterDict.pop(_)
            else:
                letterDict[_] = 1
        if letterDict:
            return False
        return True
            