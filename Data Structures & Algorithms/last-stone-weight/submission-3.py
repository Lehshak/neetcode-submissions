import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, stone*-1)

        while len(max_heap) > 1:
            stone1 = heapq.heappop(max_heap) * -1
            stone2 = heapq.heappop(max_heap) * -1

            if stone1 != stone2:
                heapq.heappush(max_heap, abs(stone1-stone2)*-1)

        if len(max_heap) == 0:
            return 0
            
        return max_heap[0]*-1



            

        
