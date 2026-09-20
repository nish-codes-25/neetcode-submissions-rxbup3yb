class Solution:
    def trap(self, height: List[int]) -> int:
        lMax, rMax = 0, 0
        l, r = 0, len(height)-1
        area = 0 

        while l<r:
            lMax = max(lMax, height[l])
            rMax = max(rMax, height[r])
            if lMax <= rMax:
                area += lMax - height[l]
                l += 1
            else:
                area += rMax - height[r]
                r -= 1
        return area