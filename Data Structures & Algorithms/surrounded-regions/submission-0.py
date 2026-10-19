class Solution:
    def solve(self, board: list[list[str]]) -> None:
        n = len(board)
        m = len(board[0])

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m:
                return

            if board[i][j] != 'O':
                return

            board[i][j] = '#'

            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m-1)

        for j in range(m):
            dfs(0, j)
            dfs(n-1, j)

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'