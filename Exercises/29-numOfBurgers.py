# Number of Burgers with No Waste of Ingredients
# Given two integers tomatoSlices and cheeseSlices. The ingredients of different burgers are as follows:
# - Jumbo Burger: 4 tomato slices and 1 cheese slice.
# - Small Burger: 2 Tomato slices and 1 cheese slice.
# Return [total_jumbo, total_small] so that the number of remaining tomatoSlices equal to 0 and the number of remaining 
# cheeseSlices equal to 0. If it is not possible to make the remaining tomatoSlices and cheeseSlices equal to 0 return [].

# Constraints:
# 0 <= tomatoSlices <= 10^7
# 0 <= cheeseSlices <= 10^7

class Solution(object):
    def numOfBurgers(self, x, y):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        J: 4x 1y
        S: 2x 1y
        """
        j = x - 2*y
        if j % 2: return []
        j /= 2
        if j < 0: return []
        s = y-j
        if j >= 0 and s >= 0: return [int(j),int(s)]
        return []
