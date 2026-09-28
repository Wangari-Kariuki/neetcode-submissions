class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices[i] - price on a given date
        #profit = value at prices[sale_day] - value at prices[buy_day]
        # we can choose to either consider prices at i as the selling price or the buying price or both the selling price and buying price
        #the day- which are indices  are ordered 
        #max_profit = max(profit, max(sell_p) - min(buy_p))
        res = 0
        i = 0 #buying day
        #sell day
        # j = len(prices) - 1
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i + 1, len(prices)): #for each possible selling day
                sell = prices[j]
                # profit = prices[j] - prices[i] #profit is sell_price - buy_price
                res = max(res, prices[j] - prices[i])
        return res
            
