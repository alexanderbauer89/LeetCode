# Runtime: 52 ms, faster than 82.75% of Python3 online submissions for Shuffle String.
# Memory Usage: 14.3 MB, less than 22.66% of Python3 online submissions for Shuffle String.
# https://leetcode.com/submissions/detail/592184318/

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        old_string = list(s)
        new_string = [''] * len(indices)
        counter = 0
        for n in indices:
            new_string[n] = old_string[counter]
            counter += 1
        return ''.join(new_string)
