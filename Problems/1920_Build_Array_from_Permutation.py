# Runtime: 116 ms, faster than 91.57% of Python3 online submissions for Build Array from Permutation.
# Memory Usage: 14.7 MB, less than 8.55% of Python3 online submissions for Build Array from Permutation.
# https://leetcode.com/submissions/detail/592158589/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0 for i in range(len(nums))]
        for i in nums:
            ans[i] = nums[nums[i]]
        return ans
