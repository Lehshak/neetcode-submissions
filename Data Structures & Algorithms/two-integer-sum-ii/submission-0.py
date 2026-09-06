class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        lp = 0
        ep = len(numbers) - 1

        while lp < ep:
            left_num = numbers[lp]
            right_num = numbers[ep]

            total = left_num + right_num
            if total == target:
                return [lp + 1, ep + 1]
            elif total < target:
                lp += 1
            else:
                ep -= 1


        

        return []

        
            
        