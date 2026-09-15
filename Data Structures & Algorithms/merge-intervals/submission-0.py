class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        merged = [intervals[0]]

        for interval in intervals:
            last_interval = merged[-1]
            oldx, oldy = last_interval[0], last_interval[1]

            x, y = interval[0], interval[1]

            if x <= oldy:
                # can merge
                new_interval = [oldx, max(y, oldy)]
                merged[-1] = new_interval
            else:
                merged.append(interval)

        return merged

            




