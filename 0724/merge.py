import heapq


class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """

    def mergeKSortedIntervalLists(self, intervals):
        heap = []
        for x, interval_list in enumerate(intervals):
            if len(interval_list) > 0:
                heapq.heappush(heap, (interval_list[0].start,
                                      interval_list[0].end, x, 0))
                # which (start, end, which list, which interval)

        start, end, x, y = heapq.heappop(heap)  # get the least start interval
        if y + 1 < len(intervals[x]):
            heapq.heappush(heap, (intervals[x][y + 1].start,
                                  intervals[x][y + 1].end, x, y + 1))
        res = []
        while len(heap) > 0:
            cur = heapq.heappop(heap)  # (new_start, new_end, x, y)
            if end >= cur[0]:
                end = max(end, cur[1])
            else:
                res.append(Interval(start, end))
                start = cur[0]
                end = cur[1]
            x, y = cur[2], cur[3]
            if y + 1 < len(intervals[x]):
                heapq.heappush(heap, (intervals[x][y + 1].start,
                                      intervals[x][y + 1].end, x, y + 1))
        res.append(Interval(start, end))
        return res