class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_num = 1
        max_num = 1
        longest = nums[0]

        for num in nums:
            if num == 0:
                min_num = 1
                max_num = 1
                longest = max(longest, 0)
                continue

            opt1 = max_num * num
            opt2 = min_num * num
            opt3 = num

            max_num = max(opt1, opt2, opt3)
            min_num = min(opt1, opt2, opt3)

            longest = max(longest, max_num)

        return longest


 



        