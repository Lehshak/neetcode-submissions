import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        max_h = [-num for num in nums]
        heapq.heapify(max_h)

        closest = -1
        for _ in range(k):
            closest = heapq.heappop(max_h)*-1

        return closest


        