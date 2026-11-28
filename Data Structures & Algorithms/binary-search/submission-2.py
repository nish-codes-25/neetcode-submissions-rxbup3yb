class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while r >= l:
            h = (l+r)//2
            print(h, nums[h])
            if nums[h] < target:
                l = h + 1
            elif nums[h] > target:
                r = h - 1
            else:
                return h
        return -1

