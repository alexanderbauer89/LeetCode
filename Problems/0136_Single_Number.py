# Runtime: 184 ms, faster than 28.46% of Python3 online submissions for Single Number.
# Memory Usage: 16.5 MB, less than 86.13% of Python3 online submissions for Single Number.
# https://leetcode.com/submissions/detail/592164009/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result.__xor__(num)
        return result

# Runtime: 9076 ms, faster than 5.07% of Python3 online submissions for Single Number.
# Memory Usage: 16.7 MB, less than 19.60% of Python3 online submissions for Single Number.
# https://leetcode.com/submissions/detail/592161539/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n
