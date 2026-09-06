class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for k in range(len(nums)):
            
            k_num = nums[k]

            # nums[k] = - nums[i] - nums[j]

            l, r = 0, len(nums) - 1
            while l < r:

                if l == k:
                    l+=1
                    continue
                elif r == k:
                    r-=1
                    continue

                total = k_num + nums[l] + nums[r]
                if total == 0:
                    res.add(tuple((sorted([k_num, nums[l], nums[r]]))))
                    r-=1
                    l+=1
                elif total > 0:
                    r-=1
                else:
                    l+=1
        return [list(x) for x in res]
        

            





            

                






            