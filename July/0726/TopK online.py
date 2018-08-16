from heapq import heappop, heappush
class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.heap = []
        self.k = k

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        if len(self.heap) < self.k:
            heappush(self.heap, num)
        else:
            if self.heap[0] < num:
                heappop(self.heap)
                heappush(self.heap, num)
    """
    @return: Top k element
    """
    def topk(self):
        ans = sorted(self.heap, reverse=True)
        return ans

