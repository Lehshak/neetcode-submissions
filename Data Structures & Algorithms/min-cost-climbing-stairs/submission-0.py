class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        steps = {0: 0, 1:0}
        # index : min cost at that index

        for i in range(2, len(cost)+1):
            steps[i] = min(cost[i-1]+steps[i-1], cost[i-2]+steps[i-2])
        
        return steps[len(cost)]
