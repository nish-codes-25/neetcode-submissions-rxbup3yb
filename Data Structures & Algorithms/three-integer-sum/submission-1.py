class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, num in enumerate(nums):
            l, r = i+1, len(nums)-1
            if i>0 and nums[i] == nums[i-1]:
                continue

            while l<r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])

                    while l<r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while r>l and nums[r] == nums[r-1]:
                        r -= 1

                    l += 1
                    r -= 1
        return res
                
