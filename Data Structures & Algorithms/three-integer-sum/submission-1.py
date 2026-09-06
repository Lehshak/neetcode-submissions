class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()
        nums.sort()

        for k in range(len(nums)):
            lp = 0
            rp = len(nums) - 1

            k_num = nums[k]

            while lp < rp and lp != k and rp != k:
                total = nums[lp] + nums[rp] + k_num

                if total == 0:
                    res.add(tuple(sorted([nums[lp], nums[rp], k_num])))
                    rp -= 1
                    lp += 1
                elif total > 0:
                    rp -= 1
                else:
                    lp += 1

        res_lst = []

        for triple in res:
            res_lst.append(list(triple))

        return res_lst
            





            

                






            