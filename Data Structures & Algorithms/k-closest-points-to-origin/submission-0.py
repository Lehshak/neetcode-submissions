class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []

        for x, y in points:
            distance = (x**2 + y**2)**0.5

            heapq.heappush(max_heap, (-distance, [x,y]))

            while len(max_heap) > k:
                heapq.heappop(max_heap)

        
        res = []

        for distance, coords in max_heap:
            res.append(coords)

        return res



        