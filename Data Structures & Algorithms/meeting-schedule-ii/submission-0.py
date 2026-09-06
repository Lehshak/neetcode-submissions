"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import defaultdict
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key=lambda x: x.start)

        min_heap = []

        for interval in intervals:

            if len(min_heap) > 0:
                # check if there's space
                earliest_room_end = heapq.heappop(min_heap)

                if interval.start >= earliest_room_end:
                    # there's space!
                    heapq.heappush(min_heap, interval.end)
                else:
                    # no Space! add back the room we removed
                    heapq.heappush(min_heap, earliest_room_end)
                    heapq.heappush(min_heap, interval.end)

            else:
                heapq.heappush(min_heap, interval.end)

        return len(min_heap)




        

            

        