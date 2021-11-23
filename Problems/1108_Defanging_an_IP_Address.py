# Runtime: 44 ms, faster than 12.40% of Python3 online submissions for Defanging an IP Address.
# Memory Usage: 14.3 MB, less than 36.70% of Python3 online submissions for Defanging an IP Address.
# https://leetcode.com/submissions/detail/591522241/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
