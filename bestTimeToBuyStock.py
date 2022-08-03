prices = [7,1,5,3,6,4]

max_profit = 0

left = 0
right = 1

for i in range(0,len(prices)):

    profit = prices[right] - prices[left]

    if profit < 0:
        left = right
        right = right + 1
    max_profit = max(max_profit,profit)
    if right > len(prices):
        break

    print(max_profit)