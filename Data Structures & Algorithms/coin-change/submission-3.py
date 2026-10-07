class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins_needed = {0:0}
        # amount: min coins needed
        for curr in range(1, amount+1):
            for coin in coins:
                if curr - coin in coins_needed:
                    prev = coins_needed.get(curr, float('inf'))
                    with_coin =  coins_needed[curr - coin] + 1

                    coins_needed[curr] = min(prev, with_coin)

        if amount not in coins_needed:
            return -1
        
        return coins_needed[amount]



        