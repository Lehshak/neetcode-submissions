class Solution:
    def climbStairs(self, n: int) -> int:
        """
        1, 2, 3, 5
        
        """
        steps = {0:0, 1:1, 2:2}

        for i in range(3, n+1):
            steps[i] = steps[i-1] + steps[i-2]

        print(steps)

        return steps[n]
        

