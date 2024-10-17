class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        least = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            value = prices[i]

            if (value - least) > profit:    
                profit = value - least

            if value < least:
                least = value
            
        return profit
        