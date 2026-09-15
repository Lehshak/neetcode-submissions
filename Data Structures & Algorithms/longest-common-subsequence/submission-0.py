class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # dp with index, curr_sub?
        memo = {}
        max_len = min(len(text1), len(text2)) - 1

        # keep track of both indicies
        def rec(i1, i2):
            if i1 >= len(text1) or i2 >= len(text2):
                return 0

            state = (i1,i2)
            if state in memo:
                return memo[state]

            if text1[i1] == text2[i2]:
                # match!
                branch = rec(i1+1, i2+1) + 1
                memo[state] = branch

                return branch
            else:

                branch1 = rec(i1+1, i2)
                branch2 = rec(i1, i2+1)
                memo[state] = max(branch1, branch2)

                return max(branch1, branch2)

        return rec(0,0)



