class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        lHeightI = 0
        rHeightI = len(height)-1

        maxArea = 0

        while lHeightI < rHeightI:
            lHeight = height[lHeightI]
            rHeight = height[rHeightI]

            area = min(lHeight, rHeight) * (rHeightI-lHeightI)
            maxArea = max(area, maxArea)

            if lHeight < rHeight:
                lHeightI += 1
            else:
                rHeightI -= 1
        
        return maxArea
