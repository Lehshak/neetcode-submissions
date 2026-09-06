class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total_gas = 0
        possible_start = 0

        for i in range(len(gas)):
            total_gas = gas[i] + total_gas

            curr_cost = cost[i]

            if curr_cost > total_gas:
                # this point is not possible to start on that point
                # reset the gas
                total_gas = 0
                possible_start = i + 1
            else:
                total_gas -= curr_cost

        return possible_start

            


        