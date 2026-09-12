class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        longest = nums[0]

        suffix_prod = dict()
        prefix_prod = dict()


        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            prefix_prod[i] = curr
            if curr == 0:
                curr = 1

        curr = 1
        for i in range(len(nums)-1, -1,-1):
            curr *= nums[i]
            suffix_prod[i] = curr
            if curr == 0:
                curr = 1
        

        for i in range(len(nums)):
            curr = nums[i]
            longest = max(longest, suffix_prod[i], prefix_prod[i])

        return longest



        