#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Default case
        if num1 == '0' or num2 == '0':
            return '0'
        
        num1, num2 = num1[::-1], num2[::-1] # Easier to work in reversed order for the multiplication
        res = [0] * (len(num1) + len(num2))

        # This is multiplication as we do manually
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                res[i1 + i2] += int(num1[i1]) * int(num2[i2]) # Multiply the two digits 
                res[i1 + i2 + 1] += res[i1 + i2] // 10 # If >= 10, carry the second digit to the next index
                res[i1 + i2] = res[i1 + i2] % 10  # If >= 10, keep only the first digit in this index

        # Revert to the desired output order
        res = res[::-1]

        # The size of res can be bigger than needed, resulting in leading zeros 
        # (e.g., for 10 * 10 = 100, res = [0,1,0,0]), which must be removed
        leftZeros = 0
        while leftZeros < len(res) and res[leftZeros] == 0:
            leftZeros += 1
  
        # Map res to strings (without leading zeros) and join in a single string
        return ''.join(map(str, res[leftZeros:]))


        
# @lc code=end

