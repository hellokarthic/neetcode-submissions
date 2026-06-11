class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)-1):
            for j in range(len(prices)-1, i, -1):
                if prices[j] > prices[i]:
                    returns = prices[j] - prices[i]
                    if returns > max_profit:
                        max_profit = returns
        return max_profit