#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum(nums) is twice the sum of each one of the two subsets
        sum_nums = sum(nums)
        target = sum_nums // 2

        # If sum is odd, cannot be divided in two subsets
        if sum_nums % 2:
            return False
        
        # Set to add all possible sums of subsets
        dp = set()
        # Since we will be adding  the members of dp to each value in sums
        # we add zero to consider each number as a possible sum
        dp.add(0) 

        for n in nums:
            new_dp = set()
            for x in dp:
                if (n + x) == target:
                    return True
                new_dp.add(n + x)
                new_dp.add(x) # So that we can substitute dp for new_dp
            dp = new_dp

        return False

        

        
# @lc code=end

