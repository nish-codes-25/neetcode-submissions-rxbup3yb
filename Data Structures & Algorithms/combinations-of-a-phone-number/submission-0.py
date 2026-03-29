class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        numberMapping = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        res = []

        substr = []

        def dfs(i):
            if i>=len(digits):
                res.append("".join(substr))
                return

            for c in numberMapping.get(digits[i]):
                substr.append(c)
                dfs(i+1)
                substr.pop()
            
        dfs(0)
        return res
        