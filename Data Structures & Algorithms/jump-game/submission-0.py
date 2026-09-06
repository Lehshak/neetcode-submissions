class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump_capacity = nums[0]

        for i in range(1, len(nums)):
            if jump_capacity == 0:
                return False

            jump_capacity -= 1
            jump_capacity = max(jump_capacity, nums[i])
        return True