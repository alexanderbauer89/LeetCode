# Runtime: 56 ms, faster than 52.34% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 14.2 MB, less than 61.78% of Python3 online submissions for Richest Customer Wealth.
# https://leetcode.com/submissions/detail/591520867/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_account = 0
        for account in accounts:
            if(sum(account)) > max_account:
                max_account = sum(account)   
        return max_account
