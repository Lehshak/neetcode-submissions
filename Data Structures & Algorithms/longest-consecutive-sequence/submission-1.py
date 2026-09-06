class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Nset = set(nums)
        longest_streak = 0

        for num in Nset:
            if num - 1 not in Nset:
                # streak of numbers found
                starter = num - 1
                streak = 1
                while num + 1 in Nset:
                    num += 1
                    streak += 1

                longest_streak = max(longest_streak, streak)

        return longest_streak
        
            

            
        
            