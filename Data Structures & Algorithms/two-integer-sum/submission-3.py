class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in numDict:
                return [numDict[diff], i]
            numDict[num] = i
