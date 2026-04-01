class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i, digit in enumerate(digits[::-1]):
            num += digit * (10 ** i)

        digits = []
        while num:
            digit = num%10
            num = num//10
            digits.append(digit)

        return digits[::-1]