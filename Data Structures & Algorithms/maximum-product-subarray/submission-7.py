class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        longest = nums[0]
        min_prod = 1
        max_prod = 1

        for n in nums:
            if n == 0:
                min_prod = 1
                max_prod = 1
                longest = max(longest, 0)
                continue
            
            temp = max_prod*n
            max_prod = max(n, temp, min_prod*n)
            min_prod = min(n, temp, min_prod*n)

            longest = max(longest, max_prod)


        return longest



 



        