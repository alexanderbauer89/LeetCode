# Runtime: 73 ms, faster than 16.08% of Python3 online submissions for Final Value of Variable After Performing Operations.
# Memory Usage: 14.1 MB, less than 76.55% of Python3 online submissions for Final Value of Variable After Performing Operations.
# https://leetcode.com/submissions/detail/591517586/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for item in operations:
            if item[1] == '-':
                x -= 1
            else:
                x += 1
        return x
