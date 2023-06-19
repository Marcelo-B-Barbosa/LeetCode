#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#

# @lc code=start
class Solution:
    # Same solution as before but memory efficien
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ...]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
    # My first solution
    def old_rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*(N + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(1,N):
            dp[i+1] = max(nums[i] + dp[i-1], dp[i])

        return dp[N]
        
# @lc code=end

