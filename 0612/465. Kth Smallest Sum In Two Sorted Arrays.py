class Solution:
    # @param {int[]} A an integer arrays sorted in ascending order
    # @param {int[]} B an integer arrays sorted in ascending order
    # @param {int} k an integer
    # @return {int} an integer
    def kthSmallestSum(self, A, B, k):
        # Write your code here
        if not A or not B:
            return 0
        from heapq import heappush, heappop
        m, n = len(A), len(B)

        heap = []
        for i in range(min(k, n)):
            heappush(heap, (A[0] + B[i], 0, i))
        while k > 1:
            min_element = heappop(heap)
            x, y = min_element[1], min_element[2]
            if x + 1 < m:
                heappush(heap, (A[x + 1] + B[y], x + 1, y))
            k -= 1
        return heappop(heap)[0]

if __name__ == "__main__":
    print Solution().kthSmallestSum([11,12,13],[4,5,6], 5)