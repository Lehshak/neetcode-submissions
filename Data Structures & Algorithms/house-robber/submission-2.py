class Solution:
    def rob(self, nums: List[int]) -> int:
        money = {0:nums[0]}
        # may amount of money at each index

        for i in range(1, len(nums)):
            money[i] = max(money.get(i-1,0), money.get(i-2, 0) + nums[i])

        return money[len(nums)-1]




        