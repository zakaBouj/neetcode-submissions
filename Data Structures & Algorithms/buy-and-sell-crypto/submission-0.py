class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        buy_day, sell_day = 0, 0
        while sell_day < len(prices) - 1:
            sell_day += 1
            if prices[sell_day] < prices[buy_day]:
                buy_day = sell_day
            
            current_profit = prices[sell_day] - prices[buy_day]
            max_profit = max(current_profit, max_profit)

        return max_profit