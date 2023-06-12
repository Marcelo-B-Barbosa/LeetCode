#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    # Using a set (better solution)
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        maxLength = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength

    # Using a Dict (my original solution)
    def lengthOfLongestSubstring_2(self, s: str) -> int:

        l = 0
        positions = {}
        maxLength = 0

        for r in range(len(s)):
            if s[r] in positions:
                new_l = positions[s[r]] + 1
                for i in range(l, new_l):
                    positions.pop(s[i])
                l = new_l
            positions[s[r]] = r
            maxLength = max(maxLength, r - l + 1)

        return maxLength

        
# @lc code=end

