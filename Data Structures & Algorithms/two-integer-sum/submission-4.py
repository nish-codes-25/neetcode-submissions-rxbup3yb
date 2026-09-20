class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}
        for i, num in enumerate(nums):
            if target-num in numsDict:
                return [numsDict[target-num], i]
            numsDict[num] = i
