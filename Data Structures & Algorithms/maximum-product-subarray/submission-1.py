class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix, suffix = 0, 0
        res = nums[0]
        n = len(nums)

        for i in range(n):
            prefix = nums[i] * (prefix if prefix!=0 else 1)
            suffix = nums[n-i-1] * (suffix if suffix!=0 else 1)

            res = max(prefix, suffix, res)
        return res