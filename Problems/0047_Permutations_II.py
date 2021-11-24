# Runtime: 56 ms, faster than 86.87% of Python3 online submissions for Permutations II.
# Memory Usage: 14.3 MB, less than 97.40% of Python3 online submissions for Permutations II.
# https://leetcode.com/submissions/detail/592154588/

import itertools

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
           return list(set(itertools.permutations(nums)))
