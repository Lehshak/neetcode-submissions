class Solution:
    def rob(self, nums: List[int]) -> int:


        money = {0:nums[0]}
        # may amount of money at each index
        for i in range(1, len(nums)-1):
            money[i] = max(money.get(i-1,0), money.get(i-2, 0) + nums[i])

        if len(nums) <= 1:
            return money[len(nums)-1]
        
        money2 = {1: nums[1]}
        for i in range(2, len(nums)):
            money2[i] = max(money2.get(i-1,0), money2.get(i-2, 0) + nums[i])

        return max(money2[len(nums)-1], money[len(nums)-2])

        







        


        

        

