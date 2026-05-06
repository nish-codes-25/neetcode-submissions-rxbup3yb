class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        arr = [0] * (2*n)

        for i in range(n):
            arr[i] = arr[i+n] = nums[i]

        return arr