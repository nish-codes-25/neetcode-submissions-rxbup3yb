class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n!=1:
            num = str(n)
            sum = 0
            for digit in num:
                digit = int(digit)
                sum += digit ** 2
            if sum in visit:
                return False
            visit.add(sum)
            n = sum

        return True
