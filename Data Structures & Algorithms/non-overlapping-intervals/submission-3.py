class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        last_interval = intervals[0]
        removed = 0

        # idea always pick the smallest range?
        for i in range(1, len(intervals)):
            oldx, oldy = last_interval[0], last_interval[1]
            x, y = intervals[i][0], intervals[i][1]

            if x >= oldy:
                # non overlapping
                last_interval = intervals[i]
            else:
                # if they do overlap keep the one with the smallest y
                if y < oldy:
                    last_interval = intervals[i]

                removed += 1

        return removed
