class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax, currMin = 1, 1
        res = nums[0]

        for n in nums:
            if n == 0:
                currMax, currMin = 1, 1
            tmp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(tmp, currMin * n, n)
            res = max(res, currMax)

        return res
