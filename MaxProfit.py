def max_profit(prices):
    if len(prices) <= 1:
        return 0
    left  = prices[:len(prices)//2]
    right = prices[len(prices)//2:]
    left_profit  = max_profit(left)
    right_profit = max_profit(right)
    middle_profit = max(right) - min(left)
    return max(left_profit, right_profit, middle_profit)

a = [20, 60, 10, 35, 50]
print(max_profit(a))