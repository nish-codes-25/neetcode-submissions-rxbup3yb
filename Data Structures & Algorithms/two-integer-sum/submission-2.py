class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num in enumerate(nums):
            if (target - num) in hashMap:
                return [hashMap[target-num], i]
            hashMap[num] = i

        
