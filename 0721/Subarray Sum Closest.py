class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        cum = [0]
        n = len(nums)
        for i in range(1, n+1):
            cum.append(cum[i-1] + nums[i-1])
        from collections import deque
        deck = deque()
        for i in range(n):
            for j in range(i+1, n+1):
                tmp = abs(cum[j] - cum[i])
                #print i, j, tmp
                if deck:
                    if deck[-1][0] > tmp:
                        while deck and deck[-1][0] > tmp:
                            deck.pop()
                        deck.append((tmp, i, j-1))
                    elif deck[-1][0] == tmp:
                        deck.append((tmp, i, j-1))
                else:
                    deck.append((tmp, i, j-1))

        #print deck
        return [deck[0][1], deck[0][2]]


class Node: # construct comparable object
    def __init__(self, _val, _pos):
        self.val = _val
        self.pos = _pos

    def __cmp__(self, other):
        if self.val == other.val:
            return self.pos - other.pos
        return self.val - other.val


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySumClosest(self, nums):
        from sys import maxsize
        sums = [Node(0, -1)]
        cum = 0
        for i, num in enumerate(nums):
            cum += num
            sums.append(Node(cum, i))
        sums.sort()
        ans = [maxsize, 0 , 0]
        for i in range(len(nums)-1):
            cum = abs(sums[i+1].val - sums[i].val)
            ans = [cum, sums[i+1].pos, sums[i].pos] if cum < ans[0] else ans

        res = [ans[1], ans[2]]
        res.sort()
        #res[0] += 1
        return res


if __name__ =="__main__":
    s = Solution()

    print s.subarraySumClosest([2147483647])