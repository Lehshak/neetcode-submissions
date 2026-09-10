class Solution:
    def rob(self, nums: List[int]) -> int:
        money = {0: nums[0]}

        for i in range(1, len(nums)):
            money[i] = max(nums[i] + money.get(i-2,0), money[i-1])

        return money[len(nums)-1]



            


        