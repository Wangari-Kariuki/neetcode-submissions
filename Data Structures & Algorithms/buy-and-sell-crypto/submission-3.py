class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices[i] - price on a given date
        #profit = value at prices[sale_day] - value at prices[buy_day]
        # we choose to consider the begining of our array as the buying price and the rest of the values as the possible selling prices
        #the day- which are indices  are ordered 
        #max_profit = max(profit, max(sell_p) - min(buy_p))
        res = 0
        i = 0 #buying day
        #sell day
        for i in range(len(prices)):
            buy_price = prices[i]
            for j in range(i + 1, len(prices)): #for each possible selling day
                sell = prices[j]
                # profit = prices[j] - prices[i] #profit is sell_price - buy_price
                res = max(res, prices[j] - prices[i])
        return res
#---------------------------------------------------------------------------------
        #USING TWO POINTERS
        # l = 0
        # r = 1
        # max_profit = 0
        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         max_profit = max(max_profit, profit)
        #     else:
        #         l = 1
        #     r += 1
        # return max_profit 

            
