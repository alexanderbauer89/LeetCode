# Runtime: 52 ms, faster than 7.72% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 14.4 MB, less than 9.40% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# https://leetcode.com/submissions/detail/591596209/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # split n into digits
        n = [int(d) for d in str(n)] 
        # calculate product
        product = 1
        for i in n:
            product = product * int(i)
        return product - sum(n)
