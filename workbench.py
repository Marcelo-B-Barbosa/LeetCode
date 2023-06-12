from typing import List

class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        cars.sort(reverse=True) # Sort by the closest to the finish line
        carsStack = []
        collisions = []

        for p, s in cars:
            


    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
    

s = Solution()

cars = [[1,2],[2,1],[4,3],[7,2]]

print(s.getCollisionTimes(cars))