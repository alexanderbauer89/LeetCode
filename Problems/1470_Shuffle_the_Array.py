# Runtime: 77 ms, faster than 21.61% of Python3 online submissions for Shuffle the Array.
# Memory Usage: 14.5 MB, less than 51.45% of Python3 online submissions for Shuffle the Array.
# https://leetcode.com/submissions/detail/592177725/

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[n+i])
        return output
