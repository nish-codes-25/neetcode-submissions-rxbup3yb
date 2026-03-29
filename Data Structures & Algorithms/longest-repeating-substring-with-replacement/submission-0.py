class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        res = 0

        l = 0

        for r in range(len(s)):
            frequency[s[r]] = 1 + frequency.get(s[r], 0)
            while (r-l+1) - max(frequency.values()) > k:
                frequency[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res