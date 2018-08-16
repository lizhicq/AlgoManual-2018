class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):

        def check(mid): # if mid is large enough to make k people finish their work before mid
            page_left = num = 0
            for page in pages:
                if page > mid:
                    return False
                if page > page_left:
                    page_left = mid
                    num += 1
                if page < page_left:
                    page_left -= page
            return num <= k

        start, end = 1, 65536
        while start + 1 < end:
            mid = start + (end - start) / 2
            if check(mid):
                end = mid
            else:
                start = mid

        if check(start): # start is large enough
            return start
        return end

if __name__ == "__main__":
    print Solution().copyBooks([3,2,4], 2)


