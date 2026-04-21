class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, val):
            if i==len(nums):
                return  val == 0
            if (i, val) in dp:
                return dp[(i, val)]
                
            dp[(i, val)] = dfs(i+1, val-nums[i]) + dfs(i+1, val+nums[i])
            return dp[(i, val)]

        return dfs(0, target)

        