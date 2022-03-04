class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        sortedIntervals = sorted(intervals, key=lambda x:[x[0], x[1]])
        intervalStart = sortedIntervals[0][0]
        intervalEnd = sortedIntervals[0][1]
        res = []
        for index in range(1, len(sortedIntervals)):
            interval = sortedIntervals[index]
            if intervalStart <= interval[0] <= intervalEnd or intervalStart <= interval[1] <= intervalEnd:
                intervalStart = min(intervalStart, interval[0])
                intervalEnd = max(intervalEnd, interval[1])
            else:
                res.append([intervalStart, intervalEnd])
                intervalStart = interval[0]
                intervalEnd = interval[1]
        res.append([intervalStart, intervalEnd])
        return res
                