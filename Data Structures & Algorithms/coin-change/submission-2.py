class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {coin:1 for coin in coins}
        dp[0] = 0

        for curr in range(amount+1):
            # start at 0 go all the way to amount

            # curr represents the current amount

            for coin in coins:
                if curr - coin in dp:
                    # this coin can be added

                    dp[curr] = min(dp.get(curr-coin,0) + 1, dp.get(curr, float('inf')))

        if amount not in dp:
            return -1
        else:
            return dp[amount] 
        