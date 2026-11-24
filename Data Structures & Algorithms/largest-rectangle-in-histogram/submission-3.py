class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                ind, h = stack.pop()
                maxArea = max(maxArea, (i-ind)*h)
                start = ind
            stack.append([start, height])
        for i, height in stack:
            maxArea = max(maxArea, (len(heights)-i)*height)
        return maxArea