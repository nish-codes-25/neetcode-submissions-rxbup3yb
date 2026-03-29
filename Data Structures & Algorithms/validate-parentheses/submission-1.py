class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for ch in s:
            if ch in closeToOpen:
                if res and res[-1]==closeToOpen[ch]:
                    res.pop()
                else:
                    return False
            else:
                res.append(ch)
        return True if not res else False

            