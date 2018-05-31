from sys import maxsize
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        start, end = 0, maxsize
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.check(mid, L, k):
                start = mid
            else:
                end = mid
        if self.check(end, L, k):
            return end
        return start

    def check(self, mid, L, k):# check if mid is small enough to make more than k woods
        num = 0

        for wood in L:
            num += wood // mid
        return num >= k





if __name__ == "__main__":
    print Solution().woodCut([232, 124, 456], 7)
