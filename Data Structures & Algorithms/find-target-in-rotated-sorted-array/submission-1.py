class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            # elif nums[m] >= target: 
            #     if nums[l] == target:
            #         return l
            #     elif nums[l] > target:
            #         l = m+1
            #     elif nums[l] < target:
            #         r = m-1
            # elif nums[m] < target:
            #     if nums[r] == target:
            #         return r
            #     elif nums[r] > target:
            #         l = m + 1
            #     elif nums[r] < target:
            #         r = m-1


            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m+1
                else:
                    r = m-1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m-1
                else:
                    l = m+1

        return -1
