#
# @lc app=leetcode id=1776 lang=python3
#
# [1776] Car Fleet II
#

# @lc code=start
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:

        pass

    # Solution from Problem 853.car-fleet
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
        
# @lc code=end

