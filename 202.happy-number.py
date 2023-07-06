#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        This solution uses a Linked List with the 
        Slow-Fast algorithm to check if we are stuck in a cycle.
        '''
        slow, fast = n, self.sumSquareDigits(n)

        while slow != fast:
            fast = self.sumSquareDigits(fast)
            fast = self.sumSquareDigits(fast)
            slow = self.sumSquareDigits(slow)

        return True if fast == 1 else False

    def sumSquareDigits(self, n):
        output = 0
        while n:
            output += (n % 10) ** 2
            n = n // 10
        return output
    
    def isHappy2(self, n: int) -> bool:
        '''
        This solution uses a set to save the numbers already
        visited to check if we are in a cycle.
        '''
        visited = set()

        while n != 1:
            n = self.sumSquareDigits(n) 
            if n in visited:
                return False
            visited.add(n)

        return True
        
# @lc code=end

