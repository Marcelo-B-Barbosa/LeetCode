#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_area = 0

        while l < r:
            hl = height[l]
            hr = height[r]
            area = min(hl, hr) * (r-l)
            max_area = max(max_area, area)
            if hl > hr:
                r -= 1
            else:
                l += 1

        return max_area
        
# @lc code=end

