#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n:int) -> float:
        def helper(x, n):
            # Base cases: x^0 = 1, 0 ^ n = 0
            if n == 0: return 1
            if x == 0: return 0
            
            res = helper(x, n // 2)
            res = res * res

            # if n is odd, we need to multiply by x one more time
            return x * res if n % 2 else res
        
        res = helper(x, abs(n))

        # Return the proper result if n is positive or negative
        return res if n >= 0 else 1 / res
        
# @lc code=end

