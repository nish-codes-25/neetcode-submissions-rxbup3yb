class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def dfs(i, val):
            if i==len(nums):
                return  val == 0
            count = dfs(i+1, val-nums[i]) + dfs(i+1, val+nums[i])
            return count

        return dfs(0, target)

        