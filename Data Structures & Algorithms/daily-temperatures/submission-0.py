class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp>stack[-1][0]:
                stackT, stackInd = stack.pop()             
                res[stackInd] = i - stackInd
            stack.append([temp, i])
        return res


[30,38,30,36,35,40,28]

[ 1, 0, 0, 0, 0, 0, 0]

[30, 30]