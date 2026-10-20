class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        n = len(heights)
        m = len(heights[0])

        pac = set()
        atl = set()

        def dfs(i, j, visited):
            visited.add((i, j))

            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < n and 0 <= y < m:
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x, y, visited)

        for j in range(m):
            dfs(0, j, pac)
            dfs(n-1, j, atl)

        for i in range(n):
            dfs(i, 0, pac)
            dfs(i, m-1, atl)

        ans = []

        for i in range(n):
            for j in range(m):
                if (i, j) in pac and (i, j) in atl:
                    ans.append([i, j])

        return ans