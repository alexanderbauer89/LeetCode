# Runtime: 56 ms, faster than 82.79% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 51.48% of Python3 online submissions for Palindrome Number.
# https://leetcode.com/submissions/detail/592091803/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
