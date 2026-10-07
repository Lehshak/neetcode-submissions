class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False
        mid = sum(nums) // 2

        memo = dict()
        def find_mid(total, i):
            if total == mid:
                return True
            elif total > mid or i >= len(nums):
                return False

            state = (total, i)
            if state in memo:
                return memo[state]
            
            memo[state] = find_mid(total, i+1) or find_mid(total + nums[i], i+1)
            return memo[state]
        return find_mid(0, 0)




        