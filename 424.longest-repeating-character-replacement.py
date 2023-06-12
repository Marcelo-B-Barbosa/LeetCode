#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#

# @lc code=start
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # 1. (r - l + 1): size of the window
            # 2. max(count.values()): maximum number of equal characters
            # 1 - 2 : number of characters that need to be changed.
            # If larger than k, l must move
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res
        
# @lc code=end

