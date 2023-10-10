class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            if buy > prices[i]:
                buy = prices[i]
            
            else:
                max_profit = max(prices[i]-buy, max_profit)

        return max_profit

        
