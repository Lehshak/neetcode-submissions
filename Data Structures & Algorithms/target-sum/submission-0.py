class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        

        memo = dict()

        def rec(i, curr_sum):
            # returns the number of ways to reach target using the subarray starting from index i.
            # match found!
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            state = (i, curr_sum)
            if state in memo:
                return memo[state]

            branch1 = rec(i+1, curr_sum + nums[i])
            branch2 = rec(i+1, curr_sum - nums[i])

            memo[state] = branch1 + branch2

            return branch1 + branch2

        return rec(0, 0)

            



