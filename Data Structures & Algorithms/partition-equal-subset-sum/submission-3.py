class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        amount = sum(nums) / 2
        if amount % 1 != 0:
            # cannot split into parts evenly
            return False

        amount = int(amount)

        memo = dict()
        def rec(i, curr_amount):
            if curr_amount == amount:
                return True
            elif i >= len(nums) or curr_amount > amount:
                # i out of bounds
                return False
            
            state = (i, curr_amount)
            if state in memo:
                return memo[state]

            result = rec(i+1, curr_amount) or rec(i+1,  curr_amount+nums[i])
            memo[state] = result

            return result

        return rec(0, 0)



        