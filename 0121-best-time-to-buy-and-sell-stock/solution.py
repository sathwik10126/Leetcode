class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_profit=prices[0]
        max_profit=0
        for i in prices:
            if (min_profit>i):
                min_profit=i
            else:
                profit=i-min_profit
                max_profit=max(profit,max_profit)
        return max_profit
            
