# Runtime: 36 ms, faster than 88.82% of Python3 online submissions for Running Sum of 1d Array.
# Memory Usage: 14.2 MB, less than 89.96% of Python3 online submissions for Running Sum of 1d Array.

from itertools import accumulate

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return list(accumulate(nums))
