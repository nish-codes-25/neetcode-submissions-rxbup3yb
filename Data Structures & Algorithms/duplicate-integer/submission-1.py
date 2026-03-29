class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numDict = {}
        for num in nums:
            if numDict.get(num):
                return True
            numDict[num] = 1
        return False