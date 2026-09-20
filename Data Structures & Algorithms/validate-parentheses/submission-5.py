class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {")": "(", "]": "[", "}": "{"}

        stack = []
        for ch in s:
            if ch in bracketMap:
                if stack and stack[-1] == bracketMap[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return stack == []
        