class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # i + j = target
        # j = target - i
        # if on i , j exists then the condition is satisfied.
        possible_solutions = dict()

        for i in range(len(nums)):
            j = target - nums[i]
            if j in possible_solutions:
                return [possible_solutions[j], i]

            else:
                possible_solutions[nums[i]] = i

        return [0,0]
        
        