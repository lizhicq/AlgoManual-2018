class Solution:
    """
        @para grid: a boolean 2D matrix
        @return: an integer
    """

    def numIslands(self, grid):
        if len(grid) == 0:
            return 0
        nrow, ncol = len(grid), len(grid[0])
        visited = [[False for j in range(ncol)] for i in range(nrow)]

        def check(x, y):
            if 0 <= x < nrow and 0 <= y < ncol and grid[x][y] and not visited[x][y]:
                return True
            return False

        def bfs(x, y):
            q = [(x, y)]
            nbrow = [1, 0, -1, 0]
            nbcol = [0, 1, 0, -1]
            while len(q) > 0:
                x, y = q.pop(0)
                for i in range(4):
                    new_x = x + nbrow[i]
                    new_y = y + nbcol[i]
                    if check(new_x, new_y):
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))

        def dfs(x, y):
            nbrow = [1, 0, -1, 0]
            nbcol = [0, 1, 0, -1]
            for i in range(4):
                new_x = x + nbrow[i]
                new_y = y + nbcol[i]
                if check(new_x, new_y):
                    visited[new_x][new_y] = True
                    dfs(new_x, new_y)

        num_islands = 0
        for row in range(nrow):
            for col in range(ncol):
                if check(row, col):
                    visited[row][col] = True
                    dfs(row, col)
                    num_islands += 1
        return num_islands