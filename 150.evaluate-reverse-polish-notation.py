#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        Map = {
                '+': lambda x,y: x+y, 
                '-': lambda x,y: x-y, 
                '*': lambda x,y: x*y,
                '/': lambda x,y: int(x/y)
                }

        for t in tokens:
            if t in Map:
                y = stack.pop()
                x = stack.pop()
                stack.append(Map[t](x,y))
                continue
            stack.append(int(t))

        return stack.pop()
        
# @lc code=end

