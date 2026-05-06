class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        prefix = ''
        minLen = min([len(word) for word in strs])
        while i<minLen:
            ch = strs[0][i]
            for word in strs:
                if word[i] != ch:
                    return prefix
            prefix = strs[0][:i+1]
            i += 1
        return prefix
            