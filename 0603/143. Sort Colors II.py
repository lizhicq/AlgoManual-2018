class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        count = [0 for _ in range(k)]
        for color in colors:
            count[color - 1] += 1
        i = 0
        for j in range(len(count)):
            while count[j] > 0:
                colors[i] = j + 1
                i += 1
                count[j] -= 1
        print colors

if __name__ == "__main__":
    colors = [2,1,1,2,2]
    k = 2
    Solution().sortColors2(colors, k)