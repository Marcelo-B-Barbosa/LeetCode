#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# Solution found here:  https://www.youtube.com/watch?v=5WZl3MMT0Eg
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = 0

        for n in nums:
            if currSum < 0:
                currSum = 0
            currSum += n
            maxSum = max(maxSum, currSum)

        return maxSum
        
# @lc code=end

