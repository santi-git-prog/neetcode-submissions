
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i, j, k):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            if board[i][j] != word[k]:
                return False

            ch = board[i][j]
            board[i][j] = '#'

            ans = (dfs(i+1, j, k+1) or
                   dfs(i-1, j, k+1) or
                   dfs(i, j+1, k+1) or
                   dfs(i, j-1, k+1))

            board[i][j] = ch
            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
