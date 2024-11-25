class Solution:
    def maxProfit(self, prices: list) -> int:
        buy = prices[0]
        profit = 0
        for current_day in range(len(prices)):
            if prices[current_day] < buy:
                buy = prices[current_day]
            elif prices[current_day] - buy > profit:
                profit = prices[current_day] - buy

        # for current_day in range(1, len(prices)):
        #     if prices[current_day] < buy:
        #         buy = prices[current_day]
        #     else:
        #         profit = max(profit, prices[current_day] - buy)
        return profit

# test code
profit = Solution()

day_price = [7,6,4,3,2,1]
print(profit.maxProfit(day_price))

