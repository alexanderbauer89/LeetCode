# Runtime: 258 ms, faster than 43.76% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# Memory Usage: 14.4 MB, less than 46.01% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
# https://leetcode.com/submissions/detail/591527345/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output_list = list()
        for current_number in nums:
            count_smaller = 0
            for i in nums:
                if i < current_number:
                    count_smaller += 1
            output_list.append(count_smaller)
        return output_list
