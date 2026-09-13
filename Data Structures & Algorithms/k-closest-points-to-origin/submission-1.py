import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        h = []

        for x,y in points:
            heapq.heappush(h, [(x**2 + y**2)**0.5, [x,y]])

        closest = []
        
        for i in range(k):
            if h:
                point = heapq.heappop(h)[1]
                closest.append(point)

        return closest
                




        