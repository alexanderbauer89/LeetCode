# alternative solution to https://github.com/alexanderbauer89/LeetCode/blob/main/Problems/1929_Concatentation_of_Array.py
# Runtime: 119 ms, faster than 15.60% of Python3 online submissions for Concatenation of Array.
# Memory Usage: 14.7 MB, less than 22.12% of Python3 online submissions for Concatenation of Array.
# https://leetcode.com/submissions/detail/591528443/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2
