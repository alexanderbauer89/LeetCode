# Runtime: 27 ms, faster than 99.49% of Python3 online submissions for Permutations.
# Memory Usage: 14.4 MB, less than 45.75% of Python3 online submissions for Permutations.
# https://leetcode.com/submissions/detail/592151307/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        import itertools
        return list(itertools.permutations(nums))
