class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l<r:
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m

        pivot = l

        def binary_search(start, end, num):
            while start<=end:
                m = (start+end)//2
                if nums[m] < num:
                    start = m+1
                elif nums[m] > num:
                    end = m-1
                else:
                    return m
            return -1

        res = binary_search(0, pivot-1, target)
        if res!=-1:
            return res
        return binary_search(pivot, len(nums)-1, target)


                

