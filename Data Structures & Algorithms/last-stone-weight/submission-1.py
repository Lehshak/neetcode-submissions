import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negative_stones = [-stone for stone in stones]
        heapq.heapify(negative_stones)

        while len(negative_stones) > 1:
            stone1 = -heapq.heappop(negative_stones)
            stone2 = -heapq.heappop(negative_stones)

            if stone1 < stone2:
                stone2 = stone2 - stone1
                heapq.heappush(negative_stones, -stone2)
            elif stone2 < stone1:
                stone1 = stone1 - stone2
                heapq.heappush(negative_stones, -stone1)

        if len(negative_stones) == 0:
            return 0
        else:
            return -negative_stones[0]

            

        
