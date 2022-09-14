prices = [7,1,5,3,6,4]

def maxProfit(prices) -> int:
        max_profit = 0

        left = 0
        right = 1

        while right < len(prices):
            prices_left = prices[left]
            prices_right = prices[right]
            if prices[left] > prices[right]:
                left = right
            profit = prices[right] - prices[left]
            max_profit = max(profit, max_profit)
            right += 1
        return max_profit

print(maxProfit(prices))