class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        houses = [0] * (N +1)
        for i in range(N):
            houses[i] = nums[i]+max(houses[:i-1], default=0)
        return max(houses)