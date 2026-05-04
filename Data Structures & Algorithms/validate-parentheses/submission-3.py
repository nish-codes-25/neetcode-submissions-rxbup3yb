class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for ch in s:
            if ch in closeToOpen.keys():
                if stack and closeToOpen[ch] == stack.pop():
                    continue
                else:
                    return False
            stack.append(ch)

        return stack == []