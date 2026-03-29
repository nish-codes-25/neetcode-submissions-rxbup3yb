class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] #(index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                print('pop', stack)
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i-index))
                start = index
            stack.append((start, h))

        print(stack)

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights)-i))
    
        return maxArea