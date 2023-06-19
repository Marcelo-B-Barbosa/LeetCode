#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#

# @lc code=start

# The solution is to run the previous House Robber solution
# considering two sub-arrays: one including the first element
# but ignoring the last and vice-versa. This solves the fact of
# the first and last elements to be adjacent in the circle
class Solution:
    # Values in max:
    # - Case when nums only has one item
    # - Consider nums sub-array without first element
    # - Consider nums sub-array without last element
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    # Solution from 198. House Robber
    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2


# This solution worked but it's quite inefficient
class Old_Solution:
    # This runs the helper function (House Robber solution)
    # Considering all starting points
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        maxVal = 0
        for i in range(N):
            maxVal = max(
                maxVal,
                self.helper(nums[i:N] + nums[:i])
            )
        return maxVal

    # Solution from 198. House Robber but keeping track if
    # the first house was visited or not
    def helper(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [[0, False] for _ in range(N + 1)]
        dp[0] = [0, False]
        dp[1] = [nums[0], True]

        for i in range(1,N):
            if i == N-1 and dp[N-2][1]:
                dp[i+1] = dp[i]
                continue
            if dp[i-1][0] + nums[i] > dp[i][0]:
                dp[i+1] = [dp[i-1][0] + nums[i], dp[i-1][1]]
            else:
                dp[i+1] = dp[i]
        
        return dp[N][0]

        
# @lc code=end

