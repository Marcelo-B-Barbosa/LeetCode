#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        # Dynamic programming running dp from N to 0
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            # Single digit case and exclude any number starting on 0
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]

            # Double digit case
            if i + 1 < len(s) and (
                s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"
            ):
                dp[i] += dp[i + 2]
        return dp[0]

    # My solution
    def old_numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        if s[0] != '0':
            dp[1] = 1

        for i in range(1,len(s)):
            # One digit and two digits cases
            case1 = dp[i] * self.isValid(s[i])
            case2 = dp[i-1] * self.isValid(s[i-1:i+1])
            # Two digits case
            dp[i+1] = case1 + case2

        return dp[len(s)]

    def isValid(self, s):
        if s == '':
            return 0
        if s[0] == '0' or int(s) > 26:
            return 0
        return 1
        
# @lc code=end

