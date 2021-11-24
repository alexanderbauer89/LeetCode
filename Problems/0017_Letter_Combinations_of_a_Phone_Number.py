# Runtime: 28 ms, faster than 86.82% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 14.3 MB, less than 34.25% of Python3 online submissions for Letter Combinations of a Phone Number.
# https://leetcode.com/submissions/detail/592132406/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_letters = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        if len(digits) == 0:
            return ""
        elif len(digits) == 1:
            return phone_letters[digits]
        else:
            output = list()
            if len(digits) == 2:
                for a in phone_letters[digits[:1]]:
                    for b in phone_letters[digits[1:2]]:
                        output.append(a+b)
            elif len(digits) == 3:
                for a in phone_letters[digits[:1]]:
                    for b in phone_letters[digits[1:2]]:
                        for c in phone_letters[digits[2:3]]:
                            output.append(a+b+c)
            elif len(digits) == 4:
                for a in phone_letters[digits[:1]]:
                    for b in phone_letters[digits[1:2]]:
                        for c in phone_letters[digits[2:3]]:
                            for d in phone_letters[digits[3:4]]:
                                output.append(a+b+c+d)
            return output
