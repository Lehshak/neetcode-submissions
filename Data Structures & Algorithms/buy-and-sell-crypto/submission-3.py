class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        lp = 0
        rp = 1

        while rp < len(prices):
            if prices[lp] < prices[rp]:
                # profit
                max_profit = max(max_profit, prices[rp] - prices[lp])
                rp += 1
            else:
                lp = rp
                rp += 1

        return max_profit




            




        


        