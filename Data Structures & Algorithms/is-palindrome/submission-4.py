class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            print(l, r, s[l], s[r])
            while l<r and not self.isAlphaNum(s[l]):
                l += 1
            while r>l and not self.isAlphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l+1, r-1
        return True

    def isAlphaNum(self, ch):
        return (
            (ord("a") <= ord(ch) <= ord("z"))
            or (ord("A") <= ord(ch) <= ord("Z"))
            or (ord('0') <= ord(ch) <= ord('9'))
        )
