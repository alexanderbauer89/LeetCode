# faster solution with dictionaries instead of lists
# Runtime: 64 ms, faster than 25.74% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14.2 MB, less than 84.81% of Python3 online submissions for Integer to Roman.
# https://leetcode.com/submissions/detail/592107730/

class Solution:
    def intToRoman(self, num: int) -> str:
        intval = {
            "0" : 1000, 
            "1" : 900,
            "2" : 500, 
            "3" : 400, 
            "4" : 100,
            "5" : 90,
            "6" : 50,
            "7" : 40,
            "8" : 10,
            "9" : 9,
            "10" : 5,
            "11" : 4,
            "12" : 1
        }
        symbols = {
            "0" : "M",
            "1" : "CM",
            "2" : "D",
            "3" : "CD",
            "4" : "C",
            "5" : "XC",
            "6" : "L",
            "7" : "XL",
            "8" : "X",
            "9": "IX",
            "10": "V",
            "11": "IV",
            "12": "I"
        }
        result = ''
        i = 0
        while  num > 0:
            for _ in range(num // intval["" + str(i) + ""]):
                result += symbols["" + str(i) + ""]
                num -= intval["" + str(i) + ""]
            i += 1
        return result


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
