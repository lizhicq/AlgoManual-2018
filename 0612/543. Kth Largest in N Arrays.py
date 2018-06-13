class Solution:
    """
    @param arrays: a list of array
    @param k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        from heapq import heappop, heappush
        # init
        m = len(arrays)
        heap = []
        for i in range(m):
            if arrays[i]:
                arrays[i].sort(reverse=True)
                heappush(heap, (-arrays[i][0], i, 0))
        while k > 1:
            max_element = heappop(heap)
            x, y = max_element[1], max_element[2]
            if y+1 < len(arrays[x]):
                heappush(heap, (-arrays[x][y+1], x, y+1))
            k -= 1
        return - heappop(heap)[0]

if __name__ == "__main__":
    arrays = [[9,3,2,4,7],[1,2,3,4,8]]
    print Solution().KthInArrays(arrays, 3)