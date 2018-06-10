class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):

        edges = {i: [] for i in range(numCourses)}
        degrees = [0 for i in range(numCourses)]

        # 1. count indegree
        for i, j in prerequisites:
            edges[j].append(i)
            degrees[i] += 1
        queue, count = [], 0

        # 2. init queue
        for i in range(numCourses):
            if degrees[i] == 0:
                queue.append(i)

        # 3. bfs
        while len(queue) > 0:
            node = queue.pop(0)
            count += 1

            for x in edges[node]:
                degrees[x] -= 1
                if degrees[x] == 0:
                    queue.append(x)

        return count == numCourses