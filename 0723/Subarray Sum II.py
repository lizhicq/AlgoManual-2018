class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """

    def subarraySumII(self, A, start, end):
        # write your code here
        n = len(A)
        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + A[i - 1]

        def find(target):
            m = len(presum)
            if presum[m - 1] < target:
                return m

            start, end = 0, m - 1
            while start + 1 < end:
                mid = (start + end) / 2
                if target <= presum[mid]:
                    end = mid
                else:
                    start = mid

            if presum[end] < target:
                return end + 1
            if presum[start] < target:
                return start + 1
            return 0

        cnt = 0
        for i in range(1, n + 1):
            l = presum[i] - end
            r = presum[i] - start
            cnt += find(r + 1) - find(l)
        return cnt




if __name__ =="__main__":
    s = Solution()
    print s.subarraySumII([1,2,3,4], 1, 3)