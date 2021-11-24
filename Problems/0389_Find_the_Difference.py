# Runtime: 43 ms, faster than 28.45% of Python3 online submissions for Find the Difference.
# Memory Usage: 14.4 MB, less than 32.89% of Python3 online submissions for Find the Difference.
# https://leetcode.com/submissions/detail/592173832/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in s:
            if i in t:
                t = t.replace(i, '', 1)
        return t
