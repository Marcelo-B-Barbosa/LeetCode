#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, t):
            if t == 0:
                res.append(curr.copy())
                return
            if t < 0 or i >= len(candidates):
                return 
            curr.append(candidates[i]) # include this candidate
            dfs(i, curr, t - candidates[i])
            curr.pop() # Exclude this candidate
            dfs(i+1, curr, t)

        dfs(0, [], target)
        return res
            
# @lc code=end

