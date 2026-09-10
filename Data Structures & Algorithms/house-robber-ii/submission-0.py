class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[1], nums[0])

        # nums is at least len 3
        money1 = {0: nums[0]}
        # start robbing at house 1 end at house n-1

        money2 = {1: nums[1]}
        # start robbin house 2 end at house n

        for i in range(1, len(nums)-1):
            money1[i] = max(money1.get(i-2,0) + nums[i], money1[i-1])

        for i in range(2, len(nums)):
            money2[i] = max(money2.get(i-2,0) + nums[i], money2[i-1])

        return max(money1[len(nums)-2], money2[len(nums)-1])

        







        


        

        

