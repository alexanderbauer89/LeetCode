# Runtime: 101 ms, faster than 5.31% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.3 MB, less than 28.60% of Python3 online submissions for Integer to Roman.
# https://leetcode.com/submissions/detail/592100531/

class Solution:
    def intToRoman(self, num: int) -> str:
        intval = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX","V", "IV","I"]
        result = ''
        i = 0
        while  num > 0:
            for _ in range(num // intval[i]):
                result += symbol[i]
                num -= intval[i]
            i += 1
        return result
