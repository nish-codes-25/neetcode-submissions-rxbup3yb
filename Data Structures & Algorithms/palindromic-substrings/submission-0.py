class Solution:
    def countSubstrings(self, s: str) -> int:
        resIdx, resLen = 0, 0
        res = 0
        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res +=1
                l-=1
                r+=1

            #even length
            l, r = i, i+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                if (r-l+1)>resLen:
                    res+=1
                l-=1
                r+=1
        return res