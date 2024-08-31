class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = max(prices)
        max_profit = 0

        for x in prices:
            if x < min_price:
                min_price = x
            elif x-min_price > max_profit:
                max_profit = x-min_price

        return max_profit