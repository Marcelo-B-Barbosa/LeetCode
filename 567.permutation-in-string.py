#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1 = [0] * 26
        countS2 = [0] * 26

        # Check first window
        window = len(s1)
        for i in range(window):
            countS1[ord(s1[i]) - ord('a')] += 1
            countS2[ord(s2[i]) - ord('a')] += 1

        if countS1 == countS2:
            return True
        
        # Move window one character at a time
        for i in range(window, len(s2)):
            countS2[ord(s2[i]) - ord('a')] += 1
            countS2[ord(s2[i-window]) - ord('a')] -= 1
            if countS1 == countS2:
                return True
            
        return False


        
# @lc code=end

